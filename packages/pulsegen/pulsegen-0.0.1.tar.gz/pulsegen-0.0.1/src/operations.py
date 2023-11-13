
def fill(C , nq  , I  )   :
    for U in C : 
        check_list = [True] * nq ; 
        for G in U : 
            if(G.__nq__== 1 ) : 
                check_list[G.q] = False; 
            elif(G.__nq__== 2 ) : 
                check_list[G.q1] = False; 
                check_list[G.q2] = False; 
        for i,v in enumerate(check_list): 
            if(v) : U.append(I(i)); 
    return C ; 

def fill_selection(C , l  , I  )   :
    for U in C : 
        check_set = set(l); 
        for G in U : 
            if(G.__nq__== 1 ) : 
                check_set.discard(G.q) ; 
            elif(G.__nq__== 2 ) : 
                check_set.discard(G.q1); 
                check_set.discard(G.q2); 
        for i in check_set: 
            U.append(I(i)); 
    return C ; 



def drag_detuning_or_vz(filled_C , ddct ) : 
    for U in filled_C: 
        for G in U : 
            if(G.__nq__ ==1 ) : 
                G.kwds["drag_detuning"] = 0 ; 
                G.kwds["extra_vz"] = 0 ; 
                
        for i,tG in enumerate(U):
            
            if(tG.__mnr_type__ == "I" ) : 
                tgkw = "extra_vz" ; srckw = "vz";  
            else :
                tgkw = "drag_detuning" ;srckw = "drag_detuning"; 
            for j,cG in enumerate(U) :
                if(cG.__mnr_type__ in ["X","Y","mX","mY"]) : 
                    tG.kwds[tgkw]+=ddct[srckw][0][cG.q][tG.q] ; 
                elif(cG.__mnr_type__ in ["X2","Y2","mX2","mY2"]) : 
                    tG.kwds[tgkw]+=ddct[srckw][1][cG.q][tG.q] ; 
    return filled_C ; 


    
                    
                    
                    
                    
                