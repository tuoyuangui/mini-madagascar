[sfdots]
Cat:    RSF/plot/main
Desc:   Plot signal with lollipops
DocCmd: sfdots | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout vpl w req 	VPL standard output (containing plot data)
Param:  clip float  -  -1. 		data clip 
Param:  connect int  -  1 		connection type: 1 - diagonal, 2 - bar, 4 - only for non-zero data 
Param:  constsep enum-bool  -  n 		if y, use constant trace separation 
Param:  corners int  -   -  		number of polygon corners (default is 6) 
Param:  dots int  -   -  		type of dots: 1 - baloon, 0 - no dots, 2 - only for non-zero data 
LDesc:  (defaults to: (n1 <= 130)? 1: 0)
Param:  font int  -  -1 		font to use in text 
Param:  gaineach enum-bool  -  y 		if y, gain each trace independently 
Param:  label1 string  -   -  		label for the axis
Param:  labels string-list  -   -  		trace labels  [n2]
Param:  labelsz int  -  8 		label size 
Param:  overlap float  -  0.9 		trace overlap 
Param:  radius float  -   -  		dot radius 
LDesc:  (defaults to: dd1/3)
Param:  screenht float  -   -  		screen height 
LDesc:  (defaults to: VP_STANDARD_HEIGHT)
Param:  screenratio float  -   -  		screen aspect ratio 
LDesc:  (defaults to: VP_SCREEN_RATIO)
Param:  screenwd float  -   -  		screen width 
LDesc:  (defaults to: screenhigh / screenratio)
Param:  seedead enum-bool  -  n 		if y, show zero traces 
Param:  seemean enum-bool  -   -  		if y, draw axis lines 
LDesc:  (defaults to: (bool) (n2 <= 30))
Param:  silk enum-bool  -  n 		if y, silky plot 
Param:  strings enum-bool  -   -  		if y, draw strings 
LDesc:  (defaults to: (bool) (n1 <= 400))
Param:  title string  -   -  		plot title
Param:  transp enum-bool  -  n 		if y, transpose the axis 
Param:  unit1 string  -   -  		unit for the axis
Param:  xxscale float  -  1. 		x scaling 
Param:  yreverse enum-bool  -  n 		if y, reverse y axis 
Param:  yyscale float  -  1. 		y scaling 

