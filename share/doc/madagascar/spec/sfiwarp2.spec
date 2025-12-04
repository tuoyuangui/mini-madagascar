[sfiwarp2]
Cat:    RSF/system/seismic
Desc:   Inverse 2-D warping
DocCmd: sfiwarp2 | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   warp rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  d1 int  -  1 		output sampling - for inv=y 
Param:  d2 float  -  1 		output sampling - for inv=y 
Param:  eps float  -  0.01 		stretch regularization 
Param:  inv enum-bool  -  y 		inversion flag 
Param:  n1 int  -   -  		
LDesc:  (defaults to: nt)
Param:  n2 int  -   -  		output samples - for inv=y 
LDesc:  (defaults to: nx)
Param:  o1 float  -  0 		output origin - for inv=y 
Param:  o2 float  -  0 		output origin - for inv=y 

