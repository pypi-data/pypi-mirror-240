class Filter:
    """
    The filter is used to predistort the sampled signal
    to correct distortions caused by electronic elements
    such as transmission line, low-pass filter, Bias-tee, etc. 
    
    ----------
    Filter design method

    For IIR filter
    Fitting the step response and get the corresponding coefficients;
        RLC: f(x) = A + B * exp(-t/tau);
        Skin effect: f(x) = A + B * erfc(?)
    A, B, and tau;
    Determine a sampling period Ts;
    Construct a inverse IIR filter by bilinear transform;
    
    For FIR filter
    Construct a inverse FIR filter by invert the transfer function matrix;

    ----------
    Parameters
    
    IIR: str 'IIR.csv'
        multiple column csv file [X1, Y1, X2, Y2, ... Xn, Yn]
        for n-IIR filter
        each set of [x, Y] belongs to one filter
        if =None, no IIR filtering
    fs: float
        Sampling frequency, Ts = 1/fs: sampling period
    FIR: str 'FIR.csv'
        if =None, no FIR filtering
    """

    # Ignore the skin effect
    def __init__(self, fs, IIR, FIR) -> None:
        self.fs = fs
        self.IIR = IIR
        self.FIR = FIR
        self.num_IIR_filter = int( len( IIR[0] ) / 2)
    def filtering(self, waveform):
        if self.IIR is not None:
            for i in range(self.num_IIR_filter):
                y = IIR_filtering(self.IIR[i][1], self.IIR[i][3], self.IIR[i][2], waveform)
                waveform[1] = y
        return waveform

def IIR_filtering(b0, b1, a1, waveform):
    y_filtered = []
    for j in range(len(waveform[0])):
        if j == 0:
            y_filtered.append(
                b0 * waveform[1][j]
            )
        else:
            y_filtered.append(
                b0 * waveform[1][j] + b1 * waveform[1][j-1] + a1 * y_filtered[j-1]
            )
    return np.array(y_filtered) ; 

def predistor(waveform,IIR,FIR,srate):
	_filter = Filter(fs=srate, IIR=IIR, FIR=FIR)
	return _filter.filtering(waveform)


def fix(X,Y,irr) : 
    Yp =  np.copy(Y)  ; 
    for F  in  irr : 
        Yp  =  IIR_filtering( F[1] , F[3]  , F[2]   ,  [X , Yp] ) ;  
    return Yp ; 

