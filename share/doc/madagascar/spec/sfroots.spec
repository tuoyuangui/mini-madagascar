[sfroots]
Cat:    RSF/system/generic
Desc:   Find roots of a complex polynomial
DocCmd: sfroots | cat
Port:   stdin  rsf r req 	RSF standard input (containing poly data)
Port:   stdout rsf w req 	RSF standard output (containing root data)
Param:  niter int  -  10 		number of iterations 
Param:  sort string  -   -  		attribute for sorting (phase,amplitude,real,imaginary) 
Param:  tol float  -  1.0e-6 		tolerance for convergence 
Param:  verb enum-bool  -  y 		verbosity flag 

