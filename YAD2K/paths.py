# Environment settings / configs

try:
    from local_settings import TRAINING_PATH
except ImportError:
    TRAINING_PATH = '/media/student/DATA/clusters_cleaned/train/'

try:
    from local_settings import VAL_PATH
except ImportError:
    VAL_PATH = '/media/student/DATA/clusters_cleaned/val/'

