[sfnmo]
Cat:    RSF/system/seismic
Desc:   Normal moveout
DocCmd: sfnmo | cat
Port:   stdin  rsf r req 	RSF standard input (containing cmp data)
Port:   stdout rsf w req 	RSF standard output (containing nmod data)
Port:   velocity rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  CDPtype int  -   -  		
Param:  a string  -   -  		
Param:  extend int  -  4 		trace extension 
Param:  h0 float  -  0. 		reference offset 
Param:  half enum-bool  -  y 		if y, the second axis is half-offset instead of full offset 
Param:  mask string  -   -  		auxiliary input file name
Param:  mute int  -  12 		mute zone 
Param:  offset string  -   -  		auxiliary input file name
Param:  s string  -   -  		auxiliary input file name
Param:  slowness enum-bool  -  n 		if y, use slowness instead of velocity 
Param:  squared enum-bool  -  n 		if y, the slowness or velocity is squared 
Param:  str float  -  0.5 		maximum stretch allowed 

