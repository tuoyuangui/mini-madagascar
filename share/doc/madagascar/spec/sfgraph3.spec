[sfgraph3]
Cat:    RSF/plot/main
Desc:   Generate 3-D cube plot for surfaces
DocCmd: sfgraph3 | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout vpl w req 	VPL standard output (containing plot data)
Param:  dframe float  -  1 		frame increment in a movie 
Param:  flat enum-bool  -  y 		if n, display perspective view 
Param:  frame1 float  -   -  		
LDesc:  (defaults to: 0.5*(min+max))
Param:  frame2 int  -   -  		
LDesc:  (defaults to: n1-1)
Param:  frame3 int  -  0 		frame numbers for cube faces 
Param:  max float  -   -  		maximum function value 
Param:  min float  -   -  		minimum function value 
Param:  movie int  -  0 		0: no movie, 1: movie over axis 1, 2: axis 2, 3: axis 3 
Param:  n1pix int  -   -  		number of vertical pixels 
LDesc:  (defaults to: n1/point1+n3/(1.-point1))
Param:  n2pix int  -   -  		number of horizontal pixels 
LDesc:  (defaults to: n2/point2+n3/(1.-point2))
Param:  orient int  -  1 		function orientation 
Param:  point1 float  -  0.5 		fraction of the vertical axis for front face 
Param:  point2 float  -  0.5 		fraction of the horizontal axis for front face 
Param:  yreverse enum-bool  -  n 		

