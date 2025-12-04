[sftshift]
Cat:    RSF/system/seismic
Desc:   Compute angle gathers for time-shift imaging condition
DocCmd: sftshift | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fstk data)
Port:   stdout rsf w req 	RSF standard output (containing Fang data)
Port:   dip rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   velocity rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  a0 float  -  0. 		
Param:  cos enum-bool  -  n 		if n, convert pseudo-v to pseudo-tan(theta); 
LDesc:         if y, compute cos(theta) from 1/|pm| 
Param:  da float  -   -  		
LDesc:  (defaults to: 1./(nv-1))
Param:  extend int  -  4 		tmp extension 
Param:  na int  -   -  		
LDesc:  (defaults to: nv)

