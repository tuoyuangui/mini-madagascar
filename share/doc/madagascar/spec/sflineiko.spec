[sflineiko]
Cat:    RSF/system/seismic
Desc:   Iterative solution of the linearized eikonal equation
DocCmd: sflineiko | cat
Port:   stdin  rsf r req 	RSF standard input (containing time data)
Port:   stdout rsf w req 	RSF standard output (containing dtime data)
Port:   slow rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  adj enum-bool  -  n 		adjoint flag (for what=linear) 
Param:  inv enum-bool  -  n 		inverse flag (for what=linear) 
Param:  mask string  -   -  		auxiliary input file name
Param:  niter int  -  1 		maximum number of iterations 
Param:  squared enum-bool  -  y 		if slowness is squared 
Param:  time string  -   -  		auxiliary input file name
Param:  tol float  -  0.001 		tolerance for convergence 
Param:  what string  -   -  		what to compute 

