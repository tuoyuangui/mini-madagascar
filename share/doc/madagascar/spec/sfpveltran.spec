[sfpveltran]
Cat:    RSF/system/seismic
Desc:   Slope-based velocity transform
DocCmd: sfpveltran | cat
Port:   stdin  rsf r req 	RSF standard input (containing cmp data)
Port:   stdout rsf w req 	RSF standard output (containing vel data)
Port:   dip rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   dipt rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  dv float  -   -  		velocity sampling 
Param:  eps float  -  0.1 		stretch regularization 
Param:  half enum-bool  -  y 		if y, the second axis is half-offset instead of full offset 
Param:  interval enum-bool  -  n 		if y, compute interval velocity 
Param:  nv int  -   -  		number of velocities 
Param:  v0 float  -   -  		velocity origin 

