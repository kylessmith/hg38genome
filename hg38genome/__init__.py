"""Init for CBS."""

from __future__ import absolute_import
from .import kmers
from . import data
from .core.hg38_core import *
from .core.calculate_bias import calculate_bias, calculate_bin_bias

# This is extracted automatically by the top-level setup.py.
__version__ = '1.0.0'

# Check download was completed

def save_genome(name, destdir=None, mode='ftp'):
    """
    tries to download a genome from UCSC by name
    for example, 'hg38' is at
    ftp://hgdownload.cse.ucsc.edu/goldenPath/hg38/bigZips/hg38.2bit
    """
    urlpath = "%s://hgdownload.cse.ucsc.edu/goldenPath/%s/bigZips/%s.2bit" % \
              (mode, name, name)
    if destdir is None:
        destdir = getcwd()
    remotefile = urlopen(urlpath)
    assert exists(destdir), 'Desination directory %s does not exist' % destdir
    with open(join(destdir, "%s.2bit" % name), 'wb') as destfile:
        copyfileobj(remotefile, destfile)
    
    return


def download_genome():
    import sys
    from urllib.request import urlopen
    from shutil import copyfileobj
    from os.path import exists, join
    from os import getcwd
    import os

    import requests
    import shutil
    from tqdm.auto import tqdm

    name = "hg38"
    mode = "http"
    urlpath = "%s://hgdownload.cse.ucsc.edu/goldenPath/%s/bigZips/%s.2bit" % \
            (mode, name, name)
    destdir = os.path.join(os.path.split(os.path.realpath(__file__))[0], "data")
    #remotefile = urlopen(urlpath)
    
    # make an HTTP request within a context manager
    with requests.get(urlpath, stream=True) as r:
        
        # check header to get content length, in bytes
        total_length = int(r.headers.get("Content-Length"))
        
        # implement progress bar via tqdm
        with tqdm.wrapattr(r.raw, "read", total=total_length, desc="")as raw:
        
            # save the output to a file
            with open(join(destdir, "%s.2bit" % name), 'wb') as output:
                shutil.copyfileobj(raw, output)


try:
    data.get_data_file("hg38.2bit")
except FileExistsError:
    response = input("Would you like to download hg38.2bit (~800MB). [Yes/No]")

    if response.upper() == "YES":
        print("Downloading hg38.2bit...", flush=True)
        download_genome()
        