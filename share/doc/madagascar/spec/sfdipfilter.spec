[sfdipfilter]
Cat:    RSF/system/generic
Desc:   Filter data based on dip in 2-D or 3-D
DocCmd: sfdipfilter | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  ang1 float  -  -50. 		
Param:  ang2 float  -  -45. 		
Param:  ang3 float  -  45. 		
Param:  ang4 float  -  50. 		Angle gate (in degrees) 
Param:  angle enum-bool  -  n 		Filter based on angle (or velocity) 
Param:  dim int  -  2 		Dimensionality: filter 2-D planes or 3-D cubes 
Param:  pass enum-bool  -  y 		Pass or reject band 
Param:  v float  -  -1. 		constant velocity (if angle-y)
LDesc:  	   The default is d(frequency)/d(wavenumber) 
Param:  v1 float  -  0. 		
Param:  v2 float  -  0.1 		
Param:  v3 float  -  99999. 		
Param:  v4 float  -  999999. 		Velocity gate 

