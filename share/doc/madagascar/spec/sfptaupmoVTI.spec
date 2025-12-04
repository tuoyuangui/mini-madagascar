[sfptaupmoVTI]
Cat:    RSF/system/seismic
Desc:   Slope-based tau-p moveout in VTI
DocCmd: sfptaupmoVTI | cat
Port:   stdin  rsf r req 	RSF standard input (containing inp data)
Port:   stdout rsf w req 	RSF standard output (containing nmod data)
Port:   cos2 rsf w  -  		auxiliary output file name (containing unspecified data)
Param:  ddip string  -   -  		curvature field (auxiliary input file name)
Param:  dip string  -   -  		slope field (auxiliary input file name)
Param:  eps float  -  0.01 		stretch regularization 
Param:  tau0 string  -   -  		tau0(tau,p) (auxiliary output file name)

