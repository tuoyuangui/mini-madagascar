[sffft1]
Cat:    RSF/system/generic
Desc:   Fast Fourier Transform along the first axis
DocCmd: sffft1 | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fin data)
Port:   stdout rsf w req 	RSF standard output (containing Fou data)
Param:  inv enum-bool  -  n 		y, inverse transform 
Param:  memsize float  -  1000.0 		
Param:  opt enum-bool  -  y 		y, determine optimal size for efficiency 
Param:  ot string  -   -  		auxiliary input file name
Param:  sym enum-bool  -  n 		y, symmetric scaling for Hermitian FFT 
Param:  verb enum-bool  -  n 		verbosity flag 

