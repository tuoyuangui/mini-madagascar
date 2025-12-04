[sflinear]
Cat:    RSF/system/generic
Desc:   1-D linear interpolation
DocCmd: sflinear | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  d1 float  -   -  		Output sampling 
Param:  n1 string  -   -  		Output grid size 
Param:  niter int  -  0 		number of iterations 
Param:  nw int  -  2 		interpolator size 
Param:  o1 float  -   -  		Output origin 
Param:  pattern string  -   -  		auxiliary input file name
Param:  rect int  -  1 		smoothing regularization 
Param:  sort enum-bool  -  n 		if y, the coordinates need sorting 

