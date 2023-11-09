import urllib3
import shutil
import os
import os.path
import ftplib
import gzip
import tarfile
import subprocess
import json
from itertools import product
from loreme.env import (PBCPG_URL, PBCPG_DIR, PB_EXAMPLE_DATA_URLS, EXAMPLE_DATA_DIR, HG38_FTP,
                       HG38_GENOME_PATH, HG38_ANNOT_PATH, DORADO_VERSION, DORADO_DIR, DORADO_URL,
                       DORADO_MODEL_DIR, DORADO_CONFIG, DORADO_PATH, MODKIT_URL,
                       MODKIT_DIR, ONT_EXAMPLE_DATA_URL, KAZU_090722_GENOME_URL,
                       KAZU_090722_ANNOT_URL)

def download_pbcpg(directory: str = PBCPG_DIR):
    """Download pb-CpG-tools

    Parameters
    ----------
    directory : str
        Destination directory for pb-CpG-tools
    """

    dest_tarfile = os.path.join(directory, 'pb-CpG-tools-v2.3.1-x86_64-unknown-linux-gnu.tar.gz')
    print(f'downloading to {dest_tarfile}')
    if os.path.exists(dest_tarfile):
        raise RuntimeError(f'a file already exists at {dest_tarfile}')
    http = urllib3.PoolManager()
    with http.request('GET', PBCPG_URL, preload_content=False) as r, open(dest_tarfile, 'wb') as f:
        shutil.copyfileobj(r, f)
    with tarfile.open(dest_tarfile) as tar:
        tar.extractall(path=directory)


def download_pb_example(directory: str = EXAMPLE_DATA_DIR, n_samples: int = 1):
    """Download an example datatset

    Parameters
    ----------
    directory : str
        Destination directory for example data
    n_samples : int
        Number of samples to download, max 4 [1]
    """

    if n_samples > 4:
        raise RuntimeError('n_samples parameter must be <= 4')
    hg38_genome_local_path = os.path.join(directory, os.path.basename(HG38_GENOME_PATH).replace('fna.gz', 'fa'))
    hg38_annot_local_path = os.path.join(directory, os.path.basename(HG38_ANNOT_PATH))
    if os.path.exists(hg38_genome_local_path):
        print(f'destination {hg38_genome_local_path} already exists')
    else:
        ftp = ftplib.FTP(HG38_FTP)
        ftp.login()
        with open(f'{hg38_genome_local_path}.gz', 'wb') as f:
            ftp.retrbinary(f'RETR {HG38_GENOME_PATH}', f.write)
    with gzip.open(f'{hg38_genome_local_path}.gz', 'rb') as f_in:
        with open(hg38_genome_local_path, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
    os.remove(f'{hg38_genome_local_path}.gz')
    if os.path.exists(hg38_annot_local_path):
        print(f'destination {hg38_annot_local_path} already exists')
    else:
        ftp = ftplib.FTP(HG38_FTP)
        ftp.login()
        with open(hg38_annot_local_path, 'wb') as f:
            ftp.retrbinary(f'RETR {HG38_ANNOT_PATH}', f.write)
    http = urllib3.PoolManager()
    for example_data_url in PB_EXAMPLE_DATA_URLS[:n_samples]:
        file_path = os.path.join(directory, os.path.basename(example_data_url))
        if os.path.exists(file_path):
            print(f'destination {file_path} already exists')
            continue
        with http.request('GET', example_data_url, preload_content=False) as r, open(file_path, 'wb') as out_file:
            shutil.copyfileobj(r, out_file)


def download_ont_example(directory: str = EXAMPLE_DATA_DIR):
    """Download an example datatset

    Parameters
    ----------
    directory : str
        Destination directory for example data
    """

    kazu_genome_local_path = os.path.join(directory, os.path.basename(KAZU_090722_GENOME_URL).replace('fna.gz', 'fa'))
    kazu_annot_local_path = os.path.join(directory, os.path.basename(KAZU_090722_ANNOT_URL))
    ont_example_data_local_path = os.path.join(directory, os.path.basename(ONT_EXAMPLE_DATA_URL))
    http = urllib3.PoolManager()
    if os.path.exists(kazu_genome_local_path):
        print(f'destination {kazu_genome_local_path} already exists')
    else:
        with http.request('GET', KAZU_090722_GENOME_URL, preload_content=False) as r, \
            open(kazu_genome_local_path, 'wb') as out_file:
            shutil.copyfileobj(r, out_file)
    if os.path.exists(kazu_annot_local_path):
        print(f'destination {kazu_annot_local_path} already exists')
    else:
        with http.request('GET', KAZU_090722_ANNOT_URL, preload_content=False) as r, \
            open(kazu_annot_local_path, 'wb') as out_file:
            shutil.copyfileobj(r, out_file)
    if os.path.exists(ont_example_data_local_path):
        print(f'destination {ont_example_data_local_path} already exists')
    else:
        with http.request('GET', ONT_EXAMPLE_DATA_URL, preload_content=False) as r, \
            open(ont_example_data_local_path, 'wb') as out_file:
            shutil.copyfileobj(r, out_file)


def download_dorado(pfm, directory=DORADO_DIR, model_dir=DORADO_MODEL_DIR,
                    dorado_config=DORADO_CONFIG):
    """Download dorado

    Parameters
    ----------
    pfm : str
        platform string (linux-x86, linux-arm64, osx-arm64, win64)
    directory : str
        Destination directory for dorado
    model_dir : str
        destination directory for dorado models
    """

    if pfm not in {'linux-x64', 'linux-arm64', 'osx-arm64', 'win64'}:
        raise RuntimeError('invalid platform choice')
    dest_tarfile = os.path.join(directory, f'dorado-{DORADO_VERSION}-{pfm}.tar.gz')
    print(f'downloading to {dest_tarfile}')
    if os.path.exists(dest_tarfile):
        raise RuntimeError(f'a file already exists at {dest_tarfile}')
    http = urllib3.PoolManager()
    with http.request('GET', DORADO_URL[pfm], preload_content=False) as r, open(dest_tarfile, 'wb') as f:
        shutil.copyfileobj(r, f)
    with tarfile.open(dest_tarfile) as tar:
        tar.extractall(path=directory)
    print(f'downloading models to {model_dir}')
    for speed, accuracy, in product((260, 400), ('fast', 'hac', 'sup')):
        subprocess.run((DORADO_PATH[pfm], 'download', '--directory', model_dir,
            '--model', f'dna_r10.4.1_e8.2_{speed}bps_{accuracy}@v4.1.0'))
        subprocess.run((DORADO_PATH[pfm], 'download', '--directory', model_dir,
            '--model', f'dna_r10.4.1_e8.2_{speed}bps_{accuracy}@v4.1.0_5mCG_5hmCG@v2'))
    for accuracy in 'fast', 'hac', 'sup':
        subprocess.run((DORADO_PATH[pfm], 'download', '--directory', model_dir,
            '--model', f'dna_r10.4.1_e8.2_400bps_{accuracy}@v4.2.0'))
        subprocess.run((DORADO_PATH[pfm], 'download', '--directory', model_dir,
            '--model', f'dna_r10.4.1_e8.2_400bps_{accuracy}@v4.2.0_5mCG_5hmCG@v2'))
        subprocess.run((DORADO_PATH[pfm], 'download', '--directory', model_dir,
            '--model', f"dna_r9.4.1_e8_{accuracy}@v3.{3+(accuracy=='fast')}"))
        subprocess.run((DORADO_PATH[pfm], 'download', '--directory', model_dir,
            '--model', f"dna_r9.4.1_e8_{accuracy}@v3.{3+(accuracy=='fast')}_5mCG@v0.1"))
    for modified_bases in '5mC', '6mA':
        subprocess.run((DORADO_PATH[pfm], 'download', '--directory', model_dir,
            '--model', f'dna_r10.4.1_e8.2_400bps_sup@v4.2.0_{modified_bases}@v2'))
    with open(dorado_config, 'w') as f:
        json.dump({'platform': pfm}, f)

def download_modkit(directory: str = MODKIT_DIR):
    """Download modkit

    Parameters
    ----------
    directory : str
        Destination directory for modkit
    """

    dest_tarfile = os.path.join(directory, 'modkit_v0.1.8_centos7_x86_64.tar.gz')
    print(f'downloading to {dest_tarfile}')
    if os.path.exists(dest_tarfile):
        raise RuntimeError(f'a file already exists at {dest_tarfile}')
    http = urllib3.PoolManager()
    with http.request('GET', MODKIT_URL, preload_content=False) as r, open(dest_tarfile, 'wb') as f:
        shutil.copyfileobj(r, f)
    with tarfile.open(dest_tarfile) as tar:
        tar.extractall(path=directory)