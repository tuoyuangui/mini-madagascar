[sfbox]
Cat:    RSF/plot/main
Desc:   Draw a balloon-style label
DocCmd: sfbox | cat
Port:   stdout vpl w req 	VPL standard output (no hint on content)
Param:  angle float  -  0. 		longitude of floating label in 3-D 
Param:  boxit enum-bool  -  y 		if y, create a box around text 
Param:  font int  -   -  		text font 
LDesc:  (defaults to: VP_NO_CHANGE)
Param:  lab_color int  -   -  		label color 
LDesc:  (defaults to: VP_WHITE)
Param:  lab_fat int  -  0 		label fatness 
Param:  label string  -   -  		text for label 
Param:  lat float  -  0. 		latitude of viewpoint in 3-D 
Param:  length float  -   -  		normalization for xt and yt 
Param:  long float  -  90. 		longitude of viewpoint in 3-D 
Param:  pointer enum-bool  -  y 		if y, create arrow pointer 
Param:  pscale float  -  1. 		scale factor for width of pointer 
Param:  reverse enum-bool  -  n 		if reverse 
Param:  scale0 float  -  1. 		scale factor for x0 and y0 
Param:  scalet float  -   -  		( scalet scale factor for xt and yt (if length is not set) )
Param:  size float  -  .25 		text height in inches 
Param:  x0 float  -  0. 		x position of the pointer tip 
Param:  x_oval float  -  0. 		x size of the oval around pointer 
Param:  xt float  -  2. 		relative position of text in x 
Param:  y0 float  -  0. 		y position of the pointer tip 
Param:  y_oval float  -  0. 		y size of the oval around pointer 
Param:  yt float  -  0. 		relative position of text in y 

