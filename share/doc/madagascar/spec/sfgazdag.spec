[sfgazdag]
Cat:    RSF/system/seismic
Desc:   Post-stack 2-D/3-D v(z) time modeling/migration with Gazdag phase-shift
DocCmd: sfgazdag | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  depth enum-bool  -  n 		if true, depth migration 
Param:  dt float  -   -  		Sampling of time axis (for modeling) 
Param:  dz float  -   -  		Sampling of depth axis (for migration, if no velocity file) 
Param:  eps float  -  0.01 		stabilization parameter 
Param:  eta string  -   -  		auxiliary input file name
Param:  inv enum-bool  -  n 		if y, modeling; if n, migration 
Param:  n float  -  0.0 		Constant eta (if no velocity file) 
Param:  nt int  -   -  		Length of time axis (for modeling) 
Param:  nz int  -   -  		Length of depth axis (for migration, if no velocity file) 
Param:  pad int  -   -  		
LDesc:  (defaults to: 2*kiss_fft_next_fast_size((nt+1)/2))
Param:  rule string  -   -  		phase-shift interpolation rule (simple, midpoint, linear) 
Param:  vel float  -   -  		Constant velocity (if no velocity file) 
Param:  velocity string  -   -  		auxiliary input file name
Param:  velz string  -   -  		auxiliary input file name
Param:  verb enum-bool  -  n 		verbosity flag 
Param:  vz float  -   -  		Constant vertical velocity (if no velocity file) 
LDesc:  (defaults to: v0)

