[sfpyramid]
Cat:    RSF/system/seismic
Desc:   Pyramid transform
DocCmd: sfpyramid | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  du float  -   -  		
LDesc:  (defaults to: dx)
Param:  eps float  -  0.01 		stretch regularization 
Param:  inv enum-bool  -  n 		inversion flag 
Param:  nu int  -   -  		
Param:  u0 float  -   -  		
LDesc:  (defaults to: x0)

