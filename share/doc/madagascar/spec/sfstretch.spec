[sfstretch]
Cat:    RSF/system/seismic
Desc:   Stretch of the time axis
DocCmd: sfstretch | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   datum rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  CDPtype int  -   -  		
Param:  delay float  -   -  		time delay for rule=lmo 
Param:  dens int  -  1 		axis stretching factor 
Param:  extend int  -  4 		trace extension 
Param:  half enum-bool  -  y 		if y, the second axis is half-offset instead of full offset 
Param:  hdelay float  -   -  		offset delay for rule=rad 
Param:  inv enum-bool  -  n 		if y, do inverse stretching 
Param:  maxstr float  -  0 		maximum stretch 
Param:  mute int  -  0 		tapering size 
Param:  nout int  -   -  		output axis length (if inv=n) 
LDesc:  (defaults to: dens*n1)
Param:  rule string  -   -  		Stretch rule:
LDesc:  	   n - constant-velocity normal moveout (nmostretch), default
LDesc:  	   l - linear moveout (lmostretch)
LDesc:  	   L - logarithmic stretch (logstretch)
LDesc:  	   2 - t^2 stretch (t2stretch)
LDesc:  	   c - t^2 chebyshev stretch (t2chebstretch)
LDesc:  	   r - radial moveout (radstretch)
LDesc:  	   d - datuming (datstretch)
LDesc:  	   s - s*t scaling stretch (scalestretch)
LDesc:  	
Param:  scale float  -   -  		scaling factor for rule=scale 
Param:  tdelay float  -   -  		time delay for rule=rad 
Param:  v0 float  -   -  		moveout velocity 
Param:  verb enum-bool  -  y 		verbosity flag 

