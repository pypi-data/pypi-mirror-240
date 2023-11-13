import NLab.Utils.common as  cm ;  cm.rl(cm); 
import PulseGen.share ; cm.rl(PulseGen.share); from PulseGen.share import * ;   
import PulseGen.gates ; cm.rl(PulseGen.gates); from PulseGen.gates import * ;   
import PulseGen.simple_pulses   ;cm.rl(PulseGen.simple_pulses  ); from PulseGen.simple_pulses   import * ;
import PulseGen.moderator as MD ; cm.rl(MD) ;
import numpy as np  ; import time ; 

def xqubits(qubits):
  s = "" ;  
  lq = len(qubits)-1;
  for i,q in enumerate(qubits) :  
    s+=str(q);
    if(i<lq): s+="x" ; 
  return s ;

def copy_gate(g):
  return type(g)(**g.kwds);


class RULE:
  __maj_type__="RULE" ; 
  __mnr_type__="RULE" ;
  
  def __init__( self , **kwds) :
    self.kw = kwds.copy();   lms=[]; 
    self.lm = {} ;
    for k , v in self.kw.items():
      if( k in MD.LookUpKeys ): self.lm[k]=v;  
    for k in self.lm: self.kw.pop(k); 
    # here the pulses have keywords

  
  def apply_one(self , qubits , qubit_info , line_info , **kwds) :
    kw = self.kw.copy(); 
    kw.update(kwds) ; 
    RES= {}; 
    lc =  qubit_info[xqubits(qubits)];
    for line, tracks in self.lm.items():
      # TODO : costom pdt
      line_name = lc[line]['nm'];  # getting the line number
      line_kw = catch( kw, line ) ;  # getting the keywords from the gate
      cp = lc[line]["cp"];   # the line based calibration parameter  
      pdt = lc[line]["pdt"];  # the every one of the usable line 
      target_tracks = [] ; 
      for i,track in enumerate(tracks):  
        track_kw = catch( line_kw , str(i) ); 
        target_track = [];
        for j,pulse in enumerate(track): 
          pulse_kw = catch( track_kw , str(j) );
          Target = None ; 
          if(type(pulse) == type): Target = pulse(**pulse_kw).get_pd(pdt,cp) ; 
          else:  
            Target_ = type(pulse)();
            Target_.kw = pulse.kw.copy()
            Target_.kw.update(pulse_kw) ; 
            Target = Target_.get_pd(pdt,cp)  ;
          target_track.append(Target); 
        target_tracks.append(target_track) ;
      RES[line_name]= target_tracks;
    return RES ; 


def apply(rules , circuit , qubit_info, line_info,extra):

  """
    rules : 
      should be a dictionary that key is the 
        all the gates __mnr_type__ attribute, that makes clear what 
        type of gate is this, for example :  CZ.__mnr_type__ where it
        was a string 'CZ', the values should be an instance of ARULE
    
    circuit: is just 2 levele nested list , elements of these lists are
      gates, for example : 
        A = [ 
          [CZ(0,2) , X(1), Y(3)] , 
          [I(0, delay=20e-9)] , 
          [CZ(0,1) , X(2), Y(3)] , 
        ]
      here the CZ ,X ,Y , I are all gates.
    m : is the Moderator, moderator knows exact qubit lines, the coulpers between
      the qubits and it works as applying a local rule to the global lines . 
    return :
      This function will return a dictionary,  its keys are global lines string.
  """
  #t1 = time.time() ;  
  end_pos = extra["end_pos"] ; 
  RES= []
  UP = [] ; 
  U_len = [] ;  
  for U in circuit :
    RES1 = [ ];  
    U_lengths=[]; 
    for G in U : 
      assert(G.__mnr_type__ in rules) , "apply_A, rules for gate type \"{}\" is not set".format(G.__mnr_type__) ;
      rule = rules[ G.__mnr_type__ ] ; # possible rule not exist error  
      R = rule.apply_one( G.qubits() , qubit_info , line_info ,**G.kwds ) ;  
      for k,tracks in R.items(): 
        for track in tracks : 
          ltrack = 0 ;  
          for pulse in track : 
            ltrack+=get_len(pulse);
          U_lengths.append(ltrack); 
      RES1.append(R);  

    if( len(U_lengths) == 0 ) : U_len.append(0) ; 
    else  : U_len.append(np.max(U_lengths))  ;
    RES.append(RES1) ;

  # plant the wave : 
  U_len.reverse();
  RES.reverse(); 
  U_pos = end_pos ;
  for i,U in enumerate(RES) : 
    U_pos -=U_len[i];
    for G in U : 
      for k,tracks in G.items(): 
        for track in tracks :
          st  = U_pos;
          for pulse in track:
            pulse["pos"] = st;     
            st += get_len(pulse) ; 
  
  RES.reverse();
  #print(time.time() - t1) ; 
  return RES; 

def handle_vz(RES):
  for pdt in RES.values():
    vz_accum = 0
    for pd in pdt:
      pd['phase'] -= vz_accum
      vz_accum +=cm.dkd(pd,'vz',0)
  return RES ; 

#@jit(nopython=True)
def flattern(RES):
  LN=[];
  for U in RES : 
    for G in U : 
      for k,tracks in G.items():
        for i,track in enumerate(tracks) : 
          if(len(LN) < i+1): LN.append({});
          for pulse in track : 
            if(k not in LN[i]) : LN[i][k]=[];
            LN[i][k].append(pulse) ; 
  return LN ; 

def handle_vz_tracks(LN ) : 
  for track_lane in LN :
    for k,track in track_lane.items():
        vz_accum = 0 ; 
        for pd in track:
          #print(pd)
          pd['phase'] -= vz_accum
          vz_accum +=cm.dkd(pd,'vz',0)
  return LN ; 



def  join_tracks(LN) :
  """
    joinging tracks
  """
  T = {} ; 
  for track_lane in LN :
    for k,track in track_lane.items() : 
      if( k not in T ): T[k]  = [] ; 
      T[k] += track ; 
  return T ; 
