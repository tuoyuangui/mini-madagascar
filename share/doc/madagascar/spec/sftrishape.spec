[sftrishape]
Cat:    RSF/system/generic
Desc:   2-D irregular data interpolation using triangulation and shaping regularization
DocCmd: sftrishape | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  d1 float  -  1. 		
Param:  d2 float  -  1. 		
Param:  fast enum-bool  -  n 		if y, use GMRES inversion 
Param:  n1 int  -   -  		
Param:  n2 int  -   -  		
Param:  niter int  -  0 		number of iterations 
Param:  nw int  -  2 		interpolator size 
Param:  o1 float  -  0. 		
Param:  o2 float  -  0. 		
Param:  pattern string  -   -  		pattern file for output dimensions (auxiliary input file name)
Param:  rect1 int  -  1 		
Param:  rect2 int  -  1 		smoothing regularization 
Param:  sym enum-bool  -  n 		if y, use symmetric shaping 
Param:  tol float  -  1e-3 		tolerance for stopping iteration 
Param:  zero float  -  0. 		level surface 

