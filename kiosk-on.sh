#!/bin/bash

# switch to the graphical virtual console
sudo chvt 7

# set the display
export DISPLAY=:0.0

# screen blanking stuff
xset s noblank
xset s off
xset -dpms

# unclutter package hides mouse 
# these options hide it after 0.5 sec, and even if over root background

# sudo apt-get install unclutter
unclutter -idle 0.5 -root &

chromium-browser --kiosk --noerrdialogs --no-first-run --disable-infobars /home/pi/cds-pi-frame/canvas.html
