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
no_channels=1.0
frequency=44100

print('Length of file is: '+str(float(len(audio[0])/(no_channels*frequency)))+' seconds')

#for i in audio:
#	print(i)

if not os.path.exists(source+"_results"):
    os.makedirs(source+"_results")
if not os.path.exists(source+"_results/audio/bird"):
    os.makedirs(source+"_results/audio/bird")
if not os.path.exists(source+"_results/audio/not_bird"):
    os.makedirs(source+"_results/audio/not_bird")
if not os.path.exists(source+"_results/imgs/bird"):
    os.makedirs(source+"_results/imgs/bird")
if not os.path.exists(source+"_results/imgs/not_bird"):
    os.makedirs(source+"_results/imgs/not_bird")

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

    #spectrogram of sliced file
    plt.figure(1)
    nfft=1024
    fs=256#Sampling frequency
    plt.clf()
    plt.cla()
    Pxx, freqs, bins, im = plt.specgram(fragment[0], nfft, fs, cmap='binary', vmin = 0, vmax = 200)
    plt.savefig(source + '_results/imgs/' + suffix + '_specgram.jpg', dpi=100)
    rows = []
    cols = []
    for i in range(len(Pxx[0])):
        cols.append(sum(Pxx[i]))
    for i in range(len(Pxx[:][0])):
        rows.append(sum(zip(*Pxx)[i]))
    tot = sum(rows)
    plt.clf()
    plt.cla()
    plt.plot(cols)
    plt.savefig(source + '_results/imgs/'+ suffix +'_cols.jpg', dpi=100)
    plt.clf()
    plt.cla()
    plt.plot(rows)
    plt.savefig(source + '_results/imgs/'+ suffix +  '_rows.jpg', dpi=100)
    offset += duration
