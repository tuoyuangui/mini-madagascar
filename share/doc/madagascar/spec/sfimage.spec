[sfimage]
Cat:    RSF/su/plot
Desc:   X IMAGE plot of a uniformly-sampled function f(x1,x2)
DocCmd: sfimage | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Param:  balance enum-bool  -  n 		if false, determine bclip & wclip individually; 
LDesc:  	   else set them to the same abs value 
Param:  bclip float  -   -  		
Param:  blank float  -   -  		portion of the lower range to blank out 
LDesc:  (defaults to: 0.0f)
Param:  blockinterp enum-bool  -  n 		whether to use block interpolation 
Param:  bperc float  -   -  		percentile for determining black clip value 
LDesc:  (defaults to: perc)
Param:  clip float  -   -  		
Param:  cmap string  -   -  		colormap specification (hsv# or rgb#) 
Param:  curve string-list  -   -  		file(s) containing points to draw curve(s)  [curve]
Param:  curvecolor string-list  -   -  		color(s) for curve(s)  [ncurvecolor]
Param:  d1num float  -  0.0 		numbered tic interval on axis 1 (0.0 for automatic) 
Param:  d2num float  -  0.0 		numbered tic interval on axis 2 (0.0 for automatic) 
Param:  f1num float  -   -  		first numbered tic on axis 1 (used if d1num not 0.0) 
LDesc:  (defaults to: x1min)
Param:  f2num float  -  0.0 		first numbered tic on axis 2 (used if d2num not 0.0) 
Param:  grid1 string  -   -  		grid lines on axis 1 (none, dot, dash, or solid) 
Param:  grid2 string  -   -  		grid lines on axis 2 (none, dot, dash, or solid) 
Param:  gridcolor string  -   -  		color for grid lines 
Param:  hbox int  -  700 		height in pixels of window 
Param:  label1 string  -   -  		label on axis 1 
Param:  label2 string  -   -  		label on axis 2 
Param:  labelcolor string  -   -  		color for axes labels 
Param:  labelfont string  -   -  		font name for axes labels 
Param:  labelsize float  -  18.0 		
Param:  legend enum-bool  -  n 		if display the color scale 
Param:  legendfont string  -   -  		font name for legend 
Param:  lheight int  -   -  		colorscale (legend) height in pixels 
LDesc:  (defaults to: hbox/3)
Param:  lwidth int  -  16 		colorscale (legend) width in pixels 
Param:  lx int  -  3 		colorscale (legend) x-position in pixels 
Param:  ly int  -   -  		colorscale (legend) y-position in pixels 
LDesc:  (defaults to: (hbox-lheight)/3)
Param:  mpicks string  -   -  		file to save mouse picks 
Param:  n1tic int  -  1 		number of tics per numbered tic on axis 1 
Param:  n2tic int  -  1 		number of tics per numbered tic on axis 2 
Param:  ncurve int  -  0 		number of curves to draw 
Param:  ncurvecolor int  -  0 		number of curve colors 
Param:  npair int-list  -   -  		number(s) of pairs in each curve file  [curve]
Param:  perc float  -  100.0 		percentile used to determine clip 
Param:  style string  -   -  		normal (axis 1 horizontal, axis 2 vertical) 
LDesc:  	or  seismic (axis 1 vertical, axis 2 horizontal) 
Param:  title string  -   -  		title of plot 
Param:  titlecolor string  -   -  		color for title 
Param:  titlefont string  -   -  		font name for title 
Param:  titlesize float  -  24.0 		
Param:  units string  -   -  		unit label for legend 
Param:  verbose enum-bool  -  y 		verbose mode 
Param:  wbox int  -  550 		width in pixels of window 
Param:  wclip float  -   -  		
Param:  windowtitle string  -   -  		title on window 
Param:  wperc float  -   -  		percentile for determining white clip value 
LDesc:  (defaults to: 100.0-perc)
Param:  x1beg float  -   -  		value at which axis 1 begins 
LDesc:  (defaults to: x1min)
Param:  x1end float  -   -  		value at which axis 1 ends 
LDesc:  (defaults to: x1max)
Param:  x2beg float  -   -  		value at which axis 2 begins 
LDesc:  (defaults to: x2min)
Param:  x2end float  -   -  		value at which axis 2 ends 
LDesc:  (defaults to: x2max)
Param:  xbox int  -  50 		x in pixels of upper left corner of window 
Param:  ybox int  -  50 		y in pixels of upper left corner of window 

