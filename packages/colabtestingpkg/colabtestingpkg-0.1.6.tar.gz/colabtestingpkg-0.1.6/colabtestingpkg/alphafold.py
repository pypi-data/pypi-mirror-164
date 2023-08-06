""""Client library for folding proteins using Cradle's implementation of Alphafold.

Example::
    from cradlebio import alphafold

    creds_path = 'path to JSON firebase credentials obtained from https://auth.internal.cradle.bio/'
    fasta_file = 'path to fasta file containing proteins to be folded'
    sequences = alphafold.predict(creds_path, fasta_file)

    for sequence in sequences:
        print(f'PDB file for folded sequence {sequence.name} is {await sequence.pdb()}')
"""
from datetime import datetime
from enum import Enum
import json
import logging
import hashlib
import os.path
from pathlib import Path
import shutil
import tempfile
from tqdm import tqdm
from typing import Dict, List, Union
import urllib
import sys

from Bio import SeqIO
from google.api_core.datetime_helpers import DatetimeWithNanoseconds
from google.api_core.exceptions import PermissionDenied
from google.cloud import firestore
from google.cloud import storage

from cradlebio import auth
from cradlebio import watch

CRADLE_GCS_BUCKET = 'cradle-bio.appspot.com'
JOBS = 'jobs'  # the name of the sub-collection where jobs are stored in Firebase
FIRESTORE_PREFIX = ''


class MsaException(Exception):
    """Indicator class for a server-side error during Multiple Sequence Alignment (MSA)"""
    pass


class PdbException(Exception):
    """Indicator class for a server-side error during sequence folding"""
    pass


class AmberRelax(Enum):
    ALL = 0  # relax all 5 PDBs
    BEST = 1  # relax only the best PDB (by plddt score)
    NONE = 2  # don't relax the PDBs at all


class Wrapper:
    def to_file(self, fname) -> None:
        pass

    def as_string(self) -> str:
        pass


class HttpOrGcsWrapper(Wrapper):
    """
    Simple wrapper around an http or gcs location that allows downloading the data at location to a file or string
    """
    location: str
    bucket: storage.Bucket

    def __init__(self, location: str, creds: auth.IdentityPlatformTokenCredentials):
        self.location = location
        gcs = storage.Client(credentials=creds.as_access_token_credentials())
        self.bucket = gcs.bucket(CRADLE_GCS_BUCKET)

    def to_file(self, fname) -> None:
        if str(self.location).startswith('https'):
            urllib.request.urlretrieve(self.location, fname)
        else:
            blob: storage.Blob = self.bucket.blob(str(self.location))
            blob.download_to_filename(fname)

    def as_string(self) -> str:
        if str(self.location).startswith('https'):
            with tempfile.NamedTemporaryFile() as f:
                urllib.request.urlretrieve(self.location, f.name)
                return open(f.name).read()
        else:
            blob: storage.Blob = self.bucket.blob(str(self.location))
            return blob.download_as_string().decode('UTF-8')


class EmptyHttpOrGcsWrapper(Wrapper):
    """
    Wraps an empty content.
    """

    def __int__(self):
        self.content = 'Alignment missing (sequence found in Swissprot?)'

    def to_file(self, fname: str) -> None:
        with open(fname, 'w') as f:
            f.write(self.content)

    def as_string(self) -> str:
        return self.content


class Sequence:
    """A protein sequence that is being folded by AlphaFold"""

    _doc: firestore.DocumentReference
    job_id: str
    user_id: str
    seq: str
    id: str
    name: str
    _a3m_path: str
    _gcs_path: str
    _creds: auth.IdentityPlatformTokenCredentials

    def __init__(self, sequence_doc: firestore.DocumentReference, creds: auth.IdentityPlatformTokenCredentials):
        """
        The Firebase document corresponding to the current sequence. This is the document that is being watched
        in order to determine when the MSA job and the structure prediction jobs are done. The relevant fields are:
          a3m: set to the path of the MSA alignment results, after a successful MSA alignment (not set if MSA fails)
          a3m_error: an error message indicating why MSA failed (not set if MSA is successful)
          pdb: set to the path of the predicted PDB structure, after a successful structure prediction
              (not set if structure prediction fails)
          pdb_error: an error message indicating why structure prediction failed
              (not set if structure prediction is successful)
        Params:
            sequence_doc: the firebase document where the sequence data is stored
        """

        self._doc = sequence_doc
        self._a3m_path = None
        self._gcs_path = None
        self._pdbs = []
        self._creds = creds

    def __str__(self) -> str:
        snapshot = self._doc.get()
        return f'Id: {self.id}\n{json.dumps(snapshot.to_dict(), indent=4)}'

    @property
    def id(self):
        return self._doc.id

    @property
    def name(self):
        return self._doc.get(['name']).get('name')

    @property
    def seq(self):
        return self._doc.get(['seq']).get('seq')

    @property
    def job_id(self):
        return self._doc.parent.parent.id

    @property
    def user_id(self):
        # the path to a sequence is 'users/<user_id>/jobs/<job_id>/sequences/<sequence_id>'
        return self._doc._path[-5]

    def to_dict(self):
        return self._doc.get().to_dict()

    def parent(self):
        """ Returns the job this sequence belongs to """
        return Job(self._doc.parent.parent, self._creds)

    def a3m(self) -> HttpOrGcsWrapper:
        """Wait for the MSA job to finish and return the path to the a3m data."""
        if self._a3m_path is None:
            result = watch.field(self._doc, 'a3m', 'a3m_error')
            if 'a3m' in result:
                self._a3m_path = HttpOrGcsWrapper(result['a3m'], self._creds)
            elif 'a3m_error' in result:
                logging.error(f'Error performing MSA for {self.name}: {result["a3m_error"]}')
                raise MsaException(result["a3m_error"])
            else:
                logging.error(f'Unknown error performing MSA for {self.name}: no result provided by server')
                raise MsaException('No result provided by server')
        elif self._a3m_path == '' and self._gcs_path is not None:
            return EmptyHttpOrGcsWrapper()

        return self._a3m_path

    def pdbs(self) -> List[HttpOrGcsWrapper]:
        """"
        Wait for the folding to finish and return the contents of the resulting pdbs as strings,
        ranked by plddt score (best first).
        """
        # First wait for the MSA (and stop if the MSA resulted in an error)
        if not self._a3m_path:
            self.a3m()
        if self._gcs_path is None:
            watch.field(self._doc, 'pdbs', 'gcs_path', 'pdb_error', 'pdbs_unrelaxed')
            # query the data again, just in case Firestore decides to call on_snapshot() multiple times for the
            # same update()
            seq_data = self._doc.get().to_dict()
            if 'pdb_error' in seq_data:
                logging.error(f'Error folding {self.name}: {seq_data["pdb_error"]}')
                raise PdbException(seq_data["pdb_error"])
            self._gcs_path = seq_data['gcs_path'] if 'gcs_path' in seq_data else ''
            self._pdbs = []
            if 'pdbs' in seq_data:
                for p in seq_data['pdbs']:
                    if p.startswith('http'):
                        self._pdbs.append(HttpOrGcsWrapper(p, self._creds))
                    else:
                        self._pdbs.append(HttpOrGcsWrapper(Path(self._gcs_path) / p, self._creds))
            elif 'pdbs_unrelaxed' in seq_data:
                for p in seq_data['pdbs_unrelaxed']:
                    self._pdbs.append(HttpOrGcsWrapper(Path(self._gcs_path) / p, self._creds))
            else:
                raise RuntimeError('Sequence document does not contained any of [pdbs, pdbs_unrelaxed, pdb_error]')
        return self._pdbs

    def pdb(self) -> HttpOrGcsWrapper:
        """ Return the PDB contents (as a string) with the highest plddt score for the given sequence """
        return self.pdbs()[0]


class Job:
    """A protein-folding job"""
    _doc: firestore.DocumentReference

    def __init__(self, job_doc: firestore.DocumentReference, creds: auth.IdentityPlatformTokenCredentials):
        self._doc = job_doc
        self._creds = creds

    @property
    def id(self):
        return self._doc.id

    @property
    def data(self):
        return self._doc.get().to_dict()

    @property
    def sequences(self):
        result = []
        for sequence_doc in self._doc.collection('sequences').stream():
            result.append(Sequence(sequence_doc.reference, self._creds))
        return result

    def __str__(self):
        data = {k: v for k, v in self.data.items() if not isinstance(v, DatetimeWithNanoseconds)}
        return f'Job: {self.id}\n{json.dumps(data, indent=4)}'


class Alphafold:
    def __init__(self, creds: auth.IdentityPlatformTokenCredentials):
        self.creds = creds
        self.client = auth.get_client(creds)

        try:
            user_doc = self.client.document(f'{FIRESTORE_PREFIX}users/{self.creds.uid}').get()
        except PermissionDenied:
            print('Access to Cradle Alphafold is only permitted for trusted testers. Please sign up at '
                  'https://ielcu542t0e.typeform.com/to/lEzf6l1E if you would like to try Cradle Alphafold.')
            sys.exit(1)

        if not user_doc.exists:
            user_doc.reference.create({})
        self.user_doc = user_doc.reference

    @staticmethod
    def _get_job_id(fasta_file: str):
        """Build and return the job name string for a given fasta file that is being folded."""
        return datetime.today().strftime('%Y-%m-%d-%H:%M:%S_') + os.path.basename(fasta_file)

    @staticmethod
    def _md5(fname):
        hash_md5 = hashlib.md5()
        with open(fname, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()

    @staticmethod
    def _parse_fasta(fasta_file: str, db_client: firestore.Client, job_doc: firestore.DocumentReference,
                     creds: auth.IdentityPlatformTokenCredentials):
        """
        Parses the given fasta file and creates a Firebase document for each sequence under
        job_id/sequences/<sequence_name> with status 'PENDING'
        """
        logging.info(f'Parsing and uploading proteins in {fasta_file}')

        # parse the proteins in the FASTA file and write them as a batch to Firestore
        batch: firestore.WriteBatch = db_client.batch()
        fasta_sequences = SeqIO.parse(fasta_file, 'fasta')
        result: List[Sequence] = []
        sequence_set = set()
        count = 0
        is_empty = True
        for fasta in fasta_sequences:
            is_empty = False
            if fasta.seq in sequence_set:
                logging.warning(f'Duplicate sequence {fasta.id}. Ignoring.')
                continue
            if len(fasta.seq) > 1400:
                raise RuntimeError(f'Sequence {fasta.id} is too long. Sequences must be shorter than 1400 AAs')
            sequence_set.add(fasta.seq)
            # since colabfold_search names sequences in the file starting with 0, we adopt
            # the same convention for convenience
            sequence_id = str(count)
            sequence_doc: firestore.DocumentReference = job_doc.collection('sequences').document(sequence_id)
            batch.create(sequence_doc, {'status': 'PENDING', 'seq': str(fasta.seq), 'name': str(fasta.id),
                                        'description': str(fasta.description)})
            result.append(Sequence(sequence_doc, creds))

            if (count + 1) % 500 == 0:  # a batch supports at most 500 operations
                batch.commit()
                batch = db_client.batch()
            count += 1
        if count > 100:
            raise RuntimeError(
                f'A maximum of 100 proteins can be folded at a time, {fasta_file} contained {count} proteins.')
        batch.commit()
        if is_empty:
            raise RuntimeError('Input fasta file is invalid or empty')
        logging.info(f'{len(sequence_set)}/{count} proteins successfully parsed and uploaded for processing.')
        return result

    def predict(self, input_data: Union[str, List[str], Dict[str, str]], show_progress: bool = True,
                block: bool = False, relax: AmberRelax = AmberRelax.ALL) -> List[Sequence]:
        """
        Returns a list of sequences corresponding to the entries in fasta_file.
        The method parses the given fasta file, and uploads it to Firebase for processing.
        Params:
          - input_data: the location of the FASTA file that contains the protein(s) to be folded if the type is string,
            a list of proteins if the type is List[str] and a dictionary of protein_name to sequence if the type is
            Dict[str,str]
          - show_progress: if true, a progress bar is shown to indicate the folding progress. Note that
            some environments such as Google Colab kill background threads as soon as the main thread is done,
            so the progress can only be shown if "block=True" is also set
          - block: if true - the method will only return after all proteins were successfully processed
        """
        db_client: firestore.Client = auth.get_client(self.creds)

        active_jobs = self.mark_stale_jobs()
        if active_jobs >= 10:
            raise RuntimeError(f'You are currently running {active_jobs} folding jobs out of a maximum of 10. '
                               f'You need to wait for some jobs to finish before creating new ones.')
        tmp_path = None
        try:
            if isinstance(input_data, str):
                if not os.path.exists(input_data):
                    raise FileNotFoundError(f'Could not find FASTA file: {input_data}')
                fasta_file = input_data
            elif isinstance(input_data, List):
                tmp_path = tempfile.mkdtemp()
                fasta_file = str(Path(tmp_path) / 'list')
                with open(fasta_file, 'w') as f:
                    for i, seq in enumerate(input_data):
                        f.write(f'>{i}\n')
                        f.write(f'{seq}\n')
            elif isinstance(input_data, Dict):
                tmp_path = tempfile.mkdtemp()
                fasta_file = str(Path(tmp_path) / 'dict')
                with open(fasta_file, 'w') as f:
                    for name, seq in input_data.items():
                        f.write(f'>{name}\n')
                        f.write(f'{seq}\n')

            md5sum = self._md5(fasta_file)
            identical_docs = self.user_doc.collection(JOBS).where('md5sum', '==', md5sum).stream()
            for job_doc in identical_docs:
                job_fields = job_doc.to_dict()
                if 'status' not in job_fields or job_fields['status'] in ['MSA_FAILED', 'FOLDING_FAILED']:
                    continue
                logging.info(f'Found session {job_doc.to_dict()} with the same hash. Returning existing session.')
                if show_progress:
                    tqdm(total=100, initial=100, unit='Done, duplicate', miniters=1, mininterval=0, ncols=110,
                         bar_format='{l_bar}{bar}|[{unit}]').close()
                return [Sequence(sequence.reference, self.creds) for sequence in
                        job_doc.reference.collection('sequences').stream()]

            job_id = self._get_job_id(fasta_file)

            # create a new job for the user and a Firestore entry pointing at the FASTA file on GCS;
            # this signals the AFAAS sever to start processing the newly uploaded FASTA file
            job_doc = self.user_doc.collection(JOBS).document(job_id)
            if job_doc.get().exists:
                raise RuntimeError(f'Duplicate session {job_id} when predicting structure for: {fasta_file}')
            if os.path.getsize(fasta_file) > 5e5:
                raise ValueError(f'Input file is too large: {fasta_file}. Max size is 500KB.')

            now = datetime.utcnow()
            job_doc.create({'creation_time': now, 'md5sum': md5sum, 'relax': relax.name})
            result = self._parse_fasta(fasta_file, db_client, job_doc, self.creds)

            # only update the status to PENDING after sequences are parsed, otherwise the server sees no sequences
            job_doc.update({'status': 'PENDING'})
            if show_progress:
                watch.add_progress_listener(job_doc, len(result))
            if block:
                for seq in result:
                    seq.pdb()
            return result
        finally:
            if tmp_path is not None:
                shutil.rmtree(tmp_path)

    def get_jobs(self, active_only=True) -> List[Job]:
        """
        Return a list of alphafold jobs for the current user. Jobs are returned ordered by creation time, starting with
        the most recent one.
        Params:
            active: if True, only jobs that are currently running are shown
        """
        done = ['DONE', 'MSA_FAILED', 'FOLDING_FAILED']
        if active_only:
            jobs_collection = self.user_doc.collection(JOBS).where('status', 'not-in', done)
        else:
            jobs_collection = self.user_doc.collection(JOBS)
        jobs = [Job(job.reference, self.creds) for job in jobs_collection.stream()]
        jobs.sort(key=lambda job: job.data['creation_time'], reverse=True)
        return jobs

    def get_job_by_id(self, job_id: str) -> Union[Job, None]:
        """Return the job with the given id for the authenticated user"""
        job_doc = self.client.document(f'{FIRESTORE_PREFIX}users/{self.creds.uid}/{JOBS}/{job_id}').get()
        if job_doc.exists:
            return Job(job_doc.reference, self.creds)
        return None

    def search_jobs(self, keyword: str, active_only=True):
        """
        Search all jobs that match the given keyword.
        Params:
          - keyword string to search for in the job status, id, md5_sum or creation time.
          - active if, True, only jobs that are currently active are returned
        """
        jobs = self.get_jobs(active_only)
        if not keyword:
            return jobs
        result = []
        for j in jobs:
            search_base = [j.data['status'], j.data['md5sum'], str(j.data['creation_time']), j.id]
            for s in search_base:
                if keyword in s:
                    result.append(j)
                    break
        return result

    def mark_stale_jobs(self) -> int:
        """ Check for jobs in the state FOLDING that haven't been updated in a long time and mark them as failed. """
        jobs_collection = self.user_doc.collection(JOBS).where('status', 'in', ['FOLDING', 'MSA_RUNNING'])
        return mark_stale_jobs(jobs_collection)


def mark_stale_jobs(jobs_collection: firestore.CollectionReference):
    active_jobs = 0
    for job in jobs_collection.stream():
        job_data = job.to_dict()
        if 'last_updated' in job_data:
            last_updated = job_data['last_update']
            if (datetime.utcnow() - last_updated).total_seconds() > 5 * 60 * 60:  # no update in 5 hours
                job.reference.update({'status': 'FOLDING_FAILED', 'pdb_error': 'Timeout - no update after 5 hours'})
                active_jobs -= 1
        elif 'fold_start_time' in job_data:
            last_updated = job_data['fold_start_time']
            # no update in 24 hours
            if (datetime.utcnow() - last_updated.replace(tzinfo=None)).total_seconds() > 24 * 60 * 60:
                job.reference.update({'status': 'FOLDING_FAILED', 'pdb_error': 'Timeout - no update after 24 hours'})
                continue
        active_jobs += 1
    return active_jobs
