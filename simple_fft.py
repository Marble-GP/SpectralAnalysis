import numpy as np
import matplotlib.pyplot as plt
import os

def CSV_FFT(fname_in, fname_out, dt, col=0):
    dat = np.loadtxt(fname_in, delimiter=",").T
    v = dat[col]
    fv = np.fft.fft(v)[0:int(len(v)/2)]
    ft_freq = np.fft.fftfreq(len(v), d=dt)[0:int(len(v)/2)]
    fv_amp=np.abs(fv)/len(v)*2.0
    fv_amp[0] /= 2.0
    fv_ph=np.arctan2(np.imag(fv), np.real(fv))

    np.savetxt(fname_out, np.array([ft_freq, fv_amp, fv_ph]).T, delimiter=",")

if __name__ == "__main__":
    fpath = input("CSV file path:")
    dt = 1.0/float(input("sampling frequnecy[Hz]:"))
    n = int(input("column number to FT:"))
    CSV_FFT(fpath, os.path.dirname(fpath)+"\\fft_col={}_".format(n)+os.path.basename(fpath), dt, n)
