[sfricker]
Cat:    RSF/system/seismic
Desc:   Ricker wavelet estimation
DocCmd: sfricker | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   ma rsf w  -  		auxiliary output file name (containing unspecified data)
Param:  m float  -   -  		initial frequency 
LDesc:  (defaults to: f0+0.25*(na-1)*df)
Param:  niter int  -  100 		number of iterations 
Param:  verb enum-bool  -  n 		verbosity flag 

