#!/usr/bin/python

import sys
from pydub import AudioSegment
from pydub.playback import play

soundFilePath="../audio/"

buttonPosition = sys.argv[1] + "_" + sys.argv[2]
soundFile=soundFilePath + buttonPosition + ".mp3"
print("Playing sound " + soundFile)

song = AudioSegment.from_mp3(soundFile)
play(song)
