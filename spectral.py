import numpy as np
import matplotlib.pyplot as plt
import os

#cos format
def SpectralTransform(dt, v, f0):
    freq=np.fft.fftfreq(len(v), d=dt)
    fv=np.fft.fft(v)
    fv_amp=np.abs(fv)/len(v)*2.0
    fv_amp[0] /= 2.0
    fv_ph=np.arctan2(np.imag(fv), np.real(fv))
    components=np.arange(int(np.max(freq)/f0))
    comp_freq=np.zeros(int(np.max(freq)/f0))
    comp_amp=np.zeros(int(np.max(freq)/f0))
    comp_ph=np.zeros(int(np.max(freq)/f0))
    for i in components:
        comp_freq[i]=freq[(np.abs(freq-i*f0)).argmin()]
        comp_amp[i]=fv_amp[(np.abs(freq-i*f0)).argmin()]
        comp_ph[i]=fv_ph[(np.abs(freq-i*f0)).argmin()]
    
    return (components, comp_freq, comp_amp, comp_ph)

def CSV_Spectral(fname_in, fname_out, f0, fs, col):
    dat = np.loadtxt(fname_in, delimiter=",").T
    dt = 1.0/fs
    v = dat[col]
    c,f,a,p = SpectralTransform(dt,v,f0)
    np.savetxt(fname_out, np.array([c,f,a,p*180.0/np.pi]).T, delimiter=",")


if __name__ == "__main__":
    fpath = input("CSV file path:")
    fs = float(input("Sampling frequency[Hz] :"))
    f0 = float(input("Fundamental frequency[Hz] :"))
    col  = int(input("column number to FT :"))
    dat = np.loadtxt(fpath, delimiter=",").T
    n = len(dat)
    CSV_Spectral(fpath, os.path.dirname(fpath)+"\\freqcomp_col="+f"{col}_"+os.path.basename(fpath), f0, fs, col)


