[sfslant]
Cat:    RSF/system/seismic
Desc:   Time-space-domain Radon transform (slant stack)
DocCmd: sfslant | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  adj enum-bool  -  n 		adjoint flag 
Param:  anti float  -  1. 		antialiasing 
Param:  dp float  -   -  		p sampling (if adj=y) 
Param:  dx float  -   -  		offset sampling 
Param:  np int  -   -  		number of p values (if adj=y) 
Param:  nx int  -   -  		number of offsets 
Param:  p0 float  -   -  		p origin (if adj=y) 
Param:  p1 float  -  0. 		reference slope 
Param:  rho enum-bool  -  y 		rho filtering 
Param:  verb enum-bool  -  n 		verbosity flag 
Param:  x0 float  -   -  		offset origin 

