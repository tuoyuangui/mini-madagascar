[sfpmig]
Cat:    RSF/system/seismic
Desc:   Slope-based prestack time migration
DocCmd: sfpmig | cat
Port:   stdin  rsf r req 	RSF standard input (containing cmp data)
Port:   stdout rsf w req 	RSF standard output (containing mig data)
Port:   hdip rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   xdip rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  eps float  -  1.0 		stretch regularization 
Param:  half enum-bool  -  y 		if y, the second axis is half-offset instead of full offset 
Param:  mzo enum-bool  -  n 		do migration to zero offset 

