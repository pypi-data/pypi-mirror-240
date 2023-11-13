import random
import pickle
import pathlib  
import NLab.Utils.common as cm; 
fname =  cm.os_slash(str(pathlib.Path(__file__).parent.absolute())) + "randlist.pkl"; 

RAND_LIST_SIZE = 100_000;
def create_random():
  R = random.Random();
  L =  [] ;
  for i in range(RAND_LIST_SIZE) :
    L.append(R.randint(0,2**31));
  pickle.dump(L ,open(fname, "wb") )  ;


def load_random():
  return pickle.load(open(fname, "rb") )  ;


#create_random();
L =load_random();

