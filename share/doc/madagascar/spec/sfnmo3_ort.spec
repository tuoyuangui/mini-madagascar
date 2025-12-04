[sfnmo3_ort]
Cat:    RSF/system/seismic
Desc:   3-D Normal moveout using orthogonal parametrization
DocCmd: sfnmo3_ort | cat
Port:   stdin  rsf r req 	RSF standard input (containing cmp data)
Port:   stdout rsf w req 	RSF standard output (containing nmod data)
Port:   velocity rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  eps float  -  0.01 		stretch regularization 
Param:  extend int  -  8 		trace extension 
Param:  half enum-bool  -  y 		if y, the second and third axes are half-offset instead of full offset 
Param:  mute int  -  12 		mute zone 
Param:  offset string  -   -  		auxiliary input file name

