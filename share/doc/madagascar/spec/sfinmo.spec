[sfinmo]
Cat:    RSF/system/seismic
Desc:   Inverse normal moveout
DocCmd: sfinmo | cat
Port:   stdin  rsf r req 	RSF standard input (containing cmp data)
Port:   stdout rsf w req 	RSF standard output (containing nmod data)
Port:   velocity rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  eps float  -  0.01 		stretch regularization 
Param:  h0 float  -  0. 		reference offset 
Param:  half enum-bool  -  y 		if y, the second axis is half-offset instead of full offset 
Param:  mask string  -   -  		auxiliary input file name
Param:  offset string  -   -  		auxiliary input file name
Param:  slowness enum-bool  -  n 		if y, use slowness instead of velocity 

