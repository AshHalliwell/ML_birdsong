import os, wave
import numpy as np
import datetime
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
#from pylab import figure, specgram, savefig, imshow
import wavy
import sys

#source="stitchbird-song.wav"
source=sys.argv[1]
audio=wavy.get_audio(source)

print audio

print(len(audio[0]))

#convert to length
no_channels=2.0
frequency=44100

print('Length of file is: '+str(float(len(audio[0])/(no_channels*frequency)))+' seconds')

#for i in audio:
#	print(i)

duration = 0.5 #Half a second
offset = 0;
end_length = 122.5 #wavy.slice_wave stops working after this point ¯\_(ツ)_/¯
#attempting to slice
while(end_length < float(len(audio[0])/(no_channels*frequency))):
    suffix = str(offset) + "-" + str(offset + duration)
    wav_file = open("audio/stitchout"+ suffix + ".wav", 'w')
    wavy.slice_wave(source, wav_file, offset, duration) #input file, output file, start in seconds, duration in seconds
    wav_file.close()
    #print("Segment: " + suffix)
    fragment = wavy.get_audio("audio/stitchout"+ suffix + ".wav")

    #spectrogram of sliced file
    plt.figure(1)
    nfft=1024
    fs=256
    #Pxx, freqs, bins, im = plt.specgram(audio[0], nfft, fs)
    #plt.savefig('imgs/stitch_specgram' + suffix + '.jpg', dpi=100)
    offset += duration
