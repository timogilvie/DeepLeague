# Data Scripts

This directory contains functions downloading and transforming LoL vods into data to train the model. Core functionality includes the following: 

download_youtube.py: Takes a list of Youtube videos from vod_info.csv (not in repo) and saves them locally as mp4 files
get_and_save_frames.py: Takes a mp4 vod and outputs individual frames to a directory 
get_ocr_data.py: Extracts text from individual frames using Google Vision API
read_ocr_and_lolesport_data.py: Align OCR timestamps with socket.json data from lolesport socket. (Not in repo? Presumably coming from ws://livestats.proxy.lolesports.com/stats) 
socket_stats.py: Reformatting data from lolesport data? 
save_frames.py: Duplicate of funcitonality in get_and_save_frames.py. Any reason to keep both? 
create_npz_file.py: Saves test, training, and val data as numpy files containing the images? and location of the bounding boxes identified?


Utility functions: 
file_fixer.py: Returns files in numerical order based on frame_XX.jpg
npz_stats.py: Returns the total number of images in the training directory   
quick_dirt_file_copy.py: Copies files from local directory to network storage      

paths.py includes configuration settings. Add a local_settings.py to override the standard paths that are unlikely to work on your system


