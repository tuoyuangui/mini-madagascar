[sfpveltranVTI]
Cat:    RSF/system/seismic
Desc:   Slope-based tau-p velocity transform for VTI media
DocCmd: sfpveltranVTI | cat
Port:   stdin  rsf r req 	RSF standard input (containing tau0 data)
Port:   stdout rsf w req 	RSF standard output (containing velN data)
Port:   cmp rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   eta rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   velH rsf w  -  		auxiliary output file name (containing unspecified data)
Param:  curv string  -   -  		curvature field (required for method=e and method=d) (auxiliary input file name)
Param:  curvt string  -   -  		time derivative of curvature field (required for method=d and method=s) (auxiliary input file name)
Param:  de float  -  0.01 		eta sampling 
Param:  dip string  -   -  		slope field (required for method=e and method=d) (auxiliary input file name)
Param:  dipt string  -   -  		time derivative of slope field(auxiliary input file name)
Param:  dv float  -   -  		velocity sampling 
Param:  dvh float  -   -  		HOR velocity sampling 
LDesc:  (defaults to: dv)
Param:  e0 float  -  -0.5 		eta origin 
Param:  map enum-bool  -  n 		output maps instead of coherency panels 
Param:  method string  -   -  		method to use (stripping,dix,fowler,effective) 
Param:  ne int  -  101 		number of etas 
Param:  nv int  -   -  		number of velocities 
Param:  nvh int  -   -  		number of HOR velocities  
LDesc:  (defaults to: nv)
Param:  nw int  -  4 		interpolator size (2,3,4,6,8) 
Param:  tau0t string  -   -  		tau0 tau derivative field (required for method=f) (auxiliary input file name)
Param:  v0 float  -   -  		velocity origin 
Param:  vh0 float  -   -  		HOR velocity origin 
LDesc:  (defaults to: v0)

