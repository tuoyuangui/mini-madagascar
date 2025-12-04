[sffreqlet]
Cat:    RSF/system/seismic
Desc:   1-D seislet frame
DocCmd: sffreqlet | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   freq rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  decomp enum-bool  -  n 		do decomposition 
Param:  inv enum-bool  -  n 		if y, do inverse transform 
Param:  ncycle int  -  0 		number of iterations 
Param:  niter int  -  1 		number of Bregman iterations 
Param:  perc float  -  50.0 		percentage for sharpening 
Param:  type string  -   -  		[haar,linear,biorthogonal] wavelet type, the default is linear  
Param:  verb enum-bool  -  y 		verbosity flag 

