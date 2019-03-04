#!/usr/bin/python

# Usage: resize-pic.py original.img max-width max-height new.img
# 
# This script resizes a file to fit a chosen max width and max height.
#
# I'm really just wrapping an imagemagick command (requires imeagemagick)
# 
# C. David Sherrill
# March 2019
#

import sys
import os

args = sys.argv

# get rid of the name of this script as an arg
args.pop(0)
argc = len(args)

# check number of arguments
if (argc != 4):
  sys.exit("Usage: resize-pic.py original.img max-width max-height new.img")

# get the arguments
infilename  = args.pop(0)
max_width   = args.pop(0)
max_height  = args.pop(0)
outfilename = args.pop(0)

if (infilename == outfilename):
  sys.exit("Error: Input and output file are same")

#print("Converting file {:} to size {:}x{:} in new file {:}".format(infilename, max_width, max_height, outfilename))

command = "convert {:} -auto-orient -resize {:}x{:} {:}".format(infilename, max_width, max_height, outfilename)

#print(command)
os.system(command)
 
