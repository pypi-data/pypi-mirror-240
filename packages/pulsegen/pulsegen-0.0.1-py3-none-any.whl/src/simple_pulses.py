import NLab.Utils.common as  cm ;  cm.rl(cm);
import numpy as np;
pi = np.pi

#pdt = {"shape":"sine" , "width":0 ,"plateu":"0",  "amp":0, "freq":0 , "pos":0 ,"phase":0} ;
def pi_gate(w,cp,ctx) : 
  w.update(cp['pi'])
  w["vz"] += cp['pi']["phase_offs"] ; 

def pi2gate(w,cp,ctx) : 
  w.update(cp['pi2'])
  w["vz"] += cp['pi2']["phase_offs"] ; 


class I_p:
  __maj_type__="pulse" ;
  __mnr_type__='I_p';
  def __init__(self, **kwds_):
    self.kw = kwds_;

  def get_pd(self, pdt, cp=None , ctx=None):
    w=pdt.copy();
    self.will(w,cp,ctx);
    w.update(self.kw) ; 
    return w; 
  def will(self,w,cp,ctx): w["amp"] = 0 ; w["width"]  =0;  w["plateau"] =0 ; 

class X_p(I_p):
  __mnr_type__="X_p"; 
  def will(self,w,cp,ctx):pi_gate(w,cp,ctx);  w["phase"] = 0 ; 

class Y_p(I_p):
  __mnr_type__="Y_p"; 
  def will(self,w,cp,ctx):pi_gate(w,cp,ctx);   w["phase"] = pi/2 ; 

class mX_p(I_p):
  __mnr_type__="mX_p"; 
  def will(self,w,cp,ctx):pi_gate(w,cp,ctx);   w["phase"] = pi ; 

class mY_p(I_p):
  __mnr_type__="mY_p"; 
  def will(self,w,cp,ctx):pi_gate(w,cp,ctx); w["phase"] = 3*pi/2 ; 


class X2_p(I_p):
  __mnr_type__="X2_p"; 
  def will(self,w,cp,ctx):pi2gate(w,cp,ctx);  w["phase"] = 0 ; 

class Y2_p(I_p):
  __mnr_type__="Y2_p"; 
  def will(self,w,cp,ctx):pi2gate(w,cp,ctx);  w["phase"] = pi/2 ; 

class mX2_p(I_p):
  __mnr_type__="mX2_p"; 
  def will(self,w,cp,ctx):pi2gate(w,cp,ctx);  w["phase"] = pi ; 


class mY2_p(I_p):
  __mnr_type__="mY2_p"; 
  def will(self,w,cp,ctx):pi2gate(w,cp,ctx);  w["phase"] = 3*pi/2 ; 

class F_p(I_p):
  __mnr_type__="F_p"; 
  def will(self,w,cp,ctx): w.update(cp["fp"]);  w["freq"] = 0 ; 


class W_p(I_p):
  __mnr_type__="Y_p"; 
  def will(self,w,cp,ctx): pi_gate(w,cp,ctx);   w["phase"] = pi/4  ; 

class mW_p(I_p):
  __mnr_type__="Y_p"; 
  def will(self,w,cp,ctx): pi_gate(w,cp,ctx);   w["phase"] = 5*pi/4 ; 

class W2_p(I_p):
  __mnr_type__="X2_p"; 
  def will(self,w,cp,ctx):   pi2gate(w,cp,ctx);  w["phase"] = pi/4  ; 

class mW2_p(I_p): 
  __mnr_type__="X2_p"; 
  def will(self,w,cp,ctx): pi2gate(w,cp,ctx);   w["phase"] = 5*pi/4 ; 

class VZ_left_p(I_p):
  __mnr_type__="VZ_left_p"; 
  def will(self,w,cp,ctx): 
    w['amp'] = 0 ; 
    w['vz'] = cp["vz_left"];

class VZ_right_p(I_p):
  __mnr_type__="VZ_left_p"; 
  def will(self,w,cp,ctx): 
    w['amp'] = 0 ; 
    w['vz'] = cp["vz_right"]; 




