[sfinttest2]
Cat:    RSF/system/generic
Desc:   Interpolation from a regular grid in 2-D
DocCmd: sfinttest2 | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   coord rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  interp string  -   -  		interpolation (lagrange,cubic,kaiser,lanczos,cosine,welch,spline) 
Param:  kai float  -  4.0 		Kaiser window parameter 
Param:  nw int  -   -  		interpolator size 

