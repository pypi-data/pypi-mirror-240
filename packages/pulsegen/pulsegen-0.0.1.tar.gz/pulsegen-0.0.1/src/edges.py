import numpy as np 

def fr(w , max_ ,min_ ) :
  return max(min(w , max_),min_) ;

def nr(w):
  return ( w - np.min(w) ) / ( np.max(w) - np.min(w) );


def mn(A,B) :
  return min(A,B) ,max(A,B) ;

def seige(x ,a ,b ,w): return  np.pi*(x*(b - a) / w + (b + a -1)/2) ;  

def sine_edge(X , x0 , w_ = 1e-10, a_ = 0 , b_ = 1 ) :
  w = max(1e-10 , w_)  ;
  a,b=mn(a_ , b_ ); 
  l,r=mn( 
    np.sin(seige(-w/2, a,b,w)), 
    np.sin(seige(w/2 , a,b,w))  
  ); 
  Y = np.zeros(len(X) , dtype=np.complex128) ;  
  Y +=   ( ( X >= x0-w/2 ) & ( X < x0+w/2 ) )*(np.sin( seige( (X-x0),a,b,w))-l ) / (r- l )  ; 
  Y +=  ( ( X >= x0+w/2 ) )  ;
  return Y ; 

def seige2pi(x ,w): return  2.0*np.pi*(x / w ) ;  

def sine_edge_2pi(X , x0 , w_ = 1e-10 ) :
  w = max(1e-10 , w_)  ; 
  Y = np.zeros(len(X) , dtype=np.complex128) ;  
  Y +=   ( ( X >= x0-w/2 ) & ( X < x0+w/2 ) )*(np.sin( seige2pi( (X-x0),w)) )  ; 
 # Y +=  ( ( X >= x0+w/2 ) )  ; 
  return Y ; 

def square_edge(X , x0 ) :return ( X >= x0)   ;






