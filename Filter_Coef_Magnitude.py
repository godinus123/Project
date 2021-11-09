# #==========================================
# My Class File

import os, sys
os.sys.path.insert(0, sys.path[0]+'.\ClassFiles') # Add class files directory

import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

class Filter_Coef_Magnitude:
    def __init__(self, filter_params):
        self.dir  = "..\Images\_"
        self.logs = "_LogScale"
        self.lins = "_LinerScale"
        self.fcof = "_FilterCoef"
        pass
       
    def filter_ALL(self, filter_params ):
        f_type, fs, cutoff, trans_width, numtaps, band_0, band_1 = filter_params
        if  f_type     == "LPF" :
            f_band     = [0, cutoff, cutoff + trans_width, 0.5*fs]
            f_shape    = [1,0]
            self.Title = "Low-pass Filter"

        elif f_type    == "HPF" :
            f_band     = [0, cutoff - trans_width, cutoff, 0.5*fs]
            f_shape    = [0,1]
            self.Title = "High-pass Filter"

        elif f_type    == "BPF" :
            f_band     = [0, band_0 - trans_width, band_0, band_1, band_1 + trans_width, 0.5*fs]
            print(f_band)
            f_shape    = [0,1,0]
            self.Title = "Band-pass Filter"

        elif f_type    == "BSF" :
            f_band     = [0, band_0 - trans_width, band_0, band_1, band_1 + trans_width, 0.5*fs]
            f_shape    = [1, 0, 1]
            self.Title = "Band-stop Filter"

        self.taps      = signal.remez(numtaps, f_band, f_shape, Hz=fs)
        self.w, self.h = signal.freqz(self.taps, [1], worN=2000)

    def plot_response(self, filter_params):
        f_type, fs, cutoff, trans_width, numtaps, band_0, band_1 = filter_params
        print(filter_params, self.Title)

        "Utility function to plot response functions"
        fig = plt.figure()
        plt.plot(0.5*fs*self.w/np.pi, 20*np.log10(np.abs(self.h)),'r') # w, h self gen
        plt.grid(True)
        plt.xlabel('Frequency (Hz)')
        plt.ylabel('Gain (dB)')
        plt.title( self.Title )
        File_1 = self.dir+f_type+self.logs
        plt.savefig(File_1)

        fig = plt.figure()
        plt.plot(0.5*fs*self.w/np.pi, abs(self.h),'g') # w, h self gen
        plt.grid(True)
        plt.xlabel('Frequency (Hz)')
        plt.ylabel('Linear Scale')
        plt.title( self.Title )
        File_2 = self.dir+f_type+self.lins
        plt.savefig(File_2)

        fig = plt.figure()
        plt.plot(self.taps,'b') # w, h self gen
        plt.grid(True)
        plt.xlabel(f'N of filter Taps : {numtaps}')
        plt.ylabel('Filter Coefficient')
        plt.title( self.Title )
        File_3 = self.dir+f_type+self.fcof
        plt.savefig(File_3)


# Terminal output
# ['LPF', 200, 50, 20, 63, 30, 40] Low-pass Filter
# ['HPF', 200, 50, 20, 63, 30, 40] High-pass Filter
# [0, 10, 30, 40, 60, 100.0]
# ['BPF', 200, 50, 20, 63, 30, 40] Band-pass Filter
# ['BSF', 200, 50, 20, 63, 30, 40] Band-stop Filter


