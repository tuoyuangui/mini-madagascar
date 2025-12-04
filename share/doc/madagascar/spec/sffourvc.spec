[sffourvc]
Cat:    RSF/system/seismic
Desc:   Prestack velocity continuation
DocCmd: sffourvc | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  dv float  -   -  		velocity step size 
Param:  eps float  -  0.01 		regularization 
Param:  extend int  -  4 		trace extension 
Param:  nv int  -   -  		velocity steps 
Param:  pad int  -   -  		padding for stretch 
LDesc:  (defaults to: n1)
Param:  pad2 int  -   -  		padding for FFT 
LDesc:  (defaults to: 2*kiss_fft_next_fast_size((n2+1)/2))
Param:  v0 float  -   -  		starting velocity 
Param:  verb enum-bool  -  n 		verbosity flag 

