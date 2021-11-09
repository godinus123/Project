# #==========================================
# My Class File
import os, sys
os.sys.path.insert(0, sys.path[0]+'.\ClassFiles') # Add class files directory

import Filter_Coef_Magnitude

import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

def main():
    # Program Init.
    plt.close('all')
    clear = lambda: os.system('cls')
    clear()

    f_type = "LPF"
    fs=100
    cutoff=50
    trans_width=20
    numtaps=63
    band_0 = 30
    band_1 = 40

    filter_params = [f_type, 2*fs, cutoff, trans_width, numtaps, band_0, band_1]
    filter_coef_mag = Filter_Coef_Magnitude.Filter_Coef_Magnitude ( filter_params )

    #===== LPF case
    filter_coef_mag.filter_ALL   ( filter_params )
    filter_coef_mag.plot_response( filter_params )

    #===== HPF case
    f_type = "HPF"
    filter_params = [f_type, 2*fs, cutoff, trans_width, numtaps, band_0, band_1]
    filter_coef_mag.filter_ALL   ( filter_params )
    filter_coef_mag.plot_response( filter_params )

    #===== BPF case
    f_type = "BPF"
    filter_params = [f_type, 2*fs, cutoff, trans_width, numtaps, band_0, band_1]
    filter_coef_mag.filter_ALL   ( filter_params )
    filter_coef_mag.plot_response( filter_params )

    #===== BSF case
    f_type = "BSF"
    filter_params = [f_type, 2*fs, cutoff, trans_width, numtaps, band_0, band_1]
    filter_coef_mag.filter_ALL   ( filter_params )
    filter_coef_mag.plot_response( filter_params )

    plt.show()

main()

