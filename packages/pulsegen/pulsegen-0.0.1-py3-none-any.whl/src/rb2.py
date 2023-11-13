import numpy as np;
import NLab.Utils.common as cm ;  cm.rl(cm);
import PulseGen.gates ; cm.rl(PulseGen.gates) ;  from PulseGen.gates import *
pi = np.pi ;
import PulseGen.rb as rb ; cm.rl(rb) ; 
import pickle;
import pathlib;
THIS_DIR=str(pathlib.Path(__file__).parent);
##

num_I  = np.matrix([ [ 1 , 0 ] , [0 , 1] ] ,dtype=np.complex128) ; 
num_sx = np.matrix([ [ 0 , 1 ] , [1 , 0] ] ,dtype=np.complex128) ; 
num_sy = np.matrix([ [ 0 ,-1j] , [1j ,0] ] ,dtype=np.complex128) ; 
num_sz = np.matrix([ [ 1 , 0 ] , [0 ,-1] ] ,dtype=np.complex128) ; 

def kron(A,B):return np.kron(A,B);

def round(A) : return np.round(A, decimals=4);

def norm(X): return X / abs(X);

def diff(A,B):
  rank = len(A) ;
  return   abs(2 * np.trace(A *B.H) / rank) -1  ;

def same(A,B): return abs( diff(A,B) - 1 )< 0.001;

def num_op(angle , _axis_ ):
  """
    here difines some numeric operators
  """
  axis_ = np.array(_axis_);
  axis = axis_ / np.sqrt(np.sum(axis_**2) )
  return num_I*np.cos(angle/2) - 1j *np.sin(angle/2) * (axis[0]*num_sx + axis[1]*num_sy + axis[2]*num_sz) ;


def copy_U(U_ ,q=None):
  U = [];
  for g in U_:
    gg = g.copy();
    if(gg.nq()==1 and None!=q): gg.q= q ;
    U.append(gg);
  return U ;

def apply_U(U_ , q0 , q1):
  U = [];
  for g in U_:
    gg = g.copy();
    if(gg.nq()==1):
      if(gg.q==-1) : gg.q=q0;
      elif(gg.q==-2) : gg.q=q1; 
    if(gg.nq()==2): 
      gg.q1=q0; gg.q2=q1; 
    U.append(gg);
  return U ;

def copy_C(C_ , q=None):
  C =[] ;
  for u in C_ : C.append(copy_U(u ,q));
  return C;

def apply_C(C_ , q0,q1):
  C =[] ;
  for u in C_ : C.append(apply_U(u ,q0,q1));
  return C;

def merge_circ_front(C1_ , C2_):
  C = [] ;
  lc1 = len(C1_); lc2 = len(C2_);
  for i in range(max(lc1,lc2)):
    U = [] ;
    if(i < lc1): U+=C1_[i];
    if(i < lc2): U+=C2_[i];
    C.append(U) ;
  return C;

def merge_circ_back(C1_ , C2_):
    C = [] ;
    lc1 = len(C1_); lc2 = len(C2_);
    C1_.reverse();
    C2_.reverse();
    for i in range(max(lc1,lc2)):
        U = [] ;
        if(i < lc1): U+=C1_[i];
        if(i < lc2): U+=C2_[i];
        C.append(U) ;
    C1_.reverse();
    C2_.reverse();
    C.reverse(); 
    return C;


C1=[
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



C1_circ_tplt=[
   [[I(-1)]],                      #0
   [[X(-1)]],                      #1
   [[Y(-1)]],                      #2
   [[Y(-1) ], [X(-2)]],                 #3
   [[X2(-1)]],                     #4
   [[mX2(-1)]],                    #5
   [[Y2(-1)]],                     #6
   [[mY2(-1)]],                    #7
   [[mX2(-1) ],[Y2(-1) ],[X2(-1)]],           #8
   [[mX2(-1) ],[mY2(-1)],[X2(-1)]],           #9

   [[X(-1)], [mY2(-1)]] ,              #1-1
   [[X(-1)], [Y2(-1)]] ,               #11
   [[Y(-1)], [X2(-1)]] ,               #12
   [[Y(-1)], [mX2(-1)]] ,              #13
   [[X2(-1)] , [Y2(-1)] , [X2(-1)]] ,         #14
   [[mX2(-1)] , [Y2(-1)] , [mX2(-1)]] ,       #15

   [[Y2(-1)] ,  [X2(-1)]] ,            #16
   [[mX2(-1)] , [Y2(-1)]] ,           #17
   [[X2(-1)]  , [mY2(-1)]] ,           #18
   [[mY2(-1)] , [mX2(-1)]] ,          #19
   [[mX2(-1)] , [mY2(-1)]] ,          #2-1
   [[mY2(-1)] , [X2(-1)]] ,           #21
   [[Y2(-1)] , [mX2(-1)]] ,           #22
   [[X2(-1)] , [Y2(-1)]] ,            #23
]; 



num_Y = num_op( pi , (0,1,0)) ; 
num_mY2 = num_op( -pi/2 , (0,1,0)) ; 
num_Y2 = num_op( pi/2 , (0,1,0)) ; 

num_mX2 = num_op( -pi/2 , (1,0,0)) ; 
num_X2 = num_op( pi/2 , (1,0,0)) ; 


S1 = [
  num_I ,
  num_X2 @ num_Y2 ,
  num_mY2 @ num_mX2 ,
]

S1_gate = [
  [[I(-1)] ] ,
  [[Y2(-1) ] , [X2(-1)] ],
  [[mX2(-1)] , [mY2(-1)] ],
]

S1x2 =  [
  num_X2  ,
  num_X2 @ num_Y2 @ num_X2,
  num_mY2
]

S1x2_gate = [
  [ [ X2(-1) ]] ,
  [ [ X2(-1) ] , [Y2(-1)] , [X2(-1)] ],
  [ [ mY2(-1)] ],
]

S1y2 = [
    num_Y2,
    num_X2 @ num_Y ,
    num_X2 @ num_mY2 @ num_mX2
]

S1y2_gate = [
    [[ Y2(-1) ]] ,
    [[ Y(-1) ] , [X2(-1) ] ],
    [[ mX2(-1)] , [mY2(-1)] ,[X2(-1) ] ],
]


num_CZ = np.matrix([
    [ 1, 0 , 0 , 0 ] ,
    [ 0, 1 , 0 , 0 ] ,
    [ 0, 0 , 1 , 0 ] ,
    [ 0, 0 , 0 , -1] ,
  ]  ,dtype=np.complex128
  ) ;

num_CNOT = np.matrix([
    [ 1, 0 , 0 , 0 ] ,
    [ 0, 1 , 0 , 0 ] ,
    [ 0, 0 , 0 , 1 ] ,
    [ 0, 0 , 1 , 0] ,
  ]  ,dtype=np.complex128
  ) ;

CNOT_circ = [
    [mY2(-2)] ,
    [CZ(-1,-2)] ,
    [Y2(-2)]
  ]

num_iSWAP = np.matrix([
    [ 1, 0 , 0 , 0 ] ,
    [ 0, 0 , 1j , 0 ] ,
    [ 0, 1j , 0 , 0 ] ,
    [ 0, 0 , 0 , 1] ,
  ]  ,dtype=np.complex128
  ) ;

iSWAP_circ = [
  [mY2(-1) , mX2(-2)]    ,
  [CZ(-1,-2)]    ,
  [Y2(-1) , mX2(-2)]    ,
  [CZ(-1,-2)]    ,
  [Y2(-1) , X2(-2)]    ,
]

num_SWAP = np.matrix([
    [ 1, 0 , 0 , 0 ] ,
    [ 0, 0 , 1 , 0 ] ,
    [ 0, 1 , 0 , 0 ] ,
    [ 0, 0 , 0 , 1] ,
  ]  ,dtype=np.complex128
  ) ;

SWAP_circ = [
  [ mY2(-2)] ,
  [ CZ(-1,-2)] ,
  [ mY2(-1) , Y2(-2)],
  [ CZ(-1,-2)] ,
  [ Y2(-1) , mY2(-2)],
  [ CZ(-1,-2)] ,
  [ Y2(-2)] ,
];

C2 = [];
C2_circ_tplt = [];

# the simples element
for i,ci in enumerate(C1):
  for j,cj in enumerate(C1):
    C2.append(kron(ci,cj))
    C2_circ_tplt.append( merge_circ_front (
      copy_C(C1_circ_tplt[i] , q = -1),
      copy_C(C1_circ_tplt[j] , q = -2)
    ));

# CNOT-like class
#for i,ci in enumerate(C1):
#  for j,cj in enumerate(C1):
#    for m,sm in  enumerate( S1):
#      for n,sn in  enumerate( S1):
#        C2.append(kron( sm , sn) @ num_CNOT @ kron(ci , cj) ) ;
#        Crct = [];
#        # old version P12 of 1402.4848.pdf
#
#        Crct += merge_circ_front (
#          copy_C(C1_circ_tplt[i] , q = 0),
#          copy_C(C1_circ_tplt[j] , q = 1)
#        );
#
#        Crct += copy_C(CNOT_circ);
#
#        Crct += merge_circ_front (
#          copy_C(S1_gate[m] , q = 0),
#          copy_C(S1_gate[n] , q = 1)
#        );
#
#        C2_circ_tplt.append(
#          Crct
#        )

# absorbed version
for i,ci in enumerate(C1):
  for j,cj in enumerate(C1):
    for m,sm in  enumerate( S1):
      for n,sn in  enumerate( S1y2 ):
        C2.append(kron( sm , sn) @ num_CZ @ kron(ci , cj) ) ;
        Crct = [];
        # old version P12 of 1402.4848.pdf
        Crct += merge_circ_front (
          copy_C(C1_circ_tplt[i] , q = -1),
          copy_C(C1_circ_tplt[j] , q = -2)
        );
        Crct += [[CZ(-1,-2)]];
        Crct += merge_circ_front (
          copy_C(S1_gate[m] , q = -1),
          copy_C(S1y2_gate[n] , q = -2)
        );
        C2_circ_tplt.append(
          Crct
        )


# iSWAP-like class :
#for i,ci in enumerate(C1):
#  for j,cj in enumerate(C1):
#    for m,sm in  enumerate( S1):
#      for n,sn in  enumerate( S1):
#        C2.append(kron( sm , sn) @ num_iSWAP @ kron(ci , cj) ) ;
#        Crct = [];
#        Crct += merge_circ_front (
#          copy_C(C1_circ_tplt[i] , q = 0),
#          copy_C(C1_circ_tplt[j] , q = 1)
#        );
#
#        Crct += copy_C(iSWAP_circ);
#
#        Crct += merge_circ_front (
#          copy_C(S1_gate[m] , q = 0),
#          copy_C(S1_gate[n] , q = 1)
#        );
#
#        C2_circ_tplt.append(
#          Crct
#        )

# absorbed version
for i,ci in enumerate(C1):
  for j,cj in enumerate(C1):
    for m,sm in  enumerate( S1y2):
      for n,sn in  enumerate( S1x2):
        C2.append( kron(sm,sn) @ num_CZ @ kron( num_Y2 , num_mX2 ) @ num_CZ @ kron(ci , cj) ) ;
        Crct = [];
        Crct += merge_circ_front (
          copy_C(C1_circ_tplt[i] , q = -1),
          copy_C(C1_circ_tplt[j] , q = -2)
        );

        Crct += [[CZ(-1,-2)] , [Y2(-1) , mX2(-2)] ,[CZ(-1,-2)]];
        Crct += merge_circ_front (
          copy_C(S1y2_gate[m] , q = -1),
          copy_C(S1x2_gate[n] , q = -2)
        );

        C2_circ_tplt.append(
          Crct
        )

# SWAP-like class :  absorbed version
for i,ci in enumerate(C1):
  for j,cj in enumerate(C1):
     C2.append(num_SWAP @ kron( ci , cj)  ) ;
     Crct = []; 
     Crct += merge_circ_front (
       copy_C(C1_circ_tplt[i] , q = -1),
       copy_C(C1_circ_tplt[ rb.G_LUT[ j , 7 ] ]  , q = -2)
     ); 

     Crct += [[CZ(-1,-2)] , [mY2(-1) , Y2(-2)] , [CZ(-1,-2)],[Y2(-1) , mY2(-2)] , [CZ(-1,-2)] , [Y2(-2)]];

     C2_circ_tplt.append(
       Crct
     )


## matrix cross check very slow
#print("checking matrix");
#for i,ci in enumerate(C2):
#  print(i);
#  for j,cj in enumerate(C2):
#    if( i == j ) : assert( same(ci,cj) ) , "the element ({},{})".format(i,j) ;
#    else : assert( not same(ci,cj) ), "the element ({},{})".format(i,j) ;
#

## diagonal check
#for i,ci in enumerate(C2):
#  T = False;
#  for k in [0,1,2,3]:
#    if(abs(ci[k,0]) >0.01):
#      print(i, k);
#      T = True;
#      break;
#  assert(T),"ERRRRRRRRRRRRRROR"


## formalise and hash
def f(A):
  for k in [0 ,1, 2, 3] :
    if (abs(A[k,0] )> 0.01):
      return np.ndarray.astype(round(norm(A[k,0]).conjugate() * A),np.complex64);
  assert(True), "Error on fomalise"

def np_hashable(A):
  return tuple(np.ndarray.flatten(A.A));

C2_DICT ={};
for i,ci in enumerate(C2):
  C2_DICT[np_hashable(f(ci))] = i;


##########################################
############   Making LUT   ##############
##########################################
# lC2 = len(C2)   ;
# RB2_LUT = np.zeros((lC2, lC2) , dtype = np.short)   ;
# for i,ci in enumerate(C2):
#  print(i);
#  for j,cj in enumerate(C2):
#    RB2_LUT[i,j] = C2_DICT[np_hashable(f( cj @ ci))]
# pickle.dump(RB2_LUT , open("RB2_LUT.pkl","wb"));
## loading
RB2_LUT_load =pickle.load(open(cm.os_slash(THIS_DIR) + "RB2_LUT.pkl","rb")); # the loaded LUT

# a random test
# C2_DICT[np_hashable(f(C2[2454] @ C2[4354]))]

# # figure out the inverse :
# lC2 = len(C2)   ;
# RB2_INV = np.zeros(lC2 , dtype = np.short)   ;
# for i,ci in enumerate(C2):
#  RB2_INV[i] = C2_DICT[np_hashable(f(np.linalg.inv(ci)))]
# pickle.dump(RB2_INV , open(cm.os_slash(THIS_DIR)+"RB2_INV.pkl","wb"));

## load it
RB2_INV_load =pickle.load(open(cm.os_slash(THIS_DIR)+"RB2_INV.pkl","rb")); # the loaded LUT

##############################################
################## apply #####################
##############################################

lC2 = len(C2)   ;
def add_rec(gnums):
  # step 1 find the last element
  TG = 0 ;
  for g in gnums:
    TG = RB2_LUT_load[TG , g%lC2 ];  #TODO possible order issue
  LG = RB2_INV_load[TG];
  if(LG!=0):return list(gnums) + [LG];
  else :return list(gnums)+[];


def gen_circ( q0, q1, ODR_):
  ODR =  add_rec(ODR_);
  CIRC= [];
  for gn in ODR:
    CIRC += apply_C(C2_circ_tplt[gn] ,q0 ,q1);
  return CIRC;

#Z = gen_circ(2,5,[1,2,3,4]);

if __name__ == "__main__":
  print(len(C2))
