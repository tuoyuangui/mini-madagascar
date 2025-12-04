[sfradon]
Cat:    RSF/system/seismic
Desc:   High-resolution Radon transform
DocCmd: sfradon | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  adj enum-bool  -  y 		if y, perform adjoint operation 
Param:  dp float  -   -  		p sampling (if adj=y) 
Param:  dx float  -   -  		
Param:  eps float  -  1. 		
Param:  fact float  -  0.5 		percentage for sharpening 
Param:  inv enum-bool  -   -  		if y, perform inverse operation 
LDesc:  (defaults to: adj)
Param:  niter int  -  100 		
Param:  np int  -   -  		number of p values (if adj=y) 
Param:  ns int  -  1 		number of sharpening cycles 
Param:  nx int  -   -  		number of offsets (if adj=n) 
Param:  offset string  -   -  		auxiliary input file name
Param:  ox float  -   -  		
Param:  p0 float  -   -  		p origin (if adj=y) 
Param:  parab enum-bool  -  n 		if y, parabolic Radon transform 
Param:  perc float  -  50.0 		percentage for sharpening 
Param:  spk enum-bool  -   -  		if y, use spiking (hi-res) inversion 
LDesc:  (defaults to: inv)
Param:  tol float  -  1.e-6 		inversion tolerance 
Param:  verb enum-bool  -  n 		verbosity flag 
Param:  x0 float  -  1. 		reference offset 

