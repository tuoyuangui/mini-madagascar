[sfmutter]
Cat:    RSF/system/generic
Desc:   Muting
DocCmd: sfmutter | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  abs enum-bool  -  y 		if y, use absolute value |x-x0| 
Param:  half enum-bool  -  y 		if y, the second axis is half-offset instead of full offset 
Param:  hyper enum-bool  -  n 		if y, do hyperbolic mute 
Param:  inner enum-bool  -  n 		if y, do inner muter 
Param:  nan enum-bool  -  n 		if y, put  nans instead of zeros 
Param:  offset string  -   -  		auxiliary input file name
Param:  slope0 float  -   -  		slope 
LDesc:  (defaults to: 1./v0)
Param:  slopep float  -   -  		end slope 
LDesc:  (defaults to: slope0)
Param:  t0 float  -  0. 		starting time 
Param:  tp float  -  0.150 		end time 
Param:  v0 float  -  1.45 		velocity 
Param:  x0 float  -  0. 		starting space 

