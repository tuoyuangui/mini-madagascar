[sfhwtex]
Cat:    RSF/system/seismic
Desc:   Huygens wavefront tracing traveltimes
DocCmd: sfhwtex | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fv data)
Port:   stdout rsf w req 	RSF standard output (containing Fw data)
Port:   sou rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  dt float  -  0.001 		
Param:  nt int  -  100 		
Param:  ot float  -  0 		
Param:  verb enum-bool  -  n 		verbosity flag 
Param:  wini enum-bool  -  n 		initialize two wavefronts 

