#!/usr/bin/python

# Usage: resize-pic.py original.img max-width max-height new.img
# 
# This script resizes a file to fit a chosen max width and max height.
# Automatically reorients image using EXIF info
# 
# Requires Pyton package wand (pip install Wand)
# Requires package libmagickwand-dev (apt-get install libmagickwand-dev)
#
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
if (argc != 7):
  sys.exit("Usage: resize-pic.py original.img max-width max-height pixel-ratio top-crop-pct bottom-crop-pct new.img")

# get the arguments
infilename  = args.pop(0)
max_width   = int(args.pop(0))
max_height  = int(args.pop(0))
pixel_ratio = float(args.pop(0)) # pixel width to height for device
top_crop_frac = float(args.pop(0)) / 100.0
bottom_crop_frac = float(args.pop(0)) / 100.0
outfilename = args.pop(0)

if (infilename == outfilename):
  sys.exit("Error: Input and output file are same")

#print("Converting file {:} to size {:}x{:} in new file {:}".format(infilename, max_width, max_height, outfilename))

#command = "convert {:} -auto-orient -resize {:}x{:} {:}".format(infilename, max_width, max_height, outfilename)
#print(command)
#os.system(command)

from wand.image import Image

with Image(filename = infilename) as src_img:
    src_width = src_img.width
    src_height = src_img.height
    print("Original dimensions {}x{}".format(src_width, src_height))
    src_img.auto_orient() 
    src_width = src_img.width
    src_height = src_img.height
    print("Reoriented dimensions {}x{}".format(src_width, src_height))
    
    ### if the pic is wider than tall: ###

    # scale down so that the width fits the max width
    if (src_width > src_height):
        dst_width = max_width
        scale = float(dst_width)/float(src_width)
        dst_height = int(src_height*scale/pixel_ratio)

        # if downscaled height fits within max_height, rescale and save
        if (dst_height <= max_height):
            src_img.resize(dst_width,dst_height)
            print("Resized to {}x{}".format(dst_width,dst_height))

        # if downscaled height plus allowed crop fits, then do that
        elif ((dst_height - max_height) < ((top_crop_frac + bottom_crop_frac)*dst_height)):
            src_img.resize(dst_width,dst_height)
            top_crop = int(top_crop_frac * dst_height)
            bottom_crop = int(bottom_crop_frac * dst_height)
            bottom_crop = dst_height - max_height - top_crop
            cropped = src_img[:,top_crop:(dst_height-bottom_crop)]
            # cropped.resize(dst_width,dst_height)
            print("Cropping off {} at top and {} at bottom".format(top_crop, bottom_crop))
            cropped.save(filename=outfilename)

        # our downscaled and cropped image is still too tall, so shrink it
        # a bit more in the width dimension
        else:
            # crop original image first by allowed amounts
            top_crop = int(top_crop_frac * src_height)
            bottom_crop = int(bottom_crop_frac * src_height)
            cropped = src_img[:,top_crop:(src_height - bottom_crop)]
            # now rescale it to fit height
            src_height = cropped.height
            dst_height = max_height
            scale = float(dst_height)/float(src_height)
            dst_width = int(src_width*scale*pixel_ratio)
            src_img.resize(dst_width,dst_height)
            print("After crop resized to {}x{}".format(dst_width,dst_height))
            src_img.save(filename=outfilename)
        
    # if the pic is taller than wide:
    # scale so that the height fits the max height
    else:
        top_crop = int(src_height * top_crop_frac)
        bottom_crop = int(src_height * bottom_crop_frac)
        cropped = src_img[:,top_crop:(src_height-bottom_crop)]
        dst_height = max_height
        scale = float(dst_height)/float(cropped.height)
        dst_width = int(src_width*scale*pixel_ratio)
        cropped.resize(dst_width,dst_height)
        cropped.save(filename=outfilename)

