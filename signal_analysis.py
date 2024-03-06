import numpy as np
import matplotlib.pyplot as plt

def generate_signal(fm = 10, a = 1, fs = 500, pd = 0, dur = 1):
    '''
    Generates a sinusoid, with
    fm: frequency of the sinusoid (hz)
    a: the magnitude of the sinusoid, or radius of the pole.
    fs: samling rate (samples/s)
    pd: phase delay in radians.     
    dur: duration of the sinusoid (s)
    '''
    if fm > 50:
        print("Error: Provide a value <= 50")
        return
    num_samples = dur * fs
    n = np.arange(0,num_samples,1)
    xc = (a**n)*(np.cos(2*np.pi*n*(fm/fs) + pd))
    xs = (a**n)*(np.sin(2*np.pi*n*(fm/fs) + pd))
    
    return xc, xs

def dft_basic(x, num_bins = 6, max_freq = 25, fs = 500, plotting = True):
    '''
    x: input signal
    num_bins: the number of bins in the dft
    max_freq: maximum frequency considered
    '''
    dft_c = np.zeros((max_freq+1,))
    dft_s = np.zeros((max_freq+1,))
    
    # Computing dot products
    for f in np.linspace(0, max_freq, num_bins):
        f  = int(f)
        xc, xs = generate_signal(fm = f)
        dft_c[f] = np.dot(x, xc)
        dft_s[f] = np.dot(x, xs)
    
    # max_val = np.max((np.max(dft_c), np.max(dft_s), 1))
    max_val = len(x)
    
    # PLOTTING
    if plotting == True:
        fig, axs = plt.subplots(2, 1)
        fig.set_figwidth(10)
        axs[0].stem(dft_c)
        axs[0].title.set_text('Cosine Component')
        axs[0].set_xlim(0,max_freq)
        axs[0].set_ylim(0,max_val)
        axs[1].stem(dft_s)
        axs[1].title.set_text('Sine Component')
        axs[1].set_xlim(0,max_freq)
        axs[1].set_ylim(0,max_val)
        plt.show()
        
    return dft_c, dft_s

def cs_basic(x, r=1, num_bins = 6, max_freq = 25, fs = 500, plotting = True):
    '''
    Compute the chirp spectrum.
    x: input signal
    r: radius of computation. 
    num_bins: number of dft bins
    max_frequency: maximum frequency upto which the dft has to be computed
    fs: sampling rate
    '''
    num_samples = np.shape(x)[0]
    mag_xz = np.zeros((max_freq+1,))
    phase_xz = np.zeros((max_freq+1,))
    dft_bins = np.linspace(0, max_freq, num_bins)
    n = np.arange(0,num_samples,1)
    
    for f in dft_bins:
        f = int(f)
        w = 2*np.pi*(f/fs)
        bf = np.multiply((1/r**n), np.exp(-1j*w*n))
        xz = np.dot(x, bf)
        mag_xz[f] = np.abs(xz)
        phase_xz[f] = np.angle(xz)
        if mag_xz[f] < 1e-12:
            mag_xz[f] = 0
        if np.abs(phase_xz[f]) < 1e-12:
            phase_xz[f] = 0
        if mag_xz[f] < 1e-12:
            phase_xz[f] = 0
    
    # PLOTTING
    if plotting == True:
        fig, axs = plt.subplots(2, 1)
        fig.set_figwidth(10)
        axs[0].stem(mag_xz)
        axs[0].title.set_text('Magnitude Spectrum')
        axs[0].set_xlim(0,max_freq)
        # axs[0].set_ylim(0,max_val)
        axs[1].stem(phase_xz)
        axs[1].title.set_text('Phase Spectrum')
        axs[1].set_xlim(0,max_freq)
        # axs[1].set_ylim(0,max_val)
        plt.show()

    return mag_xz, phase_xz