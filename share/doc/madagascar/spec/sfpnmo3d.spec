[sfpnmo3d]
Cat:    RSF/system/seismic
Desc:   Slope-based normal moveout for 3-D CMP geometry
DocCmd: sfpnmo3d | cat
Port:   stdin  rsf r req 	RSF standard input (containing cmp data)
Port:   stdout rsf w req 	RSF standard output (containing nmod data)
Port:   dipx rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   dipy rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   vel rsf w  -  		auxiliary output file name (containing unspecified data)
Param:  eps float  -  0.01 		stretch regularization 
Param:  extend int  -  8 		trace extension 
Param:  half enum-bool  -  y 		if y, the second axis is half-offset instead of full offset 

