[sftime2depth]
Cat:    RSF/system/seismic
Desc:   Time-to-depth conversion in V(z)
DocCmd: sftime2depth | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   velocity rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  dz float  -   -  		Depth sampling (default: d1) 
Param:  eps float  -  0.01 		stretch regularization 
Param:  extend int  -  4 		Interpolation accuracy 
Param:  intime enum-bool  -  n 		y if velocity is in time rather than depth 
Param:  nz int  -   -  		Number of depth samples (default: n1) 
Param:  slow enum-bool  -  n 		If y, input slowness; if n, velocity 
Param:  twoway enum-bool  -  y 		if y, two-way traveltime 
Param:  z0 float  -  0. 		Depth origin 

