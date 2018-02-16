import shutil
import os
import time
from paths import LOCAL_BASE_PATH

for folder in os.listdir(LOCAL_BASE_PATH +'data'):
    print('looking @ ', folder)
    if os.path.isdir(LOCAL_BASE_PATH + 'data/' + folder):
        if not (os.path.exists('/Volumes/DATA/data/' + folder)):
            os.mkdir('/Volumes/DATA/data/' + folder)
        for file_name in os.listdir(LOCAL_BASE_PATH+'data/' + folder):
            # frames folder special case
            if 'frames' in file_name:
                print("creating / copying frames")
                os.mkdir('/Volumes/DATA/data/' + folder + '/frames/')
                time.sleep(3000)
                src = LOCAL_BASE_PATH +'data/' + folder + '/frames/'
                dst = '/Volumes/DATA/data/' + folder + '/frames/'
                shutil.copytree(src, dst)

            print('looking @ file ', file_name)
            src = LOCAL_BASE_PATH +'data/' + folder + '/' + file_name
            dst = '/Volumes/DATA/data/' + folder
            shutil.copy(src, dst)
