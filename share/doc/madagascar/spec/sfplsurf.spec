[sfplsurf]
Cat:    RSF/plot/plplot
Desc:   Generate a surface plot
DocCmd: sfplsurf | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Param:  alt float  -  35.0 		altitude [0;90] 
Param:  az float  -  25.0 		azimuth 
Param:  bcontour enum-bool  -  n 		draw contour lines at the bottom 
Param:  color string  -   -  		color scheme (default is i) 
Param:  faceted enum-bool  -  n 		each cell is faceted on the surface (surface mode only) 
Param:  font int  -  2 		font 
Param:  label1 string  -   -  		
Param:  label2 string  -   -  		
Param:  label3 string  -   -  		
Param:  labelfat int  -  1 		label fatness 
Param:  labelsz float  -  8.0 		label font size 
Param:  maxval float  -   -  		maximum value for the vertical axis (default is data maximum) 
LDesc:  (defaults to: -SF_HUGE)
Param:  mesh enum-bool  -  y 		what to draw: true - mesh, false - shaded surface 
Param:  meshc int  -   -  		mesh color or surface contour color 
LDesc:  (defaults to: VP_YELLOW)
Param:  minval float  -   -  		minimum value for the vertical axis (default is data minimum) 
LDesc:  (defaults to: SF_HUGE)
Param:  nc int  -  10 		number of contour lines 
Param:  scontour enum-bool  -  n 		draw contour lines on the surface (surface mode only) 
Param:  sides enum-bool  -  n 		draw sides 
Param:  title string  -   -  		
Param:  titlefat int  -  1 		title fatness 
Param:  titlesz float  -  10.0 		title font size 
Param:  unit1 string  -   -  		
Param:  unit2 string  -   -  		
Param:  unit3 string  -   -  		
Param:  wantaxis enum-bool  -  y 		if generate axes with ticks and labels 
Param:  wantaxis1 enum-bool  -  y 		
Param:  wantaxis2 enum-bool  -  y 		
Param:  wantaxis3 enum-bool  -  y 		
Param:  wanttitle enum-bool  -  y 		if include title 
Param:  wheretitle string  -   -  		where to put title (top,bottom) 

