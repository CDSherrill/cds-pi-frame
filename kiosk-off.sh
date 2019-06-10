#!/bin/bash


# switch to the graphical virtual console
sudo chvt 7

# set the display
export DISPLAY=:0.0

# not sure why it only works if I chop off the last letter
pkill chromium-browse

# screen blanking stuff
# blank time 5 seconds
xset dpms 5 5 5

# unclutter package hides mouse 
# these options hide it after 0.5 sec, and even if over root background

