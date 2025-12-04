[sfenvelope]
Cat:    RSF/system/seismic
Desc:   None
DocCmd: sfenvelope | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  hilb enum-bool  -  n 		if y, compute Hilbert transform 
Param:  order int  -  100 		Hilbert transformer order 
Param:  phase float  -  90. 		phase shift (in degrees) to use with hilb=y 
Param:  ref float  -  1. 		Hilbert transformer reference (0.5 < ref <= 1) 

