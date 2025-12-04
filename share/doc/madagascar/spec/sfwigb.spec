[sfwigb]
Cat:    RSF/su/plot
Desc:   X WIGgle-trace plot of f(x1,x2) via Bitmap
DocCmd: sfwigb | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Param:  bias float  -  0.0 		data value corresponding to location along axis 2 
Param:  clip float  -   -  		data values < bias+clip and > bias-clip are clipped 
Param:  d1num float  -  0.0 		numbered tic interval on axis 1 (0.0 for automatic) 
Param:  d2num float  -  0.0 		numbered tic interval on axis 2 (0.0 for automatic) 
Param:  endian int  -   -  		endian for display =0 little endian =1 big endian 
Param:  f1num float  -   -  		first numbered tic on axis 1 (used if d1num not 0.0) 
LDesc:  (defaults to: x1min)
Param:  f2num float  -   -  		first numbered tic on axis 2 (used if d2num not 0.0) 
LDesc:  (defaults to: x2min)
Param:  grid1 string  -   -  		grid lines on axis 1 - none, dot, dash, or solid 
Param:  grid2 string  -   -  		grid lines on axis 2 - none, dot, dash, or solid 
Param:  gridcolor string  -   -  		
Param:  hbox int  -  700 		height in pixels of window 
Param:  interp enum-bool  -  n 		if y, use interpolation 
Param:  label1 string  -   -  		
Param:  label2 string  -   -  		
Param:  labelcolor string  -   -  		
Param:  labelfont string  -   -  		font name for axes labels 
Param:  labelsize float  -  18.0 		
Param:  mpicks string  -   -  		file to save mouse picks in 
Param:  n1tic int  -  1 		number of tics per numbered tic on axis 1 
Param:  n2tic int  -  1 		number of tics per numbered tic on axis 2 
Param:  perc float  -  100.0 		percentile for determining clip 
Param:  style string  -   -  		
Param:  title string  -   -  		
Param:  titlecolor string  -   -  		
Param:  titlefont string  -   -  		
Param:  titlesize float  -  24.0 		
Param:  va int  -  1 		=0 for no variable-area; 
LDesc:         =1 for variable-area fill;
LDesc:         =2 for variable area, solid/grey fill 
Param:  verbose enum-bool  -  y 		y for info printed on stderr (n for no info) 
Param:  wbox int  -  550 		width in pixels of window 
Param:  wigclip int  -  0 		If 0, the plot box is expanded to accommodate	
LDesc:         the larger wiggles created by xcur>1. If this 
LDesc:         flag is non-zero, the extra-large wiggles are	
LDesc:         are clipped at the boundary of the plot box. 
Param:  windowtitle string  -   -  		initialize zoom box parameters 
Param:  wt int  -  1 		=0 for no wiggle-trace; =1 for wiggle-trace 
Param:  x1beg float  -   -  		value at which axis 1 begins 
LDesc:  (defaults to: x1min)
Param:  x1end float  -   -  		value at which axis 1 ends 
LDesc:  (defaults to: x1max)
Param:  x2 float-list  -   -  		array of sampled values in 2nd dimension  [n2]
Param:  x2beg float  -   -  		value at which axis 2 begins 
LDesc:  (defaults to: x2min)
Param:  x2end float  -   -  		value at which axis 2 ends 
LDesc:  (defaults to: x2max)
Param:  xbox int  -  50 		x in pixels of upper left corner of window 
Param:  xcur float  -  1.0 		wiggle excursion in traces corresponding to clip 
Param:  ybox int  -  50 		y in pixels of upper left corner of window 

