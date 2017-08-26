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

print(audio)

print(len(audio[0]))

#convert to length
no_channels=1.0
frequency=44100

print('Length of file is: '+str(float(len(audio[0])/(no_channels*frequency)))+' seconds')

#for i in audio:
#	print(i)

if not os.path.exists(source+"_results"):
    os.makedirs(source+"_results")
if not os.path.exists(source+"_results/audio"):
    os.makedirs(source+"_results/audio")
if not os.path.exists(source+"_results/imgs"):
    os.makedirs(source+"_results/imgs")

duration = 1 #Half a second
offset = 0;
#attempting to slice
while(offset + duration < float(len(audio[0])/(no_channels*frequency))):

    suffix = str(offset) + "-" + str(offset + duration)
    wav_file = open(source + "_results/audio/audio_"+ suffix + ".wav", 'w')
    wavy.slice_wave(source, wav_file, offset, duration) #input file, output file, start in seconds, duration in seconds
    wav_file.close()
    #print("Segment: " + suffix)
    fragment = wavy.get_audio(source + "_results/audio/audio_"+ suffix + ".wav")
#Vmin/max
    #spectrogram of sliced file
    plt.figure(1)
    nfft=1024
    fs=256#Sampling frequency
    Pxx, freqs, bins, im = plt.specgram(fragment[0], nfft, fs, cmap='gray')
    #for i in range(len(Pxx[0][:]))
    #    someArray[i] = sum(Pxx[0][i])
    plt.colorbar()
    plt.savefig(source + '_results/imgs/' + source + '_specgram_' + suffix + '.jpg', dpi=100)
    #plt.plot(i, someArray[i])
    #plt.savefig(source + '_results/imgs/' + source + '_specgram_' + suffix + '.jpg', dpi=100)
    offset += duration
