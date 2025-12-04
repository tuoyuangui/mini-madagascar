[sfcontour]
Cat:    RSF/plot/main
Desc:   Contour plot
DocCmd: sfcontour | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout vpl w req 	VPL standard output (containing plot data)
Param:  allpos enum-bool  -  y 		contour positive values only 
Param:  barlabel string  -   -  		scale bar label 
Param:  c float-list  -   -  		 [nc]
Param:  c0 float  -   -  		first contour 
Param:  cfile string  -   -  		contours in a file 
Param:  dc float  -   -  		contour increment 
Param:  max1 float  -   -  		maximum on 1st axis 
LDesc:  (defaults to: o1+(n1-1)*d1)
Param:  max2 float  -   -  		maximum on 2nd axis 
LDesc:  (defaults to: o2+(n2-1)*d2)
Param:  maxval float  -   -  		maximum value for scalebar (default is the data maximum) 
Param:  min1 float  -   -  		minimum on 1st axis 
LDesc:  (defaults to: o1)
Param:  min2 float  -   -  		minimum on 2nd axis 
LDesc:  (defaults to: o2)
Param:  minval float  -   -  		minimum value for scalebar (default is the data minimum) 
Param:  nc int  -  50 		number of contours 
Param:  transp enum-bool  -  y 		if y, transpose the axes 

