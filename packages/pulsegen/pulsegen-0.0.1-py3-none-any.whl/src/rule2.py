



def apply_sub(rules, gate) :
  R= {} ; 
  return R ; 



def apply(rules, circuit , qubit_info , line_info ,extra):      
  lR = []; 
  for U in circuit : 
    RES1=  [] ; 
    for G in U : 
      R= [];  
      if(isinstance(G,list) or isinstance(G,tuple)): 
        for sG in G:  R.apepnd(apply_sub(rules, sG))  ; 
      else :  R.append(apply_sub(rules, G)); 
     

