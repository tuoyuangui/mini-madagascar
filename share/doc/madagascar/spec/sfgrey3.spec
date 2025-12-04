[sfgrey3]
Cat:    RSF/plot/main
Desc:   Generate 3-D cube plot
DocCmd: sfgrey3 | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout vpl w req 	VPL standard output (containing plot data)
Param:  bar string  -   -  		file for scalebar data 
Param:  barreverse enum-bool  -  n 		if y, go from small to large on the bar scale 
Param:  color string  -   -  		color scheme (default is i) 
Param:  dframe int  -  1 		frame increment in a movie 
Param:  flat enum-bool  -  y 		if n, display perspective view 
Param:  frame1 int  -  0 		top frame number 
Param:  frame2 int  -   -  		side frame number 
LDesc:  (defaults to: n2-1)
Param:  frame3 int  -  0 		front frame number 
Param:  maxval float  -   -  		maximum value for scalebar (default is the data maximum) 
Param:  minval float  -   -  		minimum value for scalebar (default is the data minimum) 
Param:  movie int  -  0 		0: no movie, 1: movie over axis 1, 2: axis 2, 3: axis 3 
Param:  n1pix int  -   -  		number of vertical pixels 
LDesc:  (defaults to: n1/point1+n3/(1.-point1))
Param:  n2pix int  -   -  		number of horizontal pixels 
LDesc:  (defaults to: n2/point2+n3/(1.-point2))
Param:  nreserve int  -  8 		reserved colors 
Param:  point1 float  -  0.5 		fraction of the vertical axis for front face 
Param:  point2 float  -  0.5 		fraction of the horizontal axis for front face 
Param:  scalebar enum-bool  -  n 		if y, draw scalebar 

