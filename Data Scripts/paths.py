# To use locally, create a local_paths.py file that defines BASE_PATH
try:
    from local_settings import BASE_PATH
except ImportError:
    BASE_PATH = '/Volumes/DATA/'

try:
    from local_settings import LOCAL_BASE_PATH
except ImportError:
    BASE_PATH = '/Users/flynn/Documents/DeepLeague/'



BASE_DATA_PATH = BASE_PATH + 'data/data/'
TRAINING_PATH = BASE_PATH + 'clusters_cleaned/train/'
