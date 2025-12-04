[sfpreconstkirch]
Cat:    RSF/system/seismic
Desc:   Prestack Kirchhoff modeling/migration in constant velocity
DocCmd: sfpreconstkirch | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  aal enum-bool  -  y 		if y, apply antialiasing 
Param:  dh float  -   -  		offset sampling 
Param:  h0 float  -   -  		offset origin 
Param:  inv enum-bool  -  n 		if y, modeling; if n, migration 
Param:  nh int  -   -  		number of offsets 
Param:  vel float  -   -  		velocity 
Param:  zero enum-bool  -  n 		if y, stack in migration 

