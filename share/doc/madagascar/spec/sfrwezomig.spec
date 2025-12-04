[sfrwezomig]
Cat:    RSF/system/seismic
Desc:   Riemannian Wavefield Extrapolation: zero-offset modeling/migration
DocCmd: sfrwezomig | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fi data)
Port:   stdout rsf w req 	RSF standard output (containing Fd data)
Port:   abm rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   abr rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  adj enum-bool  -  n 		y=modeling; n=migration 
Param:  dw float  -   -  		
Param:  method int  -  0 		extrapolation method 
Param:  nw int  -   -  		
Param:  ow float  -  0. 		
Param:  verb enum-bool  -  n 		

