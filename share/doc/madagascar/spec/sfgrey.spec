[sfgrey]
Cat:    RSF/plot/main
Desc:   Generate raster plot
DocCmd: sfgrey | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  allpos enum-bool  -  n 		if y, assume positive data 
Param:  bar string  -   -  		file for scalebar data 
Param:  barreverse enum-bool  -  n 		if y, go from small to large on the bar scale 
Param:  bias float  -  0. 		value mapped to the center of the color table 
Param:  clip float  -   -  		data clip 
Param:  color string  -   -  		color scheme (default is i) 
Param:  gainpanel string  -   -  		gain reference: 'a' for all, 'e' for each, or number 
Param:  gainstep int  -   -  		subsampling for gpow and clip estimation 
LDesc:  (defaults to: 0.5+n1/256.)
Param:  gpow float  -  1 		raise data to gpow power for display 
Param:  maxval float  -   -  		maximum value for scalebar (default is the data maximum) 
Param:  mean enum-bool  -  n 		if y, bias on the mean value 
Param:  minval float  -   -  		minimum value for scalebar (default is the data minimum) 
Param:  nreserve int  -  8 		reserved colors 
Param:  pclip float  -   -  		data clip percentile (default is 99) 
Param:  phalf float  -   -  		percentage for estimating gpow 
Param:  polarity enum-bool  -  n 		if y, reverse polarity (white is high by default) 
Param:  scalebar enum-bool  -  n 		if y, draw scalebar 
Param:  symcp enum-bool  -  n 		if y, assume symmetric color palette of 255 colors 
Param:  transp enum-bool  -  y 		if y, transpose the display axes 
Param:  verb enum-bool  -  n 		verbosity flag 
Param:  wantframenum enum-bool  -   -  		if y, display third axis position in the corner 
LDesc:  (defaults to: (bool) (n3 > 1))
Param:  xreverse enum-bool  -  n 		if y, reverse the horizontal axis 
Param:  yreverse enum-bool  -  y 		if y, reverse the vertical axis 

