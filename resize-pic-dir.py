#!/usr/bin/python

# Resize all the pictures in a directory, calling
# resize-pic.py to do each pic
#
# C. David Sherrill, March 2019
#

import os
import pathlib

# top-level dir to find the source pics...include trailing slash
top_src_dir = '/mnt/photo/'
# look in these subdirectories of top_src_dir
src_subdirs = ['2017']

# top-level dir to put the resized pics
top_dst_dir = '/home/pi/photo/'

# filename must end in one of these suffixes
suffixes = ['.jpg', '.JPG', '.gif', '.GIF', '.png', '.PNG']

# exclude any file that has these substrings
excludes = ['thumb', 'THUMB', '@eaDir']

# file_list holds the final list of files (full paths)
file_list = []

for src_subdir in src_subdirs:
    src_dirname = top_src_dir + src_subdir;
    for root, dirs, files in os.walk(src_dirname):
        for file in files: 
            if any(exclude in file for exclude in excludes):
                continue
            if any(file.endswith(suffix) for suffix in suffixes):
                # full path to source file
                full_src_name = os.path.join(root, file)
                # now get the path without the top_src_dir
                src_rel_name = full_src_name[len(top_src_dir):] 
                print(src_rel_name)
                slash_pos = src_rel_name.find('/')
                if slash_pos != -1:
                  dst_dir = top_dst_dir + src_rel_name[:slash_pos]
                  # make sure the dst_dir exists, if not, create it
                  print("Creating directory {}".format(dst_dir))
                  # pathlib.Path(dst_dir).mkdir(parents=True, exist_ok=True) 

