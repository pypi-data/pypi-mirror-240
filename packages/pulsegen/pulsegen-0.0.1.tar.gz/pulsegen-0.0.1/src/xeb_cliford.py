import numpy as np
import random as rnd
import PulseGen.gates as GATE;
pi = np.pi
num_I  = np.matrix([ [ 1 , 0 ] , [0 , 1] ] ,dtype=np.complex128) ; 
num_sx = np.matrix([ [ 0 , 1 ] , [1 , 0] ] ,dtype=np.complex128) ; 
num_sy = np.matrix([ [ 0 ,-1j] , [1j ,0] ] ,dtype=np.complex128) ; 
num_sz = np.matrix([ [ 1 , 0 ] , [0 ,-1] ] ,dtype=np.complex128) ; 

def num_op(angle , _axis_ ):
  """
    here difines some numeric operators
  """
  axis_ = np.array(_axis_);
  axis = axis_ / np.sqrt(np.sum(axis_**2) )
  return num_I*np.cos(angle/2) - 1j *np.sin(angle/2) * (axis[0]*num_sx + axis[1]*num_sy + axis[2]*num_sz) ;

def tensor(*gates):
    if len(gates)==1:
        return gates[0]
    else:
        gate_kron=gates[-1]
        for gate in gates[-2::-1]:
            gate_kron = np.kron(gate,gate_kron)
        return gate_kron


num_CZ = np.matrix([
    [ 1, 0 , 0 , 0 ] ,
    [ 0, 1 , 0 , 0 ] ,
    [ 0, 0 , 1 , 0 ] ,
    [ 0, 0 , 0 , -1] ,
  ]  ,dtype=np.complex128
  ) 

# I = num_op(0 ,  (1,0,0)) 
# X = num_op(np.pi ,  (1,0,0)) 
# Y = num_op(np.pi ,  (0,1,0)) 
# W = num_op(np.pi ,  (1,1,0)) 
# mX = num_op(np.pi ,  (-1,0,0)) 
# mY = num_op(np.pi ,  (0,-1,0)) 
# mW = num_op(np.pi ,  (-1,-1,0)) 
# X2 = num_op(np.pi/2 ,  (1,0,0)) 
# Y2 = num_op(np.pi/2 ,  (0,1,0)) 
# W2 = num_op(np.pi/2 ,  (1,1,0)) 
# mX2 = num_op(np.pi/2 ,  (-1,0,0)) 
# mY2 = num_op(np.pi/2 ,  (0,-1,0)) 
# mW2 = num_op(np.pi/2 ,  (-1,-1,0)) 
# sqg_set=[GATE.X2,GATE.mX2,GATE.Y2,GATE.mY2,GATE.W2,GATE.mW2]
# sqg_unitary=[X2,mX2,Y2,mY2,W2,mW2]

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
   [GATE.mX2 , GATE.mY2] ,          #21
   [GATE.mY2 , GATE.X2] ,           #20
   [GATE.Y2 , GATE.mX2] ,           #22
   [GATE.X2 , GATE.Y2] ,           #23
]; 


def max_len_in_list(list1):
    max_len = 0
    for list2 in list1:
        max_len=max(max_len,len(list2))
    return max_len

def append_to_seq(sequence,gates_list):
    qnum=len(gates_list)
    depth = len(gates_list[0])
    for d in range(depth):
        cir = []
        for q in range(qnum):
            cir.append(gates_list[q][d])
        sequence.append(cir)

def random_sqg(sqg_set,qlist):
    mq_list=[]
    for q in qlist:
        sqg_list=[]
        gset = rnd.choice(sqg_set)
        for g in gset:
            sqg_list.append( g(int(q)) )
        mq_list.append(sqg_list)
    maxlen = max_len_in_list(mq_list)
    for i,q in enumerate(qlist):
        if len(mq_list[i])<maxlen:
            mq_list[i].append(GATE.I(int(q)))
    return mq_list

def xeb_gates(target_gate,cycle,seed,qlist=[0,1,2,3],use_cz=False,sqg_set=Gt):
    rnd.seed(seed)
    sequence = []
    # sequence.append(random_sqg(sqg_set,qlist) )
    append_to_seq(sequence,random_sqg(sqg_set,qlist))
    for _ in range(int(cycle)):
        sequence.append(target_gate[0])
        # sequence.append(random_sqg(sqg_set,qlist) )
        append_to_seq(sequence,random_sqg(sqg_set,qlist))
        if use_cz:
            pass
    return sequence

def random_sqg_unitary(sqg_unitary,qlist):
    sqg_list=[]
    for _ in qlist:
        sqg_list.append( rnd.choice(sqg_unitary) )
    return tensor(*sqg_list)

def xeb_unitary(target_unitary,cycle,seed,qlist,use_cz=False,sqg_unitary=Gp):
    rnd.seed(seed)
    U = random_sqg_unitary(sqg_unitary,qlist)

    for _ in range(int(cycle)):
        U = target_unitary @ U
        U = random_sqg_unitary(sqg_unitary,qlist) @ U
        if use_cz:
            pass
    psi0 = np.zeros(2**len(qlist),dtype=complex)
    psi0[0] = 1.0 + 0j
    psif = np.array(U @ psi0)[0]
    return np.abs(psif)**2 

def xeb_pc(data,target_unitary,cycle,seed_list,qlist,use_cz=False,sqg_unitary=Gp):
    """
    data_shape:[repeat_times, 2**qnum]
    """
    psif_ideal_collec=np.array([])
    for seed in seed_list:
        psif_ideal = xeb_unitary(target_unitary,cycle,seed,qlist,use_cz=False,sqg_unitary=sqg_unitary)
        psif_ideal_collec = np.append(psif_ideal_collec,psif_ideal)
    # print(psif_ideal_collec)
    psif_ideal_collec= psif_ideal_collec.reshape(len(seed_list),len(psif_ideal))

    state_num = 2**(len(qlist))

    fm=0
    ft=-1
    for i in range(len(seed_list)):
        fm += sum( (state_num * psif_ideal_collec[i,:] - 1) * data[i,:] ) /  len(seed_list)
        ft += state_num * sum( (psif_ideal_collec[i,:])**2) /  len(seed_list)
    return fm/ft,psif_ideal_collec
