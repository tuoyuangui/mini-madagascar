[sfthplot]
Cat:    RSF/plot/main
Desc:   Hidden-line surface plot
DocCmd: sfthplot | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout vpl w req 	VPL standard output (containing plot data)
Param:  alpha float  -  45. 		apparent angle in degrees, |alpha| < 89 
Param:  axis enum-bool  -  y 		
Param:  axis1 enum-bool  -  y 		
Param:  axis2 enum-bool  -  y 		
Param:  axis3 enum-bool  -  y 		plot axis 
Param:  axisfat int  -  2 		axes fatness 
Param:  axissz int  -  6 		axes size 
Param:  bias float  -  0. 		subtract bias from data 
Param:  clip float  -  0. 		data clip 
Param:  dclip float  -  1. 		change the clip: clip *= dclip 
Param:  dflag enum-bool  -  y 		if y, plot down side of the surface 
Param:  gainstep int  -   -  		subsampling for gpow and clip estimation 
LDesc:  (defaults to: 0.5+nx/256.)
Param:  norm enum-bool  -  y 		normalize by the clip 
Param:  pclip float  -  100. 		data clip percentile 
Param:  plotcoldn int  -   -  		color of the lower side 
LDesc:  (defaults to: VP_RED)
Param:  plotcolup int  -   -  		color of the upper side 
LDesc:  (defaults to: VP_YELLOW)
Param:  plotfat int  -  0 		line fatness 
Param:  ratio float  -  5. 		plot adjustment 
Param:  sz float  -  6. 		vertical scale 
Param:  title string  -   -  		
Param:  titlefat int  -  2 		title fatness 
Param:  titlsz int  -  9 		title size 
Param:  uflag enum-bool  -  y 		if y, plot upper side of the surface 
Param:  wanttitle enum-bool  -  y 		
Param:  xc float  -  1.5 		
Param:  zc float  -  3 		lower left corner of the plot 
Param:  zmax float  -   -  		
Param:  zmin float  -   -  		

