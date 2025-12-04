[sftri2reg]
Cat:    RSF/system/generic
Desc:   Interpolate triangulated triplets to a regular grid
DocCmd: sftri2reg | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  d1 float  -  1. 		
Param:  d2 float  -  1. 		
Param:  edgein string  -   -  		input edge file (auxiliary input file name)
Param:  edgeout string  -   -  		auxiliary output file name
Param:  n1 int  -   -  		
Param:  n2 int  -   -  		
Param:  nodeout string  -   -  		auxiliary output file name
Param:  nr int  -  0 		number of refinements 
Param:  o1 float  -  0. 		
Param:  o2 float  -  0. 		
Param:  pattern string  -   -  		pattern file for output dimensions (auxiliary input file name)
Param:  zero float  -  0. 		level surface 

