[sfcgscan]
Cat:    RSF/system/seismic
Desc:   Hyperbolic Radon transform with conjugate-directions inversion
DocCmd: sfcgscan | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  adj enum-bool  -  n 		adjoint flag 
Param:  anti float  -  1. 		antialiasing 
Param:  error string  -   -  		auxiliary output file name
Param:  fact float  -  0.5 		factor for sharpening 
Param:  mask string  -   -  		auxiliary input file name
Param:  miter int  -  2 		conjugate-direction memory 
Param:  ncycle int  -  0 		number of sharpening cycles 
Param:  niter int  -  0 		number of iterations 
Param:  perc float  -  50.0 		percentage for sharpening 
Param:  psun1 int  -  1 		amplitude type for adjoint 
Param:  psun2 int  -  1 		amplitude type for forward 
Param:  s02 float  -  0. 		reference slowness squared (for antialiasing) 

