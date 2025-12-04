[sfradial]
Cat:    RSF/system/seismic
Desc:   Radial transform
DocCmd: sfradial | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  inv enum-bool  -  n 		if y, do inverse transform 
Param:  nv int  -   -  		number of velocities (if inv=n) 
Param:  nw int  -  2 		accuracy level 
Param:  tp float  -   -  		
LDesc:  (defaults to: t0)
Param:  vmax float  -   -  		maximum velocity (if inv=n) 
Param:  vmin float  -   -  		minimum velocity (if inv=n) 
Param:  xp float  -  0. 		

