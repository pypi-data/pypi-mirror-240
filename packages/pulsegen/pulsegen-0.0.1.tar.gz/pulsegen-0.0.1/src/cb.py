from typing import Sequence
import numpy as np
import random as rnd

from numpy.lib.shape_base import _make_along_axis_idx
import PulseGen.gates as GATE;
import copy

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

U_I = num_op(0 ,  (1,0,0)) 
U_X = num_op(np.pi ,  (1,0,0)) 
U_Y = num_op(np.pi ,  (0,1,0))
U_Z = num_op(np.pi, (0, 0, 1))
U_mX = num_op(np.pi ,  (-1,0,0)) 
U_mY = num_op(np.pi ,  (0,-1,0))
U_X2 = num_op(np.pi/2 ,  (1,0,0)) 
U_Y2 = num_op(np.pi/2 ,  (0,1,0))
U_mX2 = num_op(np.pi/2 ,  (-1,0,0)) 
U_mY2 = num_op(np.pi/2 ,  (0,-1,0))

# Basis gates set
basis_gates_set = [GATE.Y2, GATE.mX2, GATE.I, GATE.X]
basis_unitary = [U_Y2, U_mX2, U_I, U_X]

def all_basis(idx, temp_list, qlist, basis_list):
	if idx == len(qlist):
		new_list = copy.deepcopy(temp_list)
		basis_list.append(new_list)
		return
	for gate in basis_gates_set:
		a = gate(int(qlist[idx]))
		temp_list.append(a)
		all_basis(idx + 1, temp_list, qlist, basis_list)
		temp_list.pop()


def get_basis(qlist, K = -1, seed = 10):
	rnd.seed(10)
	basis_list = []
	all_basis(0, [], qlist, basis_list)
	if K == -1:
		return basis_list
	else:	
		rnd.shuffle(basis_list)
		return basis_list[:K]


def get_basis_dag(b):
	"""
	b: a basis gate list 
	"""
	basis_dag_list = []
	for gate in b:
		if gate.__mnr_type__ == "Y2":
			basis_dag_list.append(GATE.mY2(gate.q))
		elif gate.__mnr_type__ == "mX2":
			basis_dag_list.append(GATE.X2(gate.q))
		elif gate.__mnr_type__ == "I":
			basis_dag_list.append(GATE.I(gate.q))
		elif gate.__mnr_type__ == "X":
			basis_dag_list.append(GATE.mX(gate.q))
		else:
			raise ValueError("Wrong basis gate!")
	return basis_dag_list	


pauli_gates_set = [GATE.X, GATE.Y, GATE.Z, GATE.I]
pauli_unitary = [U_X, U_Y, U_Z, U_I]

def random_pauli_gate(qlist):
	pauli_list = []
	for q in qlist:
		pauli_list.append(rnd.choice(pauli_gates_set)(int(q)))
	return pauli_list



def cb_seq(qlist, seed, target, m, K=-1, b=0):
	"""
	m: the cycle length
	b: basis changing gates
	"""
	B = get_basis(qlist, K=K)
	rnd.seed(seed)
	sequence = []
	sequence.append(B[b])
	sequence.append(random_pauli_gate(qlist))
	for _ in range(m):
		sequence.append(target)
		sequence.append(random_pauli_gate(qlist))
	sequence.append(get_basis_dag(B[b]))
	return sequence

# def cb_unitary(seed)


