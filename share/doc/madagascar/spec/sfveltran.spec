[sfveltran]
Cat:    RSF/system/seismic
Desc:   Hyperbolic Radon transform
DocCmd: sfveltran | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  adj enum-bool  -  n 		adjoint flag 
Param:  anti float  -  1. 		antialiasing 
Param:  pull enum-bool  -  y 		pull or push operator 
Param:  s02 float  -  0. 		reference slowness squared (for antialiasing) 

