#!/usr/bin/python

import sys
from pydub import AudioSegment
from pydub.playback import play

# Load songs into array
soundFilePath="../audio/"
soundFileTemplate=soundFilePath + "{}_{}.mp3"

soundClips = [[0,0,0],[0,0,0]]
for row in [0, 1]:
    for col in [0, 1, 2]:
        soundFile=soundFileTemplate.format(row, col)
        print("Loading " + soundFile)
        soundClips[row][col] = AudioSegment.from_mp3(soundFile)
        


row = int(sys.argv[1])
col = int(sys.argv[2])
#soundFile=soundFilePath + buttonPosition + ".mp3"

print("Playing sound {} {} ".format(row, col))

clip=soundClips[row][col] 
play(clip)
