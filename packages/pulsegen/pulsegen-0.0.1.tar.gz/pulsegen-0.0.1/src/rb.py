import NLab.Utils.common as cm ;  cm.rl(cm);
import PulseGen.gates as GATE; cm.rl(GATE) ;
import PulseGen.create_random_list as crlist; cm.rl(crlist) ;
import numpy as np;
pi = np.pi ;

# cliford group related
# this is copied from 0F_UCSB_Chen2018

I  = np.matrix([ [ 1 , 0 ] , [0 , 1] ] ,dtype=np.complex128) ;
sx = np.matrix([ [ 0 , 1 ] , [1 , 0] ] ,dtype=np.complex128) ;
sy = np.matrix([ [ 0 ,-1j] , [1j ,0] ] ,dtype=np.complex128) ;
sz = np.matrix([ [ 1 , 0 ] , [0 ,-1] ] ,dtype=np.complex128) ;

def num_op(angle , _axis_ ):
  axis_ = np.array(_axis_);
  axis = axis_ / np.sqrt(np.sum(axis_**2) )
  # Quantum Mechaincs J.J.Sakurai
  return I*np.cos(angle/2) - 1j *np.sin(angle/2) * (axis[0]*sx + axis[1]*sy + axis[2]*sz) ;


Gp=[
    num_op(0 ,  (1,0,0)) ,
    num_op(pi , (1,0,0)) ,
    num_op(pi , (0,1,0)) ,
    num_op(pi , (0,0,1)) ,

    num_op(pi/2 , (1,0,0)) ,
    num_op(pi/2 , (-1,0,0)) ,
    num_op(pi/2 , (0,1,0)) ,
    num_op(pi/2 , (0,-1,0)) ,
    num_op(pi/2 , (0,0,1)) ,
    num_op(pi/2 , (0,0,-1)) ,

    num_op(pi , (1,0,1)) ,
    num_op(pi , (-1,0,1)) ,
    num_op(pi , (0,1,1)) ,
    num_op(pi , (0,-1,1)) ,
    num_op(pi , (1,1,0)) ,
    num_op(pi , (1,-1,0)) ,

    num_op(2*pi/3 , (1,1,1)) ,
    num_op(2*pi/3 , (-1,1,1)) ,
    num_op(2*pi/3 , (1,-1,1)) ,
    num_op(2*pi/3 , (-1,-1,1)) ,
    num_op(-2*pi/3 , (1,1,1)) ,
    num_op(-2*pi/3 , (-1,1,1)) ,
    num_op(-2*pi/3 , (1,-1,1)) ,
    num_op(-2*pi/3 , (-1,-1,1))
]; 

def diff(op1 , op2 ) :
  R = (op1 ) @ (op2.H) ; 
  return  np.sqrt(
    (np.abs(R[0,0])-1)**2 + (np.abs(R[1,1])-1)**2 +np.abs(R[0,0]-R[1,1])**2
      + np.abs(R[0,1] )**2 + np.abs(R[1,0] )**2
  ) ;

def same(op1 , op2):
  return diff(op1 , op2) < 0.001;

def getLUT():
  D = [];
  for g1 in Gp:
    Dr = [] ;
    for g2 in Gp:
      op =g2 @ g1 ;
      for i,wich_e in enumerate(Gp):
        if(same(wich_e , op)):
          Dr.append(i);
          break ;
    D.append(Dr);
  Inv=  [] ;
  for rw in D:
    for i,g in enumerate(rw):
      if g == 0 : Inv.append(i);
  return np.array(D),Inv;


# globals:

SAMES = {
  "X" : GATE.mX , 
  "Y" : GATE.mY ,
}


G_LUT,G_INV= getLUT();
Gt=[
   [GATE.I],                       #0
   [GATE.X],                       #1
   [GATE.Y],                       #2
   [GATE.Y  , GATE.X],                #3

   [GATE.X2],                     #4
   [GATE.mX2],                    #5
   [GATE.Y2],                     #6
   [GATE.mY2],                    #7
   [GATE.mX2 ,GATE.Y2 , GATE.X2],          #8
   [GATE.mX2 , GATE.mY2,GATE.X2],          #9

   [GATE.X , GATE.mY2] ,             #10
   [GATE.X , GATE.Y2] ,              #11
   [GATE.Y , GATE.X2] ,              #12
   [GATE.Y , GATE.mX2] ,             #13
   [GATE.X2 , GATE.Y2 , GATE.X2] ,    #14
   [GATE.mX2 , GATE.Y2 , GATE.mX2] ,  #15

   [GATE.Y2 , GATE.X2] ,            #16
   [GATE.mX2 , GATE.Y2] ,           #17
   [GATE.X2 , GATE.mY2] ,           #18
   [GATE.mY2 , GATE.mX2] ,          #19
   [GATE.mX2 , GATE.mY2] ,          #20
   [GATE.mY2 , GATE.X2] ,           #21
   [GATE.Y2 , GATE.mX2] ,           #22
   [GATE.X2 , GATE.Y2] ,           #23
]; 


# defining the rb things :
def ran(seed:int ,  n:int , ceil_):
  l = crlist.RAND_LIST_SIZE;
  start = crlist.L[seed % l] % l;
  secs = [] ; 
  for i in range(n):
    secs.append( crlist.L[(start+i)%l] % ceil_ );
  return secs;

def get_recover(A):
  g = 0;# iterative group element
  for i in A :
    g=G_LUT[g][i] ; 
  return G_INV[g]

def join_circ(CC):
  C= [];
  for C_ in CC: C+=C_ ; 
  return C; 

def merge_circ_2(C1_,C2_ , back = True):
    """
      the option back indicates where this circuit is aligned,
      if back is True, the circuit is aligned at the end,
        which is used at the final joining of 2 circuits
      if back is False, the circuit is aligned at the front, 
        which is used at the Cliford element sub circuit alignment
    """
    C = []; 
    lc1 =  len(C1_) ; lc2 = len(C2_) ; 
    mx = max(lc1 , lc2) ; 
    if(back) : 
      C1_.reverse(); 
      C2_.reverse(); 
    for i in range(mx) : 
      U =[]; 
      if( i < lc1) :  U+=C1_[i] ; 
      if( i < lc2) :  U+=C2_[i] ; 
      C.append(U) ; 
    if(back) : 
      C1_.reverse(); 
      C2_.reverse(); 
      C.reverse(); 
    return C ; 



def merge_circ(CC, back:bool = True) : 
  """
    join multiple cicuit collections CC,
    if back is True, the circuit is aligned at the end,
      which is used at the final joining of 2 circuits
    if back is False, the circuit is aligned at the front, 
      which is used at the Cliford element sub circuit alignment
  """
  C = []; 
  lcs= [] ; 
  for C_ in CC: lcs.append(len(C_) ) ;  
  mx = np.max(lcs) ; 
  if(back) : 
    for C_ in CC: C_.reverse() ; 

  for i in range(mx) : 
    U =[]; 
    for j,C_ in enumerate(CC): 
      if( i < lcs[j] ) :  U+=C_[i] ; 
    C.append(U) ; 
  
  if(back) : 
    for C_ in CC: C_.reverse() ; 
    C.reverse(); 

  return C ; 

def element_wise_merge(CCs  , back  = True ) : 
  """
     takes in many collection of sub circuits
  """
  C= [] ; # return target circuit; 
  lCCs = [] ;  
  for CC in CCs: lCCs.append(len(CC)) ; 
  mx = np.max(lCCs) ; 
  if(back) : 
    for CC in CCs: CC.reverse() ; 
 
  CPCC = [] ; 
  for i in range(mx) : 
    PCC =[];  # parallel cicuit collection. 
    for j,CC in enumerate(CCs): 
      if( i < lCCs[j] ) :  PCC.append(CC[i]) ; 
    CPCC.append(PCC ) ; 

  if(back) : 
    for CC in CCs: CC.reverse() ;  
    CPCC.reverse() ; 
  
  C= [] ; 
  for PCC in CPCC : 
    C+= merge_circ(PCC, False);  

  return C; 




def raw_rb(gnums_, q0 , **kwds) :
  gnums = gnums_ + [get_recover(gnums_)] ; 
  circ_col = []; 
  for i,g in enumerate(gnums):
    odd = bool(i%2) ; 
    tC = Gt[g] ; 
    TC = [] ; 
    for gate in tC :
      gate_sel = gate ; 
      if(odd and gate.__mnr_type__ in SAMES)  : 
        gate_sel = SAMES[gate.__mnr_type__] ; 
      TC.append([gate_sel(q0,**kwds)]) ; 
    circ_col.append(TC) ; 
  return circ_col ; 

def rb(gnums_, q0 , **kwds) :
  return join_circ(raw_rb(gnums_, q0 , **kwds)) ; 

def raw_seed_rb(seed , n , q0 ,  interleave_gate_num = None , **kwds ) :
  """
    single qubit rb,
    generated a circuit that is ready to be computed
  """
  lgt = len(Gt)
  R_ = ran(seed,n,lgt); 
  if(None != interleave_gate_num and interleave_gate_num >= 0 ) : 
    R = []; 
    for e in R_ :  R.append(e) ; R.append(interleave_gate_num % lgt ); 
  else : R = R_ ; 
  return raw_rb(R ,q0 ,**kwds)  ; 

def seed_rb(seed , n , q0 ,  interleave_gate_num = None , **kwds ) :
  return join_circ(raw_seed_rb(seed , n , q0 ,  interleave_gate_num , **kwds)) ; 


def mul_seed_rb(params ,cliford_element_wise_align = False):
  """
    params is list of param  , 
    param is a dictionary , for example : 
    {"seed":5, "n":34,  "q":0 , "ign" : 4 , "kwds":{"width":10} } 
    ign stands for "interleave gate num", 
    ign and kwds are not compulsatory

    cliford_element_wise_align is the align of the circuit option ,
    if it was set to be true, then generated circuit will just align to "GATES".
    but if it was set True,  then they will align to each "CLIFORD GROUP ELEMENT", wich consist of multiple gates.
  """
  CCs = [];  # the collection of the sub circuits;  
  for param in params :
    CCs.append(
      raw_seed_rb(
        int(param["seed"]) , 
        max(1 , int( param["n"])) , 
        int(param["q"]) ,
        cm.dkd(param , "ign" , None ) , 
        **cm.dkd(param , "kwds" , {} ) , 
      ) 
    ); 
  if cliford_element_wise_align: 
    return element_wise_merge(CCs , False) ; 
  else : # here goes gate wise ; 
    Cs = [ join_circ(CC) for CC in CCs  ] ; 
    return merge_circ(Cs) ; 


# def RB(seed , n , q_list , kwds={} , interleave_gate = None) :
#   """
#     single qubit rb,
#     generated a circuit that is ready to be computed
#   """
#   A= []; 
#   Ge=ran(seed, n , len(Gt)); 
#   Ge.append(get_recover(Ge)); 
#   for a in Ge :
#     for G in Gt[a]:
#       temp=[]
#       for q in q_list:
#         temp.append( G(q,**kwds)  )
#       A.append(temp); 
#   return A; 




def plain_rb(_grums_ , q0 , **kwds) :
  gnums_ = list(_gnums_) ; 
  gnums = gnums_ + [get_recover(gnums_)] ; 
  circ = [] ;
  for  i, g in enumerate(gnums) :  circ.append([ Gt[g](q0 , **kwds) ]) ; 
  return circ ; 
