[sfcontour3]
Cat:    RSF/plot/main
Desc:   Generate 3-D contour plot
DocCmd: sfcontour3 | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout vpl w req 	VPL standard output (containing plot data)
Param:  barreverse enum-bool  -  n 		if y, go from small to large on the bar scale 
Param:  c float-list  -   -  		 [nc]
Param:  c0 float  -   -  		first contour 
Param:  cfile string  -   -  		contours in a file 
Param:  dc float  -   -  		contour increment 
Param:  dframe int  -  1 		frame increment in a movie 
Param:  flat enum-bool  -  y 		if n, display perspective view 
Param:  frame1 int  -  0 		
Param:  frame2 int  -   -  		
LDesc:  (defaults to: n2-1)
Param:  frame3 int  -  0 		frame numbers for cube faces 
Param:  max1 float  -   -  		
LDesc:  (defaults to: o1+(n1-1)*d1)
Param:  max2 float  -   -  		
LDesc:  (defaults to: o2+(n2-1)*d2)
Param:  max3 float  -   -  		data window to plot 
LDesc:  (defaults to: o3+(n3-1)*d3)
Param:  maxval float  -   -  		maximum value for scalebar (default is the data maximum) 
Param:  min1 float  -   -  		
LDesc:  (defaults to: o1)
Param:  min2 float  -   -  		
LDesc:  (defaults to: o2)
Param:  min3 float  -   -  		
LDesc:  (defaults to: o3)
Param:  minval float  -   -  		minimum value for scalebar (default is the data minimum) 
Param:  movie int  -  0 		0: no movie, 1: movie over axis 1, 2: axis 2, 3: axis 3 
Param:  n1pix int  -   -  		number of vertical pixels 
LDesc:  (defaults to: n1/point1+n3/(1.-point1))
Param:  n2pix int  -   -  		number of horizontal pixels 
LDesc:  (defaults to: n2/point2+n3/(1.-point2))
Param:  nc int  -  50 		number of contours 
Param:  point1 float  -  0.5 		fraction of the vertical axis for front face 
Param:  point2 float  -  0.5 		fraction of the horizontal axis for front face 
Param:  scalebar enum-bool  -  n 		if y, draw scalebar 
Param:  yreverse enum-bool  -  y 		if y, reverse the first axis 

