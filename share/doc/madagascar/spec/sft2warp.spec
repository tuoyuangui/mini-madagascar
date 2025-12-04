[sft2warp]
Cat:    RSF/system/generic
Desc:   Time-squared warping
DocCmd: sft2warp | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  adj enum-bool  -  n 		adjoint flag 
Param:  eps float  -  0.01 		stretch regularization 
Param:  inv enum-bool  -  n 		inversion flag 
Param:  pad int  -   -  		output time samples 
LDesc:  (defaults to: n1)

