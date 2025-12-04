[sfradial2]
Cat:    RSF/system/seismic
Desc:   Another version of radial transform
DocCmd: sfradial2 | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  eps float  -  0.01 		stretch regularization 
Param:  inv enum-bool  -  n 		if y, do inverse transform 
Param:  nv int  -   -  		number of velocities (if inv=n) 
Param:  tp float  -   -  		
LDesc:  (defaults to: t0)
Param:  vmax float  -   -  		maximum velocity (if inv=n) 
Param:  vmin float  -   -  		minimum velocity (if inv=n) 

