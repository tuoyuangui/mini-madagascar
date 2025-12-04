[sfsmooth]
Cat:    RSF/system/generic
Desc:   Multi-dimensional triangle smoothing
DocCmd: sfsmooth | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  adj enum-bool  -  n 		run in the adjoint mode 
Param:  diff# enum-bool  -   -  		differentiation on #-th axis 
LDesc:  (defaults to: (n,n,...))
Param:  rect# int  -   -  		smoothing radius on #-th axis 
LDesc:  (defaults to: (1,1,...))
Param:  repeat int  -  1 		repeat filtering several times 

