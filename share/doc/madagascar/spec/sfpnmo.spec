[sfpnmo]
Cat:    RSF/system/seismic
Desc:   Slope-based normal moveout
DocCmd: sfpnmo | cat
Port:   stdin  rsf r req 	RSF standard input (containing cmp data)
Port:   stdout rsf w req 	RSF standard output (containing nmod data)
Port:   dip rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   eta rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   vel rsf w  -  		auxiliary output file name (containing unspecified data)
Param:  crv string  -   -  		auxiliary input file name
Param:  eps float  -  0.01 		stretch regularization 
Param:  half enum-bool  -  y 		if y, the second axis is half-offset instead of full offset 
Param:  offset string  -   -  		auxiliary input file name

