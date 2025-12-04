[sfaastack]
Cat:    RSF/system/seismic
Desc:   Stack with antialiasing
DocCmd: sfaastack | cat
Port:   stdin  rsf r req 	RSF standard input (containing inp data)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  adj enum-bool  -  n 		adjoint flag 
Param:  antialias float  -  1. 		antialiasing 
Param:  box enum-bool  -  n 		box antialiasing 
Param:  inv enum-bool  -  n 		inverse flag 
Param:  n2 int  -  1 		
Param:  vel float  -  1.5 		velocity 

