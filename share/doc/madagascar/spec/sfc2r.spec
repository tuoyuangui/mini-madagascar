[sfc2r]
Cat:    RSF/system/seismic
Desc:   Cartesian-Coordinates to Riemannian-Coordinates interpolation
DocCmd: sfc2r | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fi data)
Port:   stdout rsf w req 	RSF standard output (containing Fo data)
Port:   rays rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  a1d float  -  1. 		
Param:  a1n int  -  1 		
Param:  a1o float  -  0. 		
Param:  a2d float  -  1. 		
Param:  a2n int  -  1 		
Param:  a2o float  -  0. 		
Param:  adj enum-bool  -  n 		
Param:  linear enum-bool  -  y 		
Param:  verb enum-bool  -  n 		

