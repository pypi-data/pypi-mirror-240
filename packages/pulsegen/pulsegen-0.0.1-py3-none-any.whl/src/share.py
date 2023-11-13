import NLab.Utils.common as  cm ;  cm.rl(cm); 

# taking the key words
def u2split(k:str):
  ks = k.split("__");
  r = [] ; 
  for w in  ks: 
    if(""!=w):r.append(w) ; 
  return r; 


def join_kw(s:list=[]):
  ls = len(s) ;  r ="" ;  
  for i,w in enumerate(s) :
    r+=w; 
    if(ls-1 != i) : r+="__";
  return r; 


def catch(kwds:dict , w:str):
  kw = {};
  for k,v in kwds.items():
    ks = u2split(k);
    if(len(ks)==1): kw[k]=v ;
    elif( ks[0] == w or ks[0] == 'X' ): kw[join_kw(ks[1:])] = v ;  
  return kw ;


def get_len(pdt ) : 
  return  cm.dkd(pdt , "width" ,  0) + cm.dkd(pdt , "plateau" ,  0) ; 
