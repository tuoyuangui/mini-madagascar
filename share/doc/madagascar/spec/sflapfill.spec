[sflapfill]
Cat:    RSF/system/generic
Desc:   Missing data interpolation in 2-D by Laplacian regularization
DocCmd: sflapfill | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  grad enum-bool  -  n 		if y, use gradient instead of laplacian 
Param:  mask string  -   -  		optional mask file with zeroes for missing data locations (auxiliary input file name)
Param:  niter int  -  200 		number of iterations 
Param:  verb enum-bool  -  n 		verbosity flag 

