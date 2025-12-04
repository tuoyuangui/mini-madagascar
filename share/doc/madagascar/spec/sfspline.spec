[sfspline]
Cat:    RSF/system/generic
Desc:   1-D cubic spline interpolation
DocCmd: sfspline | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  fp float-list  -   -  		end-point derivatives  [2]
Param:  pattern string  -   -  		auxiliary input file name
Param:  sort enum-bool  -  n 		if y, the coordinates need sorting 

