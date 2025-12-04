[sfremap1]
Cat:    RSF/system/generic
Desc:   1-D ENO interpolation
DocCmd: sfremap1 | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  d1 float  -   -  		Output sampling 
LDesc:  (defaults to: d1)
Param:  n1 int  -   -  		Number of output samples 
LDesc:  (defaults to: n1)
Param:  o1 float  -   -  		Output origin 
LDesc:  (defaults to: o1)
Param:  order int  -  3 		Interpolation order 
Param:  pattern string  -   -  		auxiliary input file name

