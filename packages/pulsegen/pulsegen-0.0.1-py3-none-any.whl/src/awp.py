#%%
import numpy as np
from scipy import interpolate
from scipy.linalg import eig
#%%
def eigensolve_close(H):
    '''
    get eigensolution of hamiltonian 'H'.
    '''
    vals, vecs = eig(H)    
    for i in range(len(vecs[:,1])):
        idx=np.append(range(i),(-abs(vecs[i,i:])).argsort()+i) if i>0 else (-abs(vecs[i,i:])).argsort()   
        vecs=vecs[:,idx]
        vals=vals[idx]
    return np.real(vals), vecs.T

def eigensolve_sort(H,ascending = True):
    '''
      get eigensolution of hamiltonian 'H', default ascending order is True.
      The return eigenenergies are in ascending order is ascending is True, else they will be is descending order.
    '''
    vals, vecs = eig(H)    
    if ascending:
        idx = vals.argsort()
    else:
        idx = vals.argsort()[::-1] 
    vals = vals[idx]
    vecs = vecs[:,idx]
    return np.real(vals), vecs.T


def Qtensor(*args):
    if len(args)==0: return args[0]
    v = args[0].data
    for _oper in args[1:]:
        v = np.kron( v, _oper.data)
    return Operator(v)

class Operator():

    def __init__(self,value):
        self._data = np.array(value)

    @property
    def data(self):
        return self._data

    def __repr__(self):
        return "Quantum Operator: \n {}".format( repr(self.data) )

    def dag(self):
        return Operator( np.transpose( np.conjugate( self.data) ) )

    def __add__(self, other):
        if isinstance(other,Operator):
            return Operator(self.data + other.data)
        else:
            raise TypeError("Incompatible Qobj shapes")

    def __sub__(self,other):
        if isinstance(other,Operator):
            return Operator(self.data - other.data)
        else:
            raise TypeError("Incompatible Qobj shapes")

    def __mul__(self, other):
        if isinstance(other,Operator):
            return Operator( np.matmul(self.data, other.data))
        elif isinstance(other,(float,int,complex )):
            return Operator( self.data * other )
        else:
            raise TypeError("Incompatible Qobj shapes")

    def __rmul__(self,other):
        return self.__mul__(other)


class OperCollec():

    def __init__(self,dims=2):
        self.dims=int(dims)

    @property
    def I(self):
        return Operator(np.eye(self.dims,dtype=complex))

    @property
    def destroy(self):
        a = np.zeros([self.dims,self.dims],dtype=complex)
        for i in range(self.dims-1):
            a[i,i+1] = np.sqrt(i+1)+0j
        return Operator(a)

    @property
    def create(self):
        return self.destroy.dag()

    @property
    def a(self):
        return self.destroy

    @property
    def x(self):
        return self.destroy+self.create

    @property
    def y(self):
        return -1j*(self.destroy-self.create)

    @property
    def p(self):
        return self.destroy(2)

    @property
    def m(self):
        return self.destroy(2).dag()

    @property
    def aa(self):
        return self.create*self.destroy

    @property
    def aaaa(self):
        return self.create*self.create*self.destroy*self.destroy

class Transmon():

    def __init__(self, f01_max, f01_min, Ec, Vperiod, Voffset=0, V0=0):
        self.f01_max = f01_max
        self.f01_min = f01_min
        self.Ec = Ec
        self.Vperiod = Vperiod
        self.Voffset = Voffset
        self.V0 = V0

        # Calculate the JJ parameters
    def calculate_JJ(self):
        self.EJS = (self.f01_max + self.Ec)**2 / (8 * self.Ec)
        self.d = (self.f01_min + self.Ec)**2 / (8 * self.EJS * self.Ec)

    def V_to_f(self, V):  # noqa 102
        F = np.pi * (V - self.Voffset) / self.Vperiod
        f = np.sqrt(8 * self.EJS * self.Ec * np.abs(np.cos(F)) *np.sqrt(1 + self.d**2 * np.tan(F)**2)) - self.Ec
        return f

    def f_to_V(self, f):  # noqa 102
        # Make sure frequencies are inside the possible frequency range
        if np.any(f > self.f01_max):
            f[ f > self.f01_max ] = self.f01_max
            # raise ValueError(
            #     'Frequency requested is outside the qubit spectrum')
        if np.any(f < self.f01_min):
            raise ValueError(
                'Frequency requested is outside the qubit spectrum')

        # Calculate the required EJ for the given frequencies
        EJ = (f + self.Ec)**2 / (8 * self.Ec)

        # Calculate the F=pi*(V-voffset)/vperiod corresponding to that EJ
        F = np.arcsin(np.sqrt((EJ**2 / self.EJS**2 - 1) / (self.d**2 - 1)))
        # And finally the voltage
        V = F * self.Vperiod / np.pi + self.Voffset

        # Mirror around Voffset, bounding the qubit to one side of the maxima
        if self.V0 >= self.Voffset:
            V[V < self.Voffset] = 2 * self.Voffset - V[V < self.Voffset]
        else:
            V[V > self.Voffset] = 2 * self.Voffset - V[V > self.Voffset]

        # Mirror beyond 1 period, bounding the qubit to one side of the minima
        Vminp = self.Vperiod / 2 + self.Voffset
        Vminn = -self.Vperiod / 2 + self.Voffset
        V[V > Vminp] = 2 * Vminp - V[V > Vminp]
        V[V < Vminn] = 2 * Vminn - V[V < Vminn]
        return V

    def df_to_dV(self, df):  # noqa 102
        f0 = self.V_to_f(self.V0)
        return self.f_to_V(df + f0) - self.V0

def state_deriv(state_trace,df):
    deriv_list = [ (state_trace[i+1]-state_trace[i-1])/2/df for i in range(1,len(state_trace)-1)] 
    deriv_list.insert(0, (state_trace[1]-state_trace[0])/df )
    deriv_list.append( (state_trace[-1]-state_trace[-2])/df )
    return deriv_list

def get_bare_state_index(H):
    ## be careful using this function, it may fail in degenerate case !!!!
    eigenvalues = eigensolve_close(H)[0]
    sort_idx = np.argsort(eigenvalues)
    return np.argsort(sort_idx)

def smooth_state_trace(state_list):
    last_state = state_list[0] 
    new_state_list = [last_state]
    for i in range(1,len(state_list)):
        if np.linalg.norm(state_list[i] - last_state) >= np.linalg.norm(state_list[i] + last_state):
            last_state = -1* state_list[i]
        else:
            last_state = state_list[i]
        new_state_list.append(last_state)
    return np.array(new_state_list)
    
def floateq(a,b,thr=1e-3):  
	return np.abs(a-b) < thr; 

def rearrangement_eigen_traces_by_ignore_small_gap(ener,estate,gap_threshold,adjcent_trace_num = 4):
    """
    ener1.shape = ( param_len , state_num)
    """
    state_num = len(estate[0])
    for i in range(state_num-1):
        for k in range(1,min( adjcent_trace_num, state_num  - i )):
            swap_two_eigen_trace(ener[:,i],ener[:,i+k],estate[:,i],estate[:,i+k],gap_threshold )

def swap_two_eigen_trace(eigen_ener1,eigen_ener2,eigen_state1,eigen_state2,gap):
    ener_diff = eigen_ener2 - eigen_ener1
    anticross_idx = np.where( ener_diff < gap )[0]
    if len(anticross_idx) == 0 or isinstance(ener_diff,float):
        pass
    else:
        extreme_points  = get_extreme_points(ener_diff,anticross_idx)
        for point in extreme_points:
            eigen_ener1_temp = eigen_ener1.copy()
            eigen_state1_temp = eigen_state1.copy()
            eigen_ener1[point:] = eigen_ener2[point:]
            eigen_ener2[point:] = eigen_ener1_temp[point:]
            eigen_state1[point:] = eigen_state2[point:]
            eigen_state2[point:] = eigen_state1_temp[point:]

def get_extreme_points(ener_diff,anticross_idx):
    start_idxs = [anticross_idx[0]]
    end_idxs = []
    for idx_count,idx in enumerate(anticross_idx):
        if idx+1 in anticross_idx:
            continue
        else:
            end_idxs.append(idx)
            if idx_count != len(anticross_idx)-1:
                start_idxs.append(anticross_idx[idx_count+1])
    extreme_points = []
    for i in range(len(start_idxs)):
        if start_idxs[i] == end_idxs[i]:
            extreme_points.append(start_idxs[i])
        else:
            extreme_points.append( np.argmin(ener_diff[start_idxs[i]:end_idxs[i]])+start_idxs[i] )    
    return extreme_points

def isNone(v):
    return type(v) ==  type(None)

class AWP:
    
    def __init__(self,dims=3):

        self.min_C=4.5e9     # minimum value in calculating the adiabaticity factor
        self.max_C=8.0e9    # maximum value in calculating the adiabaticity factor
        self.down_tuning = True

        self.f_Terms = 1
        self.lcoeff = np.array([1.2])
        self.dfdV = 1e9
        self.negative_amplitude = False
        self.up_limit=None    # set uplimit of pulse value, prevent outliers
        self.down_limit=None  # set downlimit of pulse value

        self.constant_coupling = False 
        self.spectro = None

        self.q1_freq = 6.0e9
        self.cplr_idle_freq = 8e9
        self.q2_freq = 5.4e9
        ## if not constant_coupling, use r1c r2c
        self.g1c = 100e6 
        self.g2c = 100e6
        self.g12 = 12e6
        self.r1c = 0.016
        self.r2c = 0.016
        self.r12 = 0.001
        self.anhar_Q1 = -250e6
        self.anhar_Q2 = -250e6
        self.anhar_CPLR = -300e6
        
        self.gap_threshold = 0  # ignore small gaps between eigentraces
        self.pulsepoints = 301  # Number of points in integrating f(t)
        self.freqpoints = 301   # Number of points in calculating the adiabaticity factor

        self.dims  = 3
        self.adia_factor_key_list = ['min_C','max_C','down_tuning','constant_coupling','gap_threshold','freqpoints',
                                    'q1_freq','q2_freq','cplr_idle_freq','g1c','g2c','g12','r1c','r2c','r12','anhar_Q1','anhar_Q2','anhar_CPLR']

        # self.calculate_adia_factor_spline()

    def update_params(self,pdict={}):
        adia_factor_modified = False
        for key,v in pdict.items():
            if key in self.adia_factor_key_list:
                if isinstance(v,(int,float,complex)):
                    if floateq(self.__getattribute__(key),v,1e-5):
                        continue
                    else:
                        self.__setattr__(key,v)
                        # print('changed_key',key,'changed_value:',v)
                        adia_factor_modified = True
                else:
                    raise ValueError('value {} of key {} should be int/float/complex'.format(v,key))
            elif key == 'spectro':
                if v:
                    if isNone(self.spectro):
                        # f01_max, f01_min, Ec, Vperiod, Voffset, V0
                        self.spectro = Transmon(v['f01_max'],v['f01_min'],v['Ec'],v['Vperiod'],v['Voffset'],0)
                    for spec_key,spec_v in v.items():
                        if spec_key in ['f01_max','f01_min', 'Ec', 'Vperiod', 'Voffset', 'V0']:
                            if not floateq(spec_v,self.spectro.__getattribute__(spec_key),1e-6):
                                self.spectro.__setattr__(spec_key,spec_v)
                    self.spectro.calculate_JJ()
            else:
                self.__setattr__(key,v)

        if adia_factor_modified:
            self.calculate_adia_factor_spline() 

    def calculate_envelope(self,t0,t,width,plateau,lcoeff):
        if isinstance(lcoeff,(int,float)):
            self.f_Terms = 1
            self.lcoeff=  lcoeff
        else:
            self.f_Terms = len(lcoeff)
            self.lcoeff = np.array(lcoeff)
        
        self.calculate_f_t_sinosoidal(width)

        dfreq = np.zeros_like(t) 
        x1 = ( abs(t - t0) <= plateau/2 + width/2)   
        x2 = ( abs(t - t0) < plateau/2 )
        x3 = ( abs(t - t0) > plateau/2 + width/2 )

        dfreq[x1] = interpolate.splev( (width/2+abs(t[x1]-t0)-plateau/2)/width,self.ft_spline ) - self.cplr_idle_freq
        dfreq[x2] = interpolate.splev( 0.5 ,self.ft_spline ) - self.cplr_idle_freq
        dfreq[x3] = 0

        if self.spectro is None:
            # Use linear dependence if no qubit was given
            # log.info('---> df (linear): ' +str(df))
            values = -1*dfreq / self.dfdV
            print("transmon spectro is not used")
        else:
            values = self.spectro.df_to_dV(dfreq)

        if self.negative_amplitude:
            values = values*-1

        if self.up_limit:
            values[values>self.up_limit]=self.up_limit
        if self.down_limit:
            values[values<self.down_limit]=self.down_limit

        return values

    def calculate_f_t_sinosoidal(self,width):
        n = np.arange(1, self.f_Terms + 1, 1)
        n_points = self.pulsepoints  # Number of points in the numerical integration
        self.t_arr = np.linspace(0, 1, n_points)
        self.dt = (self.t_arr[1]-self.t_arr[0])*width
        
        f_t0=self.cplr_idle_freq
        f_t_arr = np.array([f_t0])
        for i in range( int((n_points-1)/2) ):
            df_dt = -1*np.sum( self.lcoeff*( np.sin(2*np.pi*n*self.t_arr[i])) ) / interpolate.splev(f_t0,self.adia_spline)  
            f_t0 += df_dt * self.dt
            f_t_arr =np.append( f_t_arr, f_t0 )
        self.f_t_arr = np.append(f_t_arr,f_t_arr[-2::-1])

        self.ft_spline = interpolate.splrep(self.t_arr,self.f_t_arr,k=3)

    def get_Hamiltonian(self,fc):
        if not self.constant_coupling:
            g1c = self.r1c*np.sqrt(self.q1_freq*fc)
            g2c = self.r2c*np.sqrt(self.q2_freq*fc)
            g12 = self.r12*np.sqrt(self.q2_freq*self.q1_freq)
        else:
            g1c = self.g1c
            g2c = self.g2c
            g12 = self.g12
        fq1 = self.q1_freq
        fq2 = self.q2_freq
        anhar1 = self.anhar_Q1
        anharc = self.anhar_CPLR
        anhar2 = self.anhar_Q2
        H_q1 =Qtensor( fq1 * self.Opers.aa + 0.5 * anhar1 * self.Opers.aaaa, self.Opers.I,self.Opers.I)
        H_q2 =Qtensor(  self.Opers.I, self.Opers.I, fq2 * self.Opers.aa + 0.5 * anhar1 * self.Opers.aaaa)
        H_qc =Qtensor( self.Opers.I, fc * self.Opers.aa + 0.5 * anharc * self.Opers.aaaa,self.Opers.I)
        H_g1c = g1c * Qtensor(self.Opers.x, self.Opers.x, self.Opers.I)
        H_g2c = g2c * Qtensor(self.Opers.I, self.Opers.x, self.Opers.x)
        H_g12 = g12 * Qtensor(self.Opers.x, self.Opers.I, self.Opers.x)
        return (H_q1 + H_q2 + H_qc + H_g12 + H_g1c + H_g2c).data

    def calculate_adia_factor_spline(self):
        print('update diabatic factor')
        if self.down_tuning:
            self.fc_arr = np.linspace(self.min_C,self.cplr_idle_freq+1e6,self.freqpoints)[::-1]
        else:
            self.fc_arr = np.linspace(self.cplr_idle_freq-1e6,self.max_C,self.freqpoints)
        df = self.fc_arr[1]-self.fc_arr[0]
        
        self.Opers = OperCollec(self.dims)
        barestate_idx = get_bare_state_index(self.get_Hamiltonian(self.fc_arr[0]))

        ener_trace = []
        estate_trace = []
        for fc in self.fc_arr:
            eigen_eners,eigen_states = self.get_eigen(fc,barestate_idx)
            ener_trace.append(eigen_eners)
            estate_trace.append(eigen_states)
        ener_trace = np.array(ener_trace)
        estate_trace = np.array(estate_trace)

        if not floateq(self.gap_threshold,0,thr=1):
            rearrangement_eigen_traces_by_ignore_small_gap(ener_trace,estate_trace,self.gap_threshold,3) 

        # 001,010,100,011,101,110,002,020,200
        qcq_relevent_sidx = [1,3,9,4,10,12,2,6,18]
        ener_trace_sub9 = ener_trace[:,qcq_relevent_sidx].T
        estate_trace_sub9 = estate_trace[:,qcq_relevent_sidx].swapaxes(0,1)

        self.adia_factor_sum = 0
        self.adia_factor_sum += np.abs( self.get_adia_factor( estate_trace_sub9[0],estate_trace_sub9[1],ener_trace_sub9[0],ener_trace_sub9[1],df) )
        self.adia_factor_sum += np.abs( self.get_adia_factor( estate_trace_sub9[0],estate_trace_sub9[2],ener_trace_sub9[0],ener_trace_sub9[2],df) )
        self.adia_factor_sum += np.abs( self.get_adia_factor( estate_trace_sub9[1],estate_trace_sub9[2],ener_trace_sub9[1],ener_trace_sub9[2],df) )

        for kk in range(3,9):
            if kk !=4:
                self.adia_factor_sum += np.abs(self.get_adia_factor( estate_trace_sub9[4],estate_trace_sub9[kk],ener_trace_sub9[4],ener_trace_sub9[kk],df))

        if self.down_tuning:
            self.adia_spline = interpolate.splrep(self.fc_arr[::-1],self.adia_factor_sum[::-1],k=3)
        else:
            self.adia_spline = interpolate.splrep(self.fc_arr,self.adia_factor_sum,k=3)

    def get_adia_factor(self,alpha,beta,E_alpha,E_beta,df):
        alpha_deriv = state_deriv( smooth_state_trace(alpha),df )
        beta_smooth = smooth_state_trace(beta)
        return np.array([ np.dot(beta_smooth[i].T.conj(),alpha_deriv[i])/(E_alpha[i]-E_beta[i]) for i in range(len(alpha_deriv))])

    def get_eigen(self,fc,sort_idx=None):  
        eigen_eners,eigen_states = eigensolve_sort( self.get_Hamiltonian(fc) )
        if isNone(sort_idx):
            return eigen_eners,eigen_states
        else:
            return eigen_eners[sort_idx],eigen_states[sort_idx]



#%%

import matplotlib.pyplot as plt
if __name__=="__main__":

    awp = AWP()
    pulse = awp.calculate_envelope(0,np.linspace(-40e-9,40e-9,81))
    plt.plot(pulse)




# %%
