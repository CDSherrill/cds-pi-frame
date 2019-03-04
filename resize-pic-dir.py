#!/usr/bin/python3.5

# Resize all the pictures in a directory, calling
# resize-pic.py to do each pic
#
# C. David Sherrill, March 2019
#

import os
import pathlib

# max width and height of downsized pics
max_width = 788
max_height = 458

# top-level dir to find the source pics...include trailing slash
top_src_dir = '/mnt/photo/'
# look in these subdirectories of top_src_dir
src_subdirs = ['2017', '2016']

# top-level dir to put the resized pics
top_dst_dir = '/home/pi/photo/'

# filename must end in one of these suffixes
suffixes = ['.jpg', '.JPG', '.gif', '.GIF', '.png', '.PNG']

# exclude any file that has these substrings
excludes = ['thumb', 'THUMB', '@eaDir']

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
                # print(src_rel_name)
                slash_pos = src_rel_name.rfind('/')
                if slash_pos != -1:
                    dst_dir = top_dst_dir + src_rel_name[:slash_pos]
                    src_fname = src_rel_name[slash_pos:]
                    # make sure the dst_dir exists, if not, create it
                    if not os.path.isdir(dst_dir):
                        print("Creating directory {}".format(dst_dir))
                        pathlib.Path(dst_dir).mkdir(parents=True,exist_ok=True) 
                    full_dst_name = dst_dir + src_fname
                else:
                    full_dst_name = top_dst_dir + src_rel_name
                if os.path.exists(full_dst_name):
                  continue
                print("{} -> \n  {}".format(full_src_name, full_dst_name))
                command = "./resize-pic.py {} {} {} {}".format(full_src_name, max_width, max_height, full_dst_name)
                # print("command is {}".format(command))
                os.system(command)

