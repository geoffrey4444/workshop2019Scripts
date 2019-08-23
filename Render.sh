#!/bin/bash
/home/geoffrey/Codes/x264ffmpeg/ffmpeg/bin/ffmpeg-4.2-amd64-static/ffmpeg -framerate 30 -i RingdownFrame.%04d.png -pix_fmt yuv420p -codec:v libx264 Ringdown.mp4
/home/geoffrey/Codes/x264ffmpeg/ffmpeg/bin/ffmpeg-4.2-amd64-static/ffmpeg -framerate 30 -i PlungeFrame.%04d.png -pix_fmt yuv420p -codec:v libx264 Plunge.mp4
cp /home/workshopStudents2019/scripts/mylist.txt .
/home/geoffrey/Codes/x264ffmpeg/ffmpeg/bin/ffmpeg-4.2-amd64-static/ffmpeg -f concat -i mylist.txt -c copy BBH.mp4
