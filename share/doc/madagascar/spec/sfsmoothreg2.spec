[sfsmoothreg2]
Cat:    RSF/system/generic
Desc:   Smoothing in 2-D by simple regularization
DocCmd: sfsmoothreg2 | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (containing smooth data)
Param:  eps float  -  1. 		smoothness parameter 
Param:  repeat int  -  1 		repeat smoothing 

