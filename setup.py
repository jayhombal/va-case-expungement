import os, sys
from subprocess import Popen, PIPE

# if running on UVA collab
if UVA_COLAB:
    BASE_DIR = "./"
    DOWNLOAD_DATA = BASE_DIR + "download-data/"
    CIRCUIT_CT_PATH = DOWNLOAD_DATA + "circuit/"
    DISTRICT_CT_PATH = DOWNLOAD_DATA + "district/"
    PROCESSED_PATH = BASE_DIR + "data/"
    CIRCUIT_CT_FILENAME = "circuit_court_2009_2019.csv.gz"
    DISTRICT_CT_FILENAME = "district_court_2009_2019.csv.gz"


# if running on local
if LOCAL:
    BASE_DIR = "./"
    DOWNLOAD_DATA = BASE_DIR + "download-data/"
    CIRCUIT_CT_PATH = DOWNLOAD_DATA + "circuit/"
    DISTRICT_CT_PATH = DOWNLOAD_DATA + "district/"
    PROCESSED_PATH = BASE_DIR + "data/"
    CIRCUIT_CT_FILENAME = "circuit_court_2009_2019.csv.gz"
    DISTRICT_CT_FILENAME = "district_court_2009_2019.csv.gz"
  

