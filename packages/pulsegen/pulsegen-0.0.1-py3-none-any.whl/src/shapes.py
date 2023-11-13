import NLab.Utils.common as  cm ;  cm.rl(cm);  
from PulseGen.global_var import SLEPIAN_dict,AWP_dict

import  PulseGen.edges as edges ; 
import PulseGen.slepian as slepian; cm.rl(slepian); from PulseGen.slepian import *
import numpy as np
pi = np.pi; 

def sine(X , pd, cp={} ):
  if(np.abs(pd["width"]) < 1e-14): return square(X , pd)  ; 
  a = cm.dkd(pd, "scale_a",0 ) ;
  b = cm.dkd(pd, "scale_b",1 ) ;
  p = pd["pos"] + pd["width"]/4; 
  return pd['amp']*edges.sine_edge(  X , p  , pd["width"]/2,  a,b ) * edges.sine_edge(  -X,  -(p + pd["width"]/2 + pd["plateau"]  ), pd["width"]/2, a,b )  ;

def sine2pi(X , pd, cp={} ):
  if(np.abs(pd["width"]) < 1e-14): return square(X , pd)  ; 
  p = pd["pos"] + ( pd["width"]  + pd["plateau"])/2 ;  
  return pd['amp']*edges.sine_edge_2pi(  X , p  ,pd["width"]  + pd["plateau"])   ; 

def cosine(X , pd, cp={} ):
  if(np.abs(pd["width"]) < 1e-14): return square(X , pd)  ; 
  a =0 ; b =1 ; 
  p = pd["pos"] + pd["width"]/4; 
  return pd['amp']*edges.sine_edge(  X , p  , pd["width"]/2,  a,b ) * edges.sine_edge(  -X,  -(p + pd["width"]/2 + pd["plateau"]  ), pd["width"]/2, a,b )  ;  

def hcosine(X , pd, cp={} ):
  if(np.abs(pd["width"]) < 1e-14): return square(X , pd)  ; 
  a =0.5 ; b =1; 
  p = pd["pos"] + pd["width"]/4; 
  return pd['amp']*edges.sine_edge(  X , p  , pd["width"]/2,  a,b ) * edges.sine_edge(  -X,  -(p + pd["width"]/2 + pd["plateau"]  ), pd["width"]/2, a,b )  ; 

def hcosine_asys(X , pd, cp={} ):
  if(np.abs(pd["width"]) < 1e-14): return square(X , pd)  ; 
  a =0.5 ; b =1; 
  ls = cm.dkd(pd,'left_scale',1)
  rs = cm.dkd(pd,'right_scale',1)
  p = pd["pos"] + pd["width"]/4; 
  return pd['amp']*edges.sine_edge(  X , p  , pd["width"]/2*ls,  a,b ) * edges.sine_edge(  -X,  -(p + pd["width"]/2 + pd["plateau"]  ), pd["width"]/2*rs, a,b )  ; 

def square(X , pd, cp={} ):
  p = pd["pos"]; 
  w = pd["width"] + pd["plateau"] ; 
  #return edges.square_edge(  X , p  ) * edges.square_edge(  -X,  -(p+w) )   ;  
  return pd['amp']*( (( X >= p ) & (X  < p + w)  )+ 0j ) ; 
  #return np.zeros( len(X) , dtype= np.complex128 ); 

def tanh(X, pd, cp={} ):
  p = pd["pos"]
  w = pd["width"]
  amp = pd['amp']
  epsilon = pd["epsilon"]
  tau = pd["width"]/2

  return amp*np.tanh(2*epsilon*(X-p)/tau)*( (( (X-p) >= 1e-10 ) & ( (X-p-w/2)  < 1e-10)  )+ 0j )+amp*np.tanh(2*epsilon*(2*tau-(X-p))/tau)*( (( (X-p-w/2) >= 1e-10 ) & ( (X-p-w)  <= 1e-10 )  )+ 0j)  ;

def hyper(X, pd, cp={} ):
  p = pd["pos"]
  w = pd["width"]
  amp = pd['amp']
  plateau = pd['plateau']
  epsilon = pd["epsilon"]
  tau = w

  y=(np.cosh(epsilon/2) - np.cosh(epsilon*((X-p)/tau-1/2)))*( (( (X-p) >= 1e-20 ) & ( (X-p-w/2) <= 1e-20 ) )+ 0j)+(np.cosh(epsilon/2) - np.cosh(epsilon*((X-p)/tau-1/2)))*( (( (X-p-w/2) >= 1e-20 ) & ( (X-p-w) <= 1e-20 ) )+ 0j)

  y/=np.max(y)
  return amp*y ;

def awp_shape(X, pd, cp={}):
  """
    currently use slepian instead.
  """
  global AWP_dict
  ampl = pd['fcoeff'] #cm.dkd(pd,'fcoeff',0)
  L_coeff = ampl  if isinstance(ampl,(int,float)) else np.array(ampl)
  awp = cm.dkd(AWP_dict, cp['AWP']['ch_name'] , None)
  awp.update_params(cp['AWP'])
  center_pos = pd["pos"]+pd["width"]/2+pd['plateau']/2; 
  if pd["width"]<2e-9:
    return np.zeros_like(X,dtype=complex)
  return awp.calculate_envelope(center_pos,X,pd["width"],pd['plateau'],L_coeff)+0j

def slepian_shape(X, pd, cp= {}):
  """
    "pdt":{
           "shape":"'slepian'",
           "slepian_collec":{ "ch_name":"'zc67'",
                              "f_Terms":1,
                              "l_coeff":[0.2],
                              "coupling":60e6,
                              "offset":300e6,
                              "negative_amplitude":False,
                              "use_spectrum":False,
                              "dfdV":1200e6,
                              "spectro":{"f01_max":6e9,
                                                "f01_min":4e9,
                                                "Ec":0.2e9,
                                                "Vperiod":1,
                                                "Voffset:0}
                            }
          }
  """
  global SLEPIAN_dict
  slepian_collec = pd['slepian_collec']
  slepian_collec.update({"width":pd['width']}) 
  slepian_collec.update({"amp":pd['amp']}) 
  slepian_collec.update({"plateau":pd['plateau']}) 

  slepian_pulse = cm.dkd(SLEPIAN_dict,slepian_collec["ch_name"],None)
  if not slepian_pulse:
    # print('creat new slepian shape')
    slepian_pulse = Slepian()
    SLEPIAN_dict[slepian_collec["ch_name"]] = slepian_pulse

  slepian_pulse.update_params(slepian_collec)
  center_pos = pd["pos"]+pd["width"]/2+pd['plateau']/2
  return slepian_pulse.calculate_envelope(center_pos,X)+0j

def circle_amp(amp,amp0):
  if amp>=2*amp0:
    return amp0
  else:
    return np.sqrt( (2.5*amp0)**2 - (2.0*amp0 - amp)**2) - 1.5*amp0

def dcosine(X, pd, cp={}):
  if(np.abs(pd["width"]) < 1e-14): return square(X , pd)  ; 
  cp_dcos = cm.dkd(cp,'dcos',{})
  lscale = cm.dkd(cp_dcos,'lscale',0.5)
  lpos = cm.dkd(cp_dcos,'lpos',0.4)
  rpos = cm.dkd(cp_dcos,'rpos',0.4)
  s0 = pd["pos"]
  s1 = s0 + pd["width"] * lscale
  s2 = s1 + pd["plateau"] 
  s3 = s2 + pd["width"] * (1 - lscale)
  s01_mid = s0 + pd["width"] * lscale * lpos
  s23_mid = s3 - pd["width"] * (1 - lscale) * rpos

  lamp =circle_amp( pd['amp'], cm.dkd(cp_dcos,'lamp',0.4) )
  ramp =circle_amp( pd['amp'], cm.dkd(cp_dcos,'ramp',0.4) )

  # print(s0,s1,s2,s3,s01_mid,s23_mid)
  Y = np.zeros(len(X) , dtype=np.complex128) ;  
  Y += ( ( X >= s0 ) & ( X < s01_mid ) )*np.sin( (X-s0)/(s01_mid - s0) * np.pi *0.5 ) * lamp
  Y += ( ( X >= s01_mid ) & ( X < s1 ) )*( ( np.sin( (X-s01_mid)/(s1 - s01_mid) * np.pi - np.pi/2 ) * 0.5 + 0.5 )* (pd['amp'] - lamp) + lamp)
  Y += ( ( X >= s1 ) & ( X < s2 ) ) * pd['amp']
  Y += ( ( X >= s2 ) & ( X < s23_mid ) )*( ( np.sin( (X-s2)/(s23_mid - s2) * np.pi + np.pi/2) * 0.5 + 0.5 )* (pd['amp'] - ramp) + ramp )
  Y += ( ( X >= s23_mid ) & ( X < s3 ) )*np.sin( (X-s23_mid)/(s3 - s23_mid) * np.pi *0.5 + np.pi/2 )  * ramp
  return Y


shapeTable={
  "sinedpi":sine2pi,
  "sine" : sine ,
  "square" : square , 
  "awp": awp_shape,
  "cos" : cosine,
  "hcos_asys" : hcosine_asys,
  "hcos" : hcosine,
  "dcos" : dcosine,
  "slepian" : slepian_shape,
  "tanh": tanh,
  "hyper": hyper
}


