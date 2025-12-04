[sfdepth2time]
Cat:    RSF/system/seismic
Desc:   Conversion from depth to time in a V(z) medium
DocCmd: sfdepth2time | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   velocity rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  dt float  -   -  		Time sampling (default is d1) 
Param:  eps float  -  0.01 		smoothness parameter 
Param:  nt int  -   -  		Number of points in time (default is n1) 
Param:  slow enum-bool  -  n 		y: slowness, n: velocity 
Param:  t0 float  -   -  		Time origin (default is 0) 

