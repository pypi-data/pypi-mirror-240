import NLab.Utils.common as  cm ;  cm.rl(cm);

# 1 qubit gate template
class I:
  __maj_type__ = "gate";
  __mnr_type__='I';
  __nq__=1;
  def __init__(self, q_, **kwds_):
    #assert(q_ >= 0) ; # qubit index must be unsigned
    self.q = q_ ; self.pos = None  ;
    self.kwds=kwds_;
  def __rep__(self):
    return self.__str__();
  def __str__(self):
    if(self.kwds!={}):
      return "{}<q{},kwds={}>".format( self.__mnr_type__, self.q , self.kwds) ;
    else:
      return "{}<q{}>".format( self.__mnr_type__, self.q) ;
  def nq(self):return self.__nq__;
  def gt(self):return self.__mnr_type__;
  def qubits(self): return [self.q];
  def copy(self) :return type(self)(self.q , **self.kwds);

# 2 qubit gate template
class I2(I):
  __mnr_type__='I2'; 
  __nq__=2;
  def __init__(self, q1_ , q2_, **kwds_):
    #assert(q1_ >= 0) ;
    #assert(q2_ >= 0) ; # qubit index must be unsigned
    self.q1=q1_ ;
    self.q2=q2_ ;
    self.kwds=kwds_;
  def __str__(self):
    if(self.kwds!={}):
      return "{}<q{},q{},kwds={}>".format(
        self.__mnr_type__, self.q1,self.q2 , self.kwds) ;
    else:
      return "{}<q{},q{}>".format( self.__mnr_type__, self.q1, self.q2) ;
  def qubits(self): return [self.q1 , self.q2];
  def copy(self) :return type(self)(self.q1 , self.q2  , **self.kwds);

# 3 qubit gates
class I3(I):
  __mnr_type__='I3'; 
  __nq__=3; 
  def __init__(self, q1_ , q2_,  q3_, **kwds_):
    #assert(q1_ >= 0) ;
    #assert(q2_ >= 0) ;
    #assert(q3_ >= 0) ; # qubit index must be unsigned
    self.q1=q1_ ; 
    self.q2=q2_ ; 
    self.q3=q2_ ; 
    self.kwds=kwds_; 
  def __str__(self):
    if(self.kwds!={}):
      return "{}<q{},q{},q{},kwds={}>".format(
        self.__mnr_type__, self.q1,self.q2 ,self.q3 , self.kwds) ;
    else:
      return "{}<q{},q{},q{}>".format( self.__mnr_type__, self.q1, self.q2, self.q3) ;
  def qubits(self): return [self.q1 , self.q2 , self.q3];
  def copy(self) :return type(self)(self.q1 , self.q2 , self.q3 , **self.kwds);

# helper functions
def is_gate(a):
  return ( (hasattr(a,"__maj_type__") and getattr(a,"__maj_type__")=="gate") ) ;

def is_gate_a(a,w):
  return (
      is_gate(a)
      and hasattr(a,"__mnr_type__")
      and getattr(a,"__mnr_type__")==w
    ) ; 

# enumeartion of the gates
# 1-qubit gates
class X(I):      __mnr_type__="X";
class X2(I):     __mnr_type__="X2";
class Y(I):      __mnr_type__="Y";
class Y2(I):     __mnr_type__="Y2";
class mX(I):     __mnr_type__="mX";
class mX2(I):    __mnr_type__="mX2";
class mY(I):     __mnr_type__="mY";
class mY2(I):    __mnr_type__="mY2";
class W(I):     __mnr_type__="W";
class mW(I):    __mnr_type__="mW";
class W2(I):     __mnr_type__="W2";
class mW2(I):    __mnr_type__="mW2";
class Z(I):     __mnr_type__="Z";
class H(I):     __mnr_type__="H";
class M(I):     __mnr_type__="M";
class R(I):     __mnr_type__="R";

class M01(I):     __mnr_type__="M01";
class M12(I):     __mnr_type__="M12";
class M23(I):     __mnr_type__="M23";


# 2-qubit gates

class CZ(I2):       __mnr_type__="CZ";
class CZnz(I2):     __mnr_type__="CZnz"; 
class CZnz1(I2):     __mnr_type__="CZnz1"; 
class CZnz2(I2):     __mnr_type__="CZnz2"; 
class CPHASE(I2):   __mnr_type__="CPHASE";


class CNOT(I2):     __mnr_type__="CNOT";
class SWAP(I2):     __mnr_type__="SWAP";
class ISWAP(I2):    __mnr_type__="ISWAP";
class FSIM(I2):     __mnr_type__="FSIM";

# 3-qubit gates
class CSWAP(I3):    __mnr_type__="CSWAP";
