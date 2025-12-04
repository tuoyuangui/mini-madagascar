[sfinttest1]
Cat:    RSF/system/generic
Desc:   Interpolation from a regular grid in 1-D
DocCmd: sfinttest1 | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   coord rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  interp string  -   -  		interpolation (lagrange,cubic,kaiser,lanczos,cosine,welch,spline,mom) 
Param:  kai float  -  4.0 		Kaiser window parameter 
Param:  nw int  -   -  		interpolator size 
Param:  same enum-bool  -  y 		same or different coordinates for each trace 

