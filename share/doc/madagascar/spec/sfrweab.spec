[sfrweab]
Cat:    RSF/system/seismic
Desc:   Riemannian Wavefield Extrapolation: a,b coefficients
DocCmd: sfrweab | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fi data)
Port:   stdout rsf w req 	RSF standard output (containing Fo data)
Port:   abr rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   slo rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  naref int  -  1 		
Param:  nbref int  -  1 		
Param:  peps float  -  0.01 		
Param:  verb enum-bool  -  n 		

