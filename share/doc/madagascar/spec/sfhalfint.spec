[sfhalfint]
Cat:    RSF/system/seismic
Desc:   Half-order integration or differentiation
DocCmd: sfhalfint | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  adj enum-bool  -  n 		If y, apply adjoint 
Param:  inv enum-bool  -  n 		If y, do differentiation instead of integration 
Param:  rho float  -   -  		Leaky integration constant 
LDesc:  (defaults to: 1.-1./n1)

