[sfmap2coh]
Cat:    RSF/system/seismic
Desc:   From parameter's attribute map (veltran) to coherency-like plots
DocCmd: sfmap2coh | cat
Port:   stdin  rsf r req 	RSF standard input (containing cmp data)
Port:   stdout rsf w req 	RSF standard output (containing coh data)
Param:  dv float  -   -  		velocity sampling 
Param:  map string  -   -  		parameters map (auxiliary input file name)
Param:  max2 float  -   -  		max2 
LDesc:  (defaults to: o2+d2*(n2-1))
Param:  min2 float  -   -  		min2 
LDesc:  (defaults to: o2)
Param:  nv int  -   -  		number of velocities 
Param:  nw int  -  4 		interpolator size (2,3,4,6,8) 
Param:  v0 float  -   -  		velocity origin 

