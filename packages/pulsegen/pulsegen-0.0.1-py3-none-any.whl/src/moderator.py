import NLab.Utils.rwjson as rwj

QubitLinesLookUp ={
    "d0"   : lambda m,qubits: m.q_xy(qubits[0]), # drive line of q0 
    "d1"   : lambda m,qubits: m.q_xy(qubits[1]), # drive line of q1 
    "d2"   : lambda m,qubits: m.q_xy(qubits[2]), # drive line of q2 
    "d3"   : lambda m,qubits: m.q_xy(qubits[3]), # drive line of q3 
    "z0"   : lambda m,qubits: m.q_zl(qubits[0]), # z line  line of q0 
    "z1"   : lambda m,qubits: m.q_zl(qubits[1]), # z line  line of q1 
    "z2"   : lambda m,qubits: m.q_zl(qubits[2]), # z line  line of q2 
    "z3"   : lambda m,qubits: m.q_zl(qubits[3]), # z line  line of q3 
    "p0"   : lambda m,qubits: m.q_pl(qubits[0]), # probe z line  of q0 
    "p1"   : lambda m,qubits: m.q_pl(qubits[1]), # probe z line  of q1 
    "p2"   : lambda m,qubits: m.q_pl(qubits[2]), # probe z line  of q2 
    "p3"   : lambda m,qubits: m.q_pl(qubits[3]), # probe z line  of q3 
    "zc01" : lambda m,qubits: m.qqcl(qubits[0],qubits[1]), # coupler between q0 q1 
    "zc12" : lambda m,qubits: m.qqcl(qubits[1],qubits[2]), # coupler between q1 q2 
    "zc02" : lambda m,qubits: m.qqcl(qubits[0],qubits[2]), # coupler between q0 q2 
    "zc03" : lambda m,qubits: m.qqcl(qubits[0],qubits[3]), # coupler between q0 q3 
    "zc13" : lambda m,qubits: m.qqcl(qubits[1],qubits[3]), # coupler between q1 q3 
    "zc23" : lambda m,qubits: m.qqcl(qubits[2],qubits[3]) # coupler between q2 q3 
  }; 
LookUpKeys= QubitLinesLookUp.keys() ;


class Moderator:
  """
    Motivation:
      Activly , case specificly  , keyword specificly
      handle connections , mappings , topological relations 
      dirty handedly using keywords DANGEROUSLY in code
    methods:
      __init__ :
        takes a file name that stores a json file , 
        in this json file has a key "MODERATOR"
      sq : returns string of qubit names,weather input is integer or string
      sc : returns string of coupler names,weather input is integer or string
      q  : returns qubit info 
      c  : returns coupler info 
      q_xy  : returns qubit xy line
      q_zl  : returns qubit z line  
      q_pl  : returns qubit probe line 
      q_lo  : returns qubit xy local source addr
      q_lf  : returns qubit xy local source freq  addr
      q_lp  : returns qubit xy local source power  addr
      c_n0  : returns coupler first neighbor
      c_n1  : returns coupler secound neighbor
      c_zl  : returns coupler z line  
      c_qqc : returns coupler for 2 qubits  
      c_qqcl : returns z line of coupler for 2 qubits  
  """
  __maj_type__="moderator" ;
  def __init__( self , fname_):
    if(isinstance(fname_ ,dict)) : M  = fname_ ; 
    else : M = rwj.read(fname_)["MODERATOR"];
    self.QUBITS =M["QUBITS"]  ; 
    self.COUPLERS =M["COUPLERS"]  ; 
    self.qcmap={};
    for cplr_k in self.COUPLERS:
      cplr = self.COUPLERS[cplr_k];
      self.qcmap[cplr["n0"] +"-"+ cplr["n1"]] = cplr_k;
      self.qcmap[cplr["n1"] +"-"+ cplr["n0"]] = cplr_k;

  def sq(self, qb_):
    if(int == type(qb_)): qb = "q"+str(qb_);
    elif(str==type(qb_)) : qb = qb_ ; 
    else: raise Exception("Type missmatch for {}".format(qb_));
    return qb ;
  
  def sc(self, c_):
    if(int == type(c_)): c = "c"+str(c_);
    elif(str==type(c_)) : c = c_ ; 
    else: raise Exception("Type missmatch for {}".format(c_));
    return c ;

  def q(self,qb_): return self.QUBITS[self.sq(qb_)];
  def c(self,c_):  return self.COUPLERS[self.sc(c_)];
  def q_xy(self,qb_): return self.q(qb_)["xy"];
  def q_zl(self,qb_): return self.q(qb_)["z"];
  def q_pl(self,qb_): return self.q(qb_)["p"];
  def q_lo(self,qb_): return self.q(qb_)["lo"];
  def q_lf(self,qb_): return self.q(qb_)["lf"];
  def q_lp(self,qb_): return self.q(qb_)["lp"];
  def c_n0(self, c_): return self.c(c_)["n0"];
  def c_n1(self, c_): return self.c(c_)["n1"];
  def c_zl(self, c_): return self.c(c_)["zc"];
  def qqc(self,qb1_,qb2_):return self.qcmap[self.sq(qb1_)+"-"+self.sq(qb2_)];
  def qqcl(self,qb1_,qb2_):return self.c_zl(self.qqc(qb1_ , qb2_));
  def line(self,l,qubits) : return QubitLinesLookUp[l](self,qubits) ; 
   
def is_moderator(m): 
  return (hasattr(m,"__maj_type__") and ( getattr(m,"__maj_type__")== "moderator") ) ; 




