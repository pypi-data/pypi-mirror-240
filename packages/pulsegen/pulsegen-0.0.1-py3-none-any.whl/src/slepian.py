#%%
import numpy as np
#%%
def floateq(a,b,thr=1e-3):  
  return np.abs(a-b) < thr; 

def isNone(v):
    return type(v) ==  type(None)

class Transmon():

    def __init__(self, f01_max, f01_min, Ec, Vperiod, Voffset=0):
        self.f01_max = f01_max
        self.f01_min = f01_min
        self.Ec = Ec
        self.Vperiod = Vperiod
        self.Voffset = Voffset
        self.V0 = 0

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

class Slepian():
    def __init__(self, *args, **kwargs):
        # For CZ pulses
        self.f_Terms = 1
        self.coupling = 20E6
        self.offset = 300E6
        self.l_coeff = np.array([0.3])

        self.width = 60e-9
        self.amp = 100e6
        self.plateau = 10e-9

        self.dfdV = 500E6
        self.use_spectrum = None
        self.negative_amplitude = False

        self.spectro = None
        self.key_list = ["f_Terms","coupling","offset","width","amp"]
        self.theta_f = None
        self.t_tau = None

    def update_params(self,pdict={}):
        # print("update params, amp:",self.amp)
        param_modified = False
        for key,v in pdict.items():
            if key in self.key_list:
                if isinstance(v,(int,float,complex)):
                    if floateq(self.__getattribute__(key),v,1e-15):
                        continue
                    else:
                        self.__setattr__(key,v)
                        # print('changed_key',key,'changed_value:',v)
                        param_modified = True
                else:
                    raise ValueError('value {} of key {} should be int/float/complex'.format(v,key))
            elif key == 'spectro':
                if v:
                    if isNone(self.spectro):
                        # f01_max, f01_min, Ec, Vperiod, Voffset, V0
                        self.spectro = Transmon(v['f01_max'],v['f01_min'],v['Ec'],v['Vperiod'],v['Voffset'])
                    for spec_key,spec_v in v.items():
                        if spec_key in ['f01_max','f01_min', 'Ec', 'Vperiod', 'Voffset']:
                            if not floateq(spec_v,self.spectro.__getattribute__(spec_key),1e-6):
                                self.spectro.__setattr__(spec_key,spec_v)
                    self.spectro.calculate_JJ()
            elif key == "l_coeff":
                self.l_coeff = np.array(v)
                # param_modified = True
            else:
                self.__setattr__(key,v)
    
        if param_modified:
            # print('recalcute waveform')
            self.calculate_cz_waveform() 

    def calculate_envelope(self, t0, t):
        if self.t_tau is None:
            self.calculate_cz_waveform()

        # Plateau is added as an extra extension of theta_f.
        theta_t = np.ones(len(t)) * self.theta_i
        for i in range(len(t)):
            if 0 < (t[i] - t0 + self.plateau / 2) < self.plateau:
                theta_t[i] = self.theta_f
            elif (0 < (t[i] - t0 + self.width / 2 + self.plateau / 2) <  (self.width + self.plateau) / 2):
                theta_t[i] = np.interp(  t[i] - t0 + self.width / 2 + self.plateau / 2, self.t_tau,  self.theta_tau)
            elif (0 < (t[i] - t0 + self.width / 2 + self.plateau / 2) <  (self.width + self.plateau)):
                theta_t[i] = np.interp(  t[i] - t0 + self.width / 2 - self.plateau / 2, self.t_tau,  self.theta_tau)

        # clip theta_f to remove numerical outliers
        theta_t = np.clip(theta_t, self.theta_i, None)
        df = 2*self.coupling * (1 / np.tan(theta_t) - 1 / np.tan(self.theta_i))

        if not self.use_spectrum:
            # Use linear dependence if no qubit was given
            values = df / self.dfdV
        else:
            values = self.spectro.df_to_dV(df)
        if self.negative_amplitude is True:
            values = -values

        return values

    def calculate_cz_waveform(self):
        """Calculate waveform for c-phase and store in object"""
        # notation and calculations are based on
        # "Fast adiabatic qubit gates using only sigma_z control"
        # PRA 90, 022307 (2014)
        # Initial and final angles on the |11>-|02> bloch sphere
        self.theta_i = np.arctan(2*self.coupling / self.offset)
        # if not self.theta_f:
        if self.amp>0:
            self.theta_f = np.arctan(2*self.coupling / self.amp)
        elif self.amp==0:
            self.theta_f= np.pi/2
        else:
            self.theta_f = np.pi - np.arctan( - 2*self.coupling / self.amp)

        # Renormalize fourier coefficients to initial and final angles
        # Consistent with both Martinis & Geller and DiCarlo 1903.02492

        l_coeff = self.l_coeff
        l_coeff[0] = (((self.theta_f - self.theta_i) / 2) - np.sum(self.l_coeff[range(2, self.f_Terms, 2)]))

        # defining helper variabels
        n = np.arange(1, self.f_Terms + 1, 1)
        n_points = 1000  # Number of points in the numerical integration

        # Calculate pulse width in tau variable - See paper for details
        tau = np.linspace(0, 1, n_points)
        self.theta_tau = np.zeros(n_points)
        # This corresponds to the sum in Eq. (15) in Martinis & Geller
        for i in range(n_points):
            self.theta_tau[i] = (
                np.sum(l_coeff * (1 - np.cos(2 * np.pi * n * tau[i]))) + self.theta_i)
        # Now calculate t_tau according to Eq. (20)
        t_tau = np.trapz(np.sin(self.theta_tau), x=tau)
        # log.info('t tau: ' + str(t_tau))
        # t_tau = np.sum(np.sin(self.theta_tau))*(tau[1] - tau[0])
        # Find the width in units of tau:
        Width_tau = self.width / t_tau

        # Calculating time as functions of tau
        # we normalize to width_tau (calculated above)
        tau = np.linspace(0, Width_tau, n_points)
        self.t_tau = np.zeros(n_points)

        for i in range(n_points):
            if i > 0:
                self.t_tau[i] = np.trapz(np.sin(self.theta_tau[0:i+1]), x=tau[0:i+1])
                # self.t_tau[i] = np.sum(np.sin(self.theta_tau[0:i+1]))*(tau[1]-tau[0])

#%%
import matplotlib.pyplot as plt
if __name__=="__main__":

    slep = Slepian()
    slep.use_spectrum=True
    slepian_collec = {"ch_name":"'zc67'","f_Terms":1,"l_coeff":[0.2],"coupling":60e6,"offset":300e6,"negative_amplitude":False, "dfdV":500e6,"spectro":{"f01_max":6e9, "f01_min":5e9, "Ec":0.2e9,  "Vperiod":1,"Voffset":0.01 } }
    slep.update_params(slepian_collec)
    pulse = slep.calculate_envelope(0,np.linspace(-40e-9,40e-9,81))
    plt.plot(pulse)

# %%
