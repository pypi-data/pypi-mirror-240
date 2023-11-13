from  numpy.core.fromnumeric import shape
import NLab.Utils.common as cm ;
import numpy as np;
import PulseGen.shapes as shapes; cm.rl(shapes)
from scipy.fft import fft
import PulseGen.predistortion as predt; cm.rl(predt) 

import copy; 
pi = np.pi ; 
pi4 = pi/4; 
sq2 = np.sqrt(2) ; 

def dur(pd):
  return (cm.dkd(pd,"width" , 0 ) + cm.dkd(pd,"plateau" , 0 )) ;

def rng(pd , tx):
  #print(pd["pos"]) ;  
  a = int(( pd["pos"] - cm.dkd(tx , "st",  0 ) ) *tx["srate"]  );
  b = int(dur(pd) * tx["srate"] ) ; 
  return max(a-5 , 0) , min(a+b+5 , tx["N"] ); 

def floateq(a,b,thr=1e-3):  
	return np.abs(a-b) < thr; 

def check_int(value,thr=1e-3):
  return floateq(int(value),value,thr  )

def skew(w,theta = np.pi/4):
  # return w
  return np.real(w)*np.cos(theta)*np.sqrt(2) + 1j*np.imag(w)*np.sin(theta)*np.sqrt(2)
 
def grad(sh ): 
  if(len(sh) <=1) :return 0*sh   ; 
  else : return np.gradient(sh) ; 

def fetch(list_a,list_b,name):
  """
  list_a=['a','b','c','d'];
  list_b=[12,23,34,1];
  fetch[list_a,list_b,'c'] = 34
  """
  if len(list_a)!=len(list_b): raise ValueError("length of list_a '{}' is not equal to length of list_b '{}' ".format( len(list_a),len(list_b) ) )
  return list_b[list_a.index(name)]

def get_freq(plen, srate):
    """
    return x_axis of 'np.fft.fft(pulse)', with total-length-of-pulse = plen, sampling-rate = srate;
    """
    pl = int(plen)
    f = np.linspace(0,srate,pl,endpoint=False)
    f[int(pl/2):] = srate - f[int(pl/2):]
    return f

def h_delay(delay,plen,srate):
    f = get_freq(plen,srate)
    h_d = np.exp(1j*2*np.pi*delay*f)
    h_d[int(plen/2) + 1 : ] =  h_d[int(plen/2) + 1 : ].conjugate()
    return h_d

def carrier(X , freq , ph=0 , imb=0 ):
  A = np.cos( pi4 + imb) * sq2  ; 
  B = np.sin( pi4 + imb) * sq2  ; 
  p2 = pi/2  + ph  ; 
  return A * np.cos( 2*pi*freq*X ) - 1j*B*np.cos( 2*pi*freq*X + p2) ; 


def pulses(pds,tx):
  N = tx["N"] ; 
  tx_st = cm.dkd(tx ,"st" , 0 );
  tx_ed = tx_st+(N/tx['srate']) ;

  # iq phase and imbalance : 

  iq_ph   = 0 ;  
  iq_imb  = 0 ;  
  off = cm.dkd(tx ,"offset" , 0 ); 
  goff = cm.dkd(tx ,"offset_global" , 0 );  # global offset
  off_s =  int( cm.dkd(tx ,"offset_s" , 0 ) * tx['srate'])
  off_e =  int( cm.dkd(tx ,"offset_e" , tx_ed - 5e-6 + 20e-9) * tx['srate'])
  S_offset = np.zeros( N , dtype=np.complex128 )
  S_offset[off_s:off_e] = off

  # time track 
  X = np.linspace(tx_st , tx_ed ,N ,endpoint = False ); 
  # wave track with carrier 
  W = np.zeros( N , dtype=np.complex128 ); 
  # wave track with out carrier 
  S = np.zeros( N , dtype=np.complex128 ); 
 
  # planting puleses
  for pd in pds :  
    st,ed = rng(pd,tx); 
    if(ed -st < 2 ) : continue; 
    # decide work range
    wX =  X[st:ed]; 
    # decide shape 
    if(type(pd["shape"])  == str):
      sh = shapes.shapeTable[pd["shape"]](wX,pd,{});      # create pulse shape
    elif (callable(pd["shape"])):
      sh = pd["shape"](wX,pd,{});      # create pulse shape
    # fix drag 
    sh +=1j*grad(sh)*tx["srate"]*cm.dkd(pd,"drag_scale",0);
    # scale amplitude as well as phase  
    drag_t = cm.dkd(pd,"drag_detuning",0) ; 
    center = (pd["width"] + pd["plateau"] ) / 2 + pd['pos'] ; 
    sh = cm.dkd(pd,"amp_scale",1) * np.exp(1j*(pd["phase"] + pd["phase1"] ) )*sh * np.exp(1j*2*np.pi*drag_t*(wX - center));  
    # carrier pulse  
    cr = carrier( wX - wX[0] , pd["freq"], iq_ph , iq_imb )  ; 
    # assgin range
    W[st:ed] += sh*cr ; 
    S[st:ed] += sh

  W += S_offset
  return [X,W+goff,S+goff ]; 


def pulse_batch(pdc:dict,line_info:dict):
  pluse_dict = {}; 
  for k,v in line_info.items():
    if(k!="extra") :
      pluse_dict[k]  =pulses(cm.dkd(pdc,k,[]), v) ; 
  extra = cm.dkd(line_info  , "extra" , {}) ; 
  

  if ("crosstalk" in extra):
    pluse_dict = crosstalk(pluse_dict,extra['crosstalk'])

  if ("predistortion" in extra):
    pluse_dict = predistortion(pluse_dict,extra['predistortion'],extra['srate'])

  if ("mixer_imbalance" in extra):
    pluse_dict = mixer_cali(pluse_dict,extra['mixer_imbalance'])

  if ("channel_delay" in extra):
    pluse_dict = channel_delay(pluse_dict,extra['channel_delay'],extra['srate'])

  return pluse_dict; 



def channel_delay(pulse_c,ch_delay_dict,srate):
  for k,v in pulse_c.items():
    delay = cm.dkd(ch_delay_dict,k,0)
    # x,w,s = v
    rd = round(delay*srate)
    v[0] = v[0] + rd/srate
    rd_inv = -1*rd
    if rd_inv == 0:
      continue
    elif rd_inv>0:
      v[1][rd_inv:] = v[1][:-rd_inv]
      v[2][rd_inv:] = v[2][:-rd_inv]
    else:
      v[1][:rd_inv] = v[1][-rd_inv:]
      v[2][:rd_inv] = v[2][-rd_inv:]
  return pulse_c

def mixer_cali(pulse_c,mixer_imb_dict):
  for k,v in pulse_c.items():
    if k in mixer_imb_dict.keys():
      iq_phase =  cm.dkd(mixer_imb_dict[k],"iq_phase",0)  
      theta  = cm.dkd(mixer_imb_dict[k],"iq_imb",0)+np.pi/4 
      v[1] = v[1].real + 1j* ( v[1].imag * np.cos(iq_phase) + v[1].real * np.sin(iq_phase)   )  
      v[2] = v[2].real + 1j* ( v[2].imag * np.cos(iq_phase) + v[2].real * np.sin(iq_phase)   )  
      v[1] = skew(v[1],theta)
      v[2] = skew(v[2],theta)
  return pulse_c

def predistortion(pulse_c,predistor_info,srate):
  for k,v in pulse_c.items():
    distor_dict=cm.dkd(predistor_info,k,{})
    if distor_dict:
      rwe = cm.dkd(distor_dict,'rwe',{})
      iir = cm.dkd(distor_dict,'iir',{})
      fir = cm.dkd(distor_dict,'fir',{})
      if rwe:
        x,w,s = v
        rw = rwe["ratio"]*np.exp(1j*rwe["phase"])*w ;    
        rs = rwe["ratio"]*np.exp(1j*rwe["phase"])*s ; 
        dN = int(rwe['delay'] * srate)
        w[dN:] += rw[:-dN]
        s[dN:] += rs[:-dN]
      if iir:
        iir_1st = cm.dkd(iir,'first',{})
        iir_2nd = cm.dkd(iir,'second',{})
        v[1] = predt.predistor(v[1],iir_1st,iir_2nd,srate)
        v[2] = predt.predistor(v[2],iir_1st,iir_2nd,srate)
      if fir:
        fir_width = cm.dkd(fir,'width',{})
        fir_delay = cm.dkd(fir,'delay',{})
        fir_amp = cm.dkd(fir,'amp',{})
        v[1] = predt.convolve_ringback(v[1],fir_delay,fir_width,fir_amp,srate)
        v[2] = predt.convolve_ringback(v[2],fir_delay,fir_width,fir_amp,srate)
  return pulse_c

def crosstalk(pulse_uc,crosstalk_dict):
  
  pulse_c = {} ; 
  for k,v in pulse_uc.items(): 
    pulse_c[k] = [v[0] , v[1].copy() , v[2].copy() ]  ;  
  
  crosstalk_xy = cm.dkd(crosstalk_dict, 'XY' , {} )
  crosstalk_z = cm.dkd(crosstalk_dict, 'Z' , {} )

  if crosstalk_xy:
    if("XYSEL" in crosstalk_dict) : 
      L = crosstalk_xy["channels"] ; 
      M =  crosstalk_xy['matrix'] ; 
      for c in L : 
        pulse_c[c] = [ pulse_uc[c][0] , pulse_uc[c][1].copy() , pulse_uc[c][2] ] ; 
      for a,b in crosstalk_dict["XYSEL"] : 
        ia =L.index(a) ;  ib= L.index(b) ; 
        pulse_c[b][1]+=  M[ia][ib] * pulse_uc[a][1] ;  
    else : 
      xy_ch_names = crosstalk_xy['channels']
      xy_matrix = np.array(crosstalk_xy['matrix'])
      carrier_freq = crosstalk_xy['lo_freq']
      pulse_c = _crosstalk(pulse_c,pulse_uc,xy_ch_names,xy_matrix,carrier_freq)

  # if crosstalk_z:
  #   z_ch_names = crosstalk_z['channels']
  #   z_matrix = np.array(crosstalk_z['matrix'])
  #   pulse_c =_crosstalk(pulse_c,pulse_uc,z_ch_names,z_matrix,carrier_freq=None)
  return pulse_c


def _crosstalk(pulse_c,pulse_uc,ch_names,ct_matrix,carrier_freq=None ):
    for control_ch_idx, control_ch_name in enumerate(ch_names):
      if ( control_ch_name not in pulse_uc.keys() ):
        continue 
      x,w,s = pulse_uc[control_ch_name]
      for target_ch_idx, target_ch_name in enumerate(ch_names):
        if target_ch_idx == control_ch_idx:
          continue
        if type(carrier_freq) != type(None):
          carrier_freq_diff = -1* carrier_freq[target_ch_idx] + carrier_freq[control_ch_idx] 
          # print("cidx",control_ch_idx,"tidx", target_ch_idx,carrier_freq_diff)
          w_c = w * carrier( x ,  carrier_freq_diff , 0 ) 
        else:
          w_c = w.copy()
        x1,w1,s1 = [x,w_c*ct_matrix[control_ch_idx,target_ch_idx],s*ct_matrix[control_ch_idx,target_ch_idx] ]
        if ( target_ch_name not in pulse_c.keys() ):
          pulse_c.update( {target_ch_name:[x1,w1,s1]} )
        else:
          pulse_c[target_ch_name][1] += w1; pulse_c[target_ch_name][2] += s1; 
    return pulse_c
    


def cross( A , F , D , wves ):
  L = np.min( [ len(A),  len(F) , len(D) , len(wves)  ] ) ;
  W = 0 ; 
  for l in  range( L ) : 
    W += A[l]*np.exp(F[l])*wves[l];
  return W; 



        
