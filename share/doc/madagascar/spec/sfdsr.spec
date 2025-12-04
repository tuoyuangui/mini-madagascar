[sfdsr]
Cat:    RSF/system/seismic
Desc:   Prestack 2-D VTI v(z) modeling/migration by DSR with angle gathers
DocCmd: sfdsr | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  arule string  -   -  		angle gather rule 
Param:  da float  -  90. 		angle sampling (in degrees) 
Param:  depth enum-bool  -  n 		if true, depth migration 
Param:  dh float  -   -  		Offset sampling (for modeling) 
Param:  dt float  -   -  		Sampling of time axis (for modeling) 
Param:  dz float  -   -  		Sampling of depth axis (for migration, if no velocity file) 
LDesc:  (defaults to: dt)
Param:  eps float  -  0.01 		Stabilization parameter 
Param:  eta string  -   -  		auxiliary input file name
Param:  inv enum-bool  -  n 		If y, modeling; If n, migration 
Param:  n float  -  0.0 		Constant eta (if no velocity file) 
Param:  na int  -  1 		number of angles 
Param:  nh int  -   -  		Number of offsets (for modeling) 
Param:  nt int  -   -  		Length of time axis (for modeling) 
Param:  nw int  -   -  		Maximum number of frequencies 
LDesc:  (defaults to: nt2/2+1)
Param:  nz int  -   -  		Length of depth axis (for migration, if no velocity file) 
LDesc:  (defaults to: nt)
Param:  rule string  -   -  		phase-shift interpolation rule (simple, midpoint, linear, anisotropic, dti) 
Param:  t0 float  -  0. 		
Param:  vel float  -   -  		Constant velocity (if no velocity file) 
Param:  velocity string  -   -  		file with velocity (file with velocity (auxiliary input file name))
Param:  velz string  -   -  		auxiliary input file name
Param:  vz float  -   -  		Constant vertical velocity (if no velocity file) 
LDesc:  (defaults to: v0)

