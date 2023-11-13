#!/usr/bin/env python3

import cmath
import numpy as np
import scipy.signal as signal


class Filter:
    r"""Filter signal with an IIR filters and a FIR filter.
    
    The IIR filter is constucted from continous time transfer function in
    zero-pole-gain form.

    Parameters
    ----------
    fs : float
        Sample rate
    z : array_like
    p : array_like
    k : float
        zeros, poles and gain of the IIR filter
    F : array_like, optional
        Coefficients for FIR filter
    gain : :obj:`float`, optional
    offset : :obj:`float`, optional
        Gain and offset of input signal. The signal actually input to filter is
        `(data-offset)/gain`
    """
    F = None
    gain = 1
    offset = 0
    
    def __init__(self, fs, z, p, k, F=None, gain=1, offset=0):
        self.fs = fs
        self.z = np.array(z)
        self.p = np.array(p)
        self.k = k
        if F is not None:
            self.F = np.array(F, dtype='f8')
        self.gain = gain
        self.offset = offset
        self._cache_sos()
        
    def _cache_sos(self):
        """Converts continuous time zpk filter to discrete time sos filter."""
        z = self.z
        p = self.p
        k = self.k
        self._sos = signal.zpk2sos(*signal.bilinear_zpk(z, p, k, self.fs))
        
    def lfilter(self, data):
        """Applys filter to data.
        
        Parameters
        ----------
        data:array_like
            Waveform to apply filter
        
        Returns
        -------
        waveform: ndarray
            Filtered waveform
        """
        data = (data-self.offset)/self.gain
        data = signal.sosfilt(self._sos, data)
        if self.F is not None:
            data = signal.lfilter(self.F, [1.], data)
        return data
    
    def get_response_time(self):
        p = self.p
        p = p[p!=0]
        return 6 * (1/np.abs(p)).max()
    
    def __repr__(self):
        return (
            f'Filter(fs={self.fs}, z={self.z!r}, p={self.p!r}, k={self.k}, '
            f'F={self.F!r}, gain={self.gain}, offset={self.offset})'
        )


def _convert_parameters_to_list(iir_1st, iir_2nd):
	"""Extracts IIR filter parameters from dict."""
	zeros = []
	poles = []
	# First order, zero z<0
	for v1 in iir_1st:
		tauB = v1['tau']
		B = v1['scale']
		if tauB > 0:
			zeros.append(-1/tauB/(1+B))
			poles.append(-1/tauB)
	# Second order
	for v2 in iir_2nd:
		tauA = v2['tau']
		A = v2['scale']
		T = v2['period']
		phi =  v2['phi']
		if tauA > 0:
			poles.extend([-1/tauA-2j*np.pi/T, -1/tauA+2j*np.pi/T])
			# solve for zeros
			a = 1 + A*np.cos(phi)
			b = (1+a)/tauA - 2*np.pi*A*np.sin(phi)/T
			c = 1/tauA**2 + (2*np.pi/T)**2
			d = cmath.sqrt(b**2 - 4*a*c)
			zeros.extend([(-b-d)/(2*a), (-b+d)/(2*a)])
	return zeros, poles

def get_invfilter_by_parameters(iir_1st,iir_2nd, fs):
	"""Construct inverse IIR filter from dict."""
	z, p = _convert_parameters_to_list(iir_1st, iir_2nd)
	k = np.real(np.prod(p) / np.prod(z))
	F = None
	# exchange zeros and poles to get inverse filter
	return Filter(fs, p, z, 1/k, F)

def predistor(waveform,iir_1st,iir_2nd,srate=2e9):
	_filter = get_invfilter_by_parameters(iir_1st,iir_2nd, srate)
	return _filter.lfilter(waveform)



def convolve_ringback(waveform,delay,width,amp,srate=2e9):
    ht = np.zeros(  int(50e-9*srate) )
    ht[0]=1
    t = np.linspace(0,50e-9,len(ht),endpoint=False)
    ht += amp/(0.25*srate*width)  * np.sin(2*np.pi * (t -delay)/ width  )  * ( np.abs( t -delay ) <= width/2 )
    return signal.convolve(waveform,ht)[0:len(waveform)]