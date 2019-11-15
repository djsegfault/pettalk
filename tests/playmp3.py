#!/usr/bin/python

import sys
from pydub import AudioSegment
from pydub.playback import play

import os.path
from os import path
import sys

# Load songs into array
soundFilePath="../audio/"
soundFileTemplate=soundFilePath + "{}_{}.mp3"
rows = 2
cols = 3

soundClips = [] 
for row in range(rows):
    soundClips.append([])
    for col in range(cols):
       soundFile=soundFileTemplate.format(row, col)
       if path.exists(soundFile):
           print("Loading " + soundFile)
           soundClips[row].append(AudioSegment.from_mp3(soundFile))
       else:
           print("WARNING: {} is missing!".format(soundFile))
           soundClips[row].append(None)
        
row = int(sys.argv[1])
col = int(sys.argv[2])
if row < 0 or row >= rows or col < 0 or col >= cols:
    print("Invalid row or column")
    sys.exit(1)

clip=soundClips[row][col]
if clip != None:
    print("Playing clip {} {} ".format(row, col))
    play(clip)
else:
    print("Skipping missing clip {} {} ".format(row, col))


