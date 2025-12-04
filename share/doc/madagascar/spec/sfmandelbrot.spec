[sfmandelbrot]
Cat:    RSF/system/generic
Desc:   Generate Mandelbrot set
DocCmd: sfmandelbrot | cat
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  dx float  -   -  		
LDesc:  (defaults to: (xmax-x0)/(n1-1))
Param:  dy float  -   -  		
LDesc:  (defaults to: (ymax-y0)/(n2-1))
Param:  n1 int  -  512 		
Param:  n2 int  -  512 		dimensions 
Param:  niter int  -  1000 		number of iterations 
Param:  x0 float  -  -2. 		
Param:  xmax float  -  0.5 		
Param:  y0 float  -  -1. 		set origin 
Param:  ymax float  -  1. 		set maximum 

