# setup

BASE_DIR = "./"
DOWNLOAD_DATA = BASE_DIR + "download-data/"
CIRCUIT_CT_PATH = DOWNLOAD_DATA + "circuit/"
DISTRICT_CT_PATH = DOWNLOAD_DATA + "district/"
PROCESSED_PATH = BASE_DIR + "data/"
CIRCUIT_CT_FILENAME = "circuit_court_2009_2019.csv.gz"
DISTRICT_CT_FILENAME = "district_court_2009_2019.csv.gz"

#
if not os.path.exists(PROCESSED_PATH):
    os.makedirs(PROCESSED_PATH)
    
if not os.path.exists(DOWNLOAD_DATA):
    os.makedirs(DOWNLOAD_DATA)
    

if not os.path.exists(CIRCUIT_CT_PATH):
    os.makedirs(CIRCUIT_CT_PATH)
    

if not os.path.exists(DISTRICT_CT_PATH):
    os.makedirs(DISTRICT_CT_PATH)