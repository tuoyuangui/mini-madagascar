[sfgraph]
Cat:    RSF/plot/main
Desc:   Graph plot
DocCmd: sfgraph | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Param:  bar string  -   -  		file for scalebar data 
Param:  barreverse enum-bool  -  n 		if y, go from small to large on the bar scale 
Param:  color string  -   -  		color scheme (default is j) 
Param:  depth string  -   -  		auxiliary input file name
Param:  maxval float  -   -  		maximum value for scalebar (default is the data maximum) 
Param:  minval float  -   -  		minimum value for scalebar (default is the data minimum) 
Param:  nreserve int  -  8 		reserved colors 
Param:  pclip float  -  100. 		clip percentile 
Param:  scalebar enum-bool  -  n 		if y, draw scalebar 
Param:  symbol string  -   -  		if set, plot with symbols instead of lines 
Param:  symbolsz float-list  -   -  		symbol size (default is 2)  [n2]
Param:  transp enum-bool  -  n 		if y, transpose the axes 
Param:  wantframenum enum-bool  -   -  		if y, display third axis position in the corner 
LDesc:  (defaults to: (bool) (n3 > 1))

