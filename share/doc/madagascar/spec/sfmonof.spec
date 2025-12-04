[sfmonof]
Cat:    RSF/system/generic
Desc:   Mono-frequency wavelet estimation
DocCmd: sfmonof | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   ma rsf w  -  		auxiliary output file name (containing unspecified data)
Param:  a0 float  -  1. 		starting sharpness 
Param:  niter int  -  100 		number of iterations 
Param:  verb enum-bool  -  n 		verbosity flag 

