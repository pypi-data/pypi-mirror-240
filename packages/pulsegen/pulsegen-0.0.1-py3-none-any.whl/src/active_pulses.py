from PulseGen.basic_pulses import * ; 
import multiprocessing as mp ;
from multiprocessing import Pool ; 
import numpy as np

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

def fix(X,Y,irr) : 
    Yp =  np.copy(Y)  ; 
    for F  in  irr : 
        Yp  =  IIR_filtering( F[1] , F[3]  , F[2]   ,  [X , Yp] ) ;  
    return Yp ; 


def predistortion(pubs,predistor_info,srate):
  for k,v in pubs.items():
    distor_dict=cm.dkd(predistor_info,k,{})
    if distor_dict and v.F:
      rwe = cm.dkd(distor_dict,'rwe',{})
      iir = cm.dkd(distor_dict,'iir',{})
      fir = cm.dkd(distor_dict,'fir',{})
      if rwe:
        rw = rwe["ratio"]*np.exp(1j*rwe["phase"])*v.W;    
        rs = rwe["ratio"]*np.exp(1j*rwe["phase"])*v.S ; 
        dN = int(rwe['delay'] * srate)
        v.W[dN:] += rw[:-dN]
        v.S[dN:] += rs[:-dN]
      if iir:
        iir_1st = cm.dkd(iir,'first',{})
        iir_2nd = cm.dkd(iir,'second',{})
        #TODO
        #v.W = predt.predistor(v.W,iir_1st,iir_2nd,srate)
        #v.S = predt.predistor(v.S,iir_1st,iir_2nd,srate)
        v.W = fix(v.X , v.W, iir_1st ) ; 
        #v.S = predt.fix(v.X , v.S, iir_1st ) ; 
        #v.S = predt.predistor(v.S,iir_1st,iir_2nd,srate)
      if fir:
        fir_width = cm.dkd(fir,'width',{})
        fir_delay = cm.dkd(fir,'delay',{})
        fir_amp = cm.dkd(fir,'amp',{})
        v.W = predt.convolve_ringback(v.W,fir_delay,fir_width,fir_amp,srate)
        v.S = predt.convolve_ringback(v.W,fir_delay,fir_width,fir_amp,srate)


def crosstalk(pubs,crosstalk_dict):
  crosstalk_z = cm.dkd(crosstalk_dict, 'Z' , {} )
  if crosstalk_z:
    z_ch_names = crosstalk_z['channels']
    z_matrix = np.array(crosstalk_z['matrix']) ;
    #print(z_matrix) ; 
    for i,znm1  in enumerate(z_ch_names) : 
      for j,znm2 in enumerate(z_ch_names) : 
        pubs[znm1].W1 += z_matrix[j][i] * pubs[znm2].W  ; # XXX
    for i,znm1  in enumerate(z_ch_names) :  
        pubs[znm1].W =  pubs[znm1].W1;  
        pubs[znm1].F =  True;  


class PulseUnitBuffer() : 
  def __init__(self , st,ed,LEN,gof,npdtype) : 
    self.X = np.linspace(st,ed,LEN , dtype = npdtype) ; 
    self.W = np.zeros(LEN , dtype = npdtype); 
    self.S = np.zeros(LEN, dtype = npdtype); 
    self.W1 = np.zeros(LEN , dtype = npdtype); 
    self.F = False ; 
    self.gof = gof ; 
    # created not to be update 

  def reset(self ): 
    self.W.fill(self.gof);
    self.S.fill(self.gof);
    self.F = True ; 

  def get_part(self , which) : 
    return{
      "X" :  self.X ,  
      "WR" : np.real(self.W), 
      "WI" : np.imag(self.W),
      "SR" : np.real(self.S), 
      "SI" : np.imag(self.S),
    }[which] ;

  def set_active(self) : self.F = True ; 
  def set_deactive(self) : self.F = False ; 
  def isactive(self) : return self.F  ; 

#########################################
### Massive Parallel implementation
#########################################
POOL_ATTRNAME = "ACTIVE_PULSE_POOL";
def manage_pool(n): 
  setattr( __builtin__ , POOL_ATTRNAME , Pool(n) )

def manage_pool_norep(n): 
  new_pool = True ; 
  if(hasattr( __builtin__ , POOL_ATTRNAME )) : 
    p = get_pool();
    if( n == len(p._pool)):  new_pool = False ; 
  if(new_pool) : manage_pool(n);

def get_pool(n):
  return getattr( __builtin__ , POOL_ATTRNAME );

class ActivePulses() : 
  def __init__(self , line_info , active_lines = []  , num_pool = 7   ): 
    #manage_pool_norep(num_pool);
    #P = get_pool();
    
    self.active_line_id = set(active_lines) ; 
    self.line_info = line_info ; 
    self.liid = {} ; 
    self.PUBS ={} ; 
    for k,v in self.line_info.items() : 
      st = cm.dkd(v,"st" ,0  )    ; 
      sr = cm.dkd(v,"srate" , 2e9 )    ; 
      N = cm.dkd(v,"N" ,128  )    ; 
      ed = st +  (N-1) / sr   ; 
      dt = cm.dkd(v, "dtype" , np.complex128) 
      gof = cm.dkd(v , "offset_global" , 0 )
      self.PUBS[k] = PulseUnitBuffer(st,ed,N,gof,dt) ; 
      self.liid[cm.dkd(v , 'id',  0 ) ] = k ;
    self.first = True ; 


  def gen1(self, pdc , X , W,S  ) : pass 


  def gen(self,pdc,extra) : 
    self.extra = extra
    for v in self.PUBS.values(): v.F =False; # clear all the flags 
    
    if(self.first): 
      for line_id in self.active_line_id : 
        if(line_id  in self.liid ):  
          k = self.liid[line_id];
          if(k in self.PUBS): self.PUBS[k].reset() ; 
      self.first = False ;

    for k , pds in  pdc.items() : 
      pub = self.PUBS[k]; 
      pub.reset() ;
      li =self.line_info[k]  ; 
      off = cm.dkd( li , "offs" , 0  ) ; 
      for pd in pds :  
        st,ed = rng(pd,li); 
        if(ed -st < 2 ) : continue; 
        
        # decide work range
        wX =  pub.X[st:ed]; 
        
        # decide shape 
        if(type(pd["shape"])  == str):
          sh = shapes.shapeTable[pd["shape"]](wX,pd,{});      # create pulse shape
        elif (callable(pd["shape"])):
          sh = pd["shape"](wX,pd,{});      # create pulse shape
        # fix drag 
        sh +=1j*grad(sh)*li["srate"]*cm.dkd(pd,"drag_scale",0);
        
        # scale amplitude as well as phase  
        drag_t = cm.dkd(pd,"drag_detuning",0) ; 
        center = (pd["width"] + pd["plateau"] ) / 2 + pd['pos'] ; 
        sh = cm.dkd(pd,"amp_scale",1) * np.exp(1j*(pd["phase"] + pd["phase1"] ) )*sh * np.exp(1j*2*np.pi*drag_t*(wX - center)) ;  
        
        # carrier pulse  
        cr = carrier( wX , pd["freq"], 0 , 0 )  ; 
        
        # assgin range
        pub.W[st:ed] += sh*cr + cm.dkd(pd , "offset" , 0 ); 
        pub.S[st:ed] += sh + cm.dkd(pd , "offset" , 0 );
        
      pub.W+=off; 
      pub.S+=off ; 
    
    if ("crosstalk" in self.extra):
      crosstalk(self.PUBS, self.extra['crosstalk']); 

    if("predistortion" in self.extra)  :
      predistortion(self.PUBS, self.extra["predistortion"] , self.extra["srate"]) ; 
    
    return self; 


  def to_display_pulses(self) : # terminal functions
    """
    APC is the eventually formate that is transfered to the wave displayer
    """
    APC = {} ; # active pulse collection
    for k,pub in self.PUBS.items() : 
      if(pub.F)  : 
        li = self.line_info[k] ; 
        disp = cm.dkd(li , "disp" , [])
        height = cm.dkd(li, "h" , 0 ) ; 
        if(0 == len(disp )): continue ; 

        disp = ["X"] + disp ; 
        displist = [] ;  
        for disp_item in disp : 
          displist.append(pub.get_part(disp_item));  
        APC[ k ] =   [
            k , height ,  displist 
        ]
    return APC; 


  def to_send_pulses(self) : 
    """
    APC eventually is the "device-channel : required-waveform" like situation
    """
    APC = {} ;
    for k, pub in self.PUBS.items() : 
      if(pub.F) : 
        li = self.line_info[k] ; 
        channel_target = cm.dkd(li,  "target" , None) ; 
        if(None == channel_target) : continue ; 
        channel_format =  cm.dkd(li , "sendas" , np.complex128   )  ;
        APC[channel_target] = channel_format(pub.W) ;
    return APC ; 


