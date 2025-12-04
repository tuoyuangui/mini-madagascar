[sfwiggle]
Cat:    RSF/plot/main
Desc:   Plot data with wiggly traces
DocCmd: sfwiggle | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout vpl w req 	VPL standard output (containing plot data)
Param:  clip float  -  0. 		data clip (estimated from pclip by default 
Param:  fatp int  -  1 		polygon border fatness 
Param:  pclip float  -  98. 		clip percentile 
Param:  poly enum-bool  -  n 		if draw polygons 
Param:  polyneg enum-bool  -  n 		if polygons for negative values 
Param:  seemean enum-bool  -  n 		if y, plot mean lines of traces 
Param:  transp enum-bool  -  n 		if y, transpose the axes 
Param:  verb enum-bool  -  n 		verbosity flag 
Param:  xmask int  -  1 		polygon filling 
Param:  xmax float  -   -  		maximum trace position (if using xpos) 
Param:  xmin float  -   -  		minimum trace position (if using xpos) 
Param:  xpos string  -   -  		optional header file with trace positions (auxiliary input file name)
Param:  xreverse enum-bool  -  n 		if y, reverse the horizontal axis 
Param:  ymask int  -  1 		polygon filling 
Param:  yreverse enum-bool  -  n 		if y, reverse the vertical axis 
Param:  zplot float  -  0.75 		vertical separation 

