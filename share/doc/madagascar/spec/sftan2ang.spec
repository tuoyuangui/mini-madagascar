[sftan2ang]
Cat:    RSF/system/seismic
Desc:   tangent to angle transformation
DocCmd: sftan2ang | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fstk data)
Port:   stdout rsf w req 	RSF standard output (containing Fang data)
Port:   velocity rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  a0 float  -  0. 		
Param:  da float  -   -  		
LDesc:  (defaults to: 90/(nt-1))
Param:  extend int  -  4 		tmp extension 
Param:  na int  -   -  		
LDesc:  (defaults to: nt)
Param:  top enum-bool  -  n 		

