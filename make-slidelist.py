#!/usr/bin/python

# this little script creates a list of filenames for pictures we want
# in the slideshow
#
# C. David Sherrill, March 2018
#

import os

# do all searching inside this top level dir
top_dir = '/home/pi/photo/'
# look in these subdirectories of top_dir
# subdirs = ['2017', '2016', '2015', '2014']
subdirs = ['DragonCon2016', 'Uppsala2016']
# filename must end in one of these suffixes
suffixes = ['.jpg', '.JPG', '.gif', '.GIF', '.png', '.PNG']
# exclude any file that has these substrings
excludes = ['thumb', 'THUMB', '@eaDir']
# file_list holds the final list of files (full paths)
file_list = []

for subdir in subdirs:
    dirname = top_dir + subdir;
    for root, dirs, files in os.walk(dirname):
        for file in files: 
            if any(exclude in file for exclude in excludes):
                continue
            if any(file.endswith(suffix) for suffix in suffixes):
                file_list.append(os.path.join(root, file))

outfile = open('slidelist.js', 'w')
outfile.write('Slides = [\n');
for counter, file in enumerate(file_list):
    if counter:
        outfile.write(",\n")
    outfile.write("'" + file + "'")
outfile.write("]\n")
outfile.close()
print file_list

