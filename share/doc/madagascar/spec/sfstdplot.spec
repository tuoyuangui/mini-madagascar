[sfstdplot]
Cat:    RSF/plot/lib
Desc:   Setting up frames for a generic plot
DocCmd: sfstdplot | cat
Param:  axiscol int  -  7 		
Param:  axisfat int  -  0 		
Param:  backcol float-list  -   -  		 [3]
Param:  barlabel string  -   -  		( barlabel bar label )(bar label)
Param:  barlabelfat int  -   -  		bar label fatness 
Param:  barlabelsz float  -   -  		bar label font size 
Param:  barmove enum-bool  -  n 		adjust scalebar position, if bartype=h 
Param:  bartype string  -   -  		[v,h] vertical or horizontal bar (default is v) 
Param:  barunit string  -   -  		( barunit bar unit )(bar unit)
Param:  barwidth float  -  0.36 		scale bar size 
Param:  crowd float  -  0.75 		
Param:  crowd1 float  -   -  		
LDesc:  (defaults to: crowd)
Param:  crowd2 float  -   -  		
LDesc:  (defaults to: crowd)
Param:  cubelinecol int  -   -  		cube lines color 
LDesc:  (defaults to: framelabelcol)
Param:  d1num float  -   -  		axis1 tic increment 
Param:  d2num float  -   -  		axis2 tic increment 
Param:  d3num float  -   -  		axis3 tic increment 
Param:  d4num float  -   -  		axis4 tic increment 
Param:  dash float-list  -   -  		line dash type	
LDesc:  	    0 continuos (default)
LDesc:  	    1 fine dash
LDesc:  	    2 fine dot
LDesc:  	    3 dash
LDesc:  	    4 large dash
LDesc:  	    5 dot dash
LDesc:  	    6 large dash small dash
LDesc:  	    7 double dot
LDesc:  	    8 double dash
LDesc:  	    9 loose dash  The part after the decimal point determines the pattern repetition interval  [n2]
Param:  dbarnum string  -   -  		scalebar tic increment 
Param:  fillcol float-list  -   -  		 [3]
Param:  font int  -  -1 		font to use in text 
Param:  format1 string  -   -  		tick mark format 
Param:  format2 string  -   -  		tickmark format ()
Param:  format3 string  -   -  		tickmark format 
Param:  formatbar string  -   -  		format for ticmark labels in the scalebar 
Param:  framelabel1 enum-bool  -   -  		to put numbers at frame ends 
LDesc:  (defaults to: (bool) (NULL != label1))
Param:  framelabel2 enum-bool  -   -  		to put numbers at frame ends 
LDesc:  (defaults to: (bool) (NULL != label2))
Param:  framelabel3 enum-bool  -   -  		to put numbers at frame ends 
LDesc:  (defaults to: (bool) (NULL != label3))
Param:  framelabelcol int  -   -  		frame labels color 
LDesc:  (defaults to: VP_YELLOW)
Param:  g1num float  -   -  		grid mark sampling on first axis 
Param:  g1num0 float  -   -  		grid mark origin on first axis 
Param:  g2num float  -   -  		grid mark sampling on second axis 
Param:  g2num0 float  -   -  		grid mark origin on second axis 
Param:  grid1 enum-bool  -   -  		to draw grid on first axis 
Param:  grid2 enum-bool  -   -  		to draw grid on second axis 
Param:  gridcol int  -   -  		grid color 
LDesc:  (defaults to: grid? VP_RED: framecol)
Param:  griddash float  -   -  		grid dash pattern 
LDesc:  (defaults to: 0.0f)
Param:  gridfat int  -  1 		grid fatness 
Param:  label1 string  -   -  		label on the first axis
Param:  label2 string  -   -  		label on the second axis
Param:  label3 string  -   -  		label on the third axis
Param:  labelfat int  -   -  		label fatness 
Param:  labelrot enum-bool  -  n 		
Param:  labelsz float  -  8. 		
Param:  larnersz float  -   -  		give the font size as a fraction of the total screen height, 
LDesc:         this is based on Ken Larner's 1/20 rule.
LDesc:         Any positive larnersz value will overwrite labelsz with 
LDesc:         the appropiate rule
LDesc:  (defaults to: 0.0f)
Param:  max1 float  -   -  		
Param:  max2 float  -   -  		
Param:  min1 float  -   -  		
Param:  min2 float  -   -  		
Param:  n1tic int  -   -  		axis1 number of ticmarks 
Param:  n2tic int  -   -  		axis2 number of ticmarks 
Param:  n3tic int  -   -  		axis3 number of ticmarks 
Param:  n4tic int  -   -  		axis4 number of ticmarks 
Param:  nbartic int  -   -  		number of scalebar ticmarks 
Param:  o1num float  -   -  		axis1 tic origin 
Param:  o2num float  -   -  		axis2 tic origin 
Param:  o3num float  -   -  		axis3 tic origin 
Param:  o4num float  -   -  		axis4 tic origin 
Param:  obarnum float  -   -  		scalebar tic origin 
Param:  pad enum-bool  -   -  		pad plotting area 
LDesc:  (defaults to: pad1)
Param:  plotcol int-list  -   -  		line color 
LDesc:  	   7 white
LDesc:  	   6 yellow (default)
LDesc:  	   5 cyan
LDesc:  	   4 green
LDesc:  	   3 magenta
LDesc:  	   2 red
LDesc:  	   1 blue
LDesc:  	   0 black  [n2]
Param:  plotfat int-list  -   -  		line fatness  [n2]
Param:  scalebar enum-bool  -  n 		plot a scalebar 
Param:  screenht float  -   -  		
LDesc:  (defaults to: VP_STANDARD_HEIGHT)
Param:  screenratio float  -   -  		
LDesc:  (defaults to: VP_SCREEN_RATIO)
Param:  screenwd float  -   -  		
LDesc:  (defaults to: screenht / screenratio)
Param:  tickscale float  -  0.5 		ticks scaling 
Param:  tickscale1 float  -   -  		ticks scaling on first axis 
LDesc:  (defaults to: tickscale)
Param:  tickscale2 float  -   -  		ticks scaling on second axis 
LDesc:  (defaults to: tickscale)
Param:  tickscale3 float  -   -  		ticks scaling on third axis 
LDesc:  (defaults to: tickscale)
Param:  tickscale4 float  -   -  		ticks scaling on fourth axis 
LDesc:  (defaults to: tickscale)
Param:  title string  -   -  		( title plot title )(plot title)
Param:  titlefat int  -  0 		
Param:  titlesz float  -  10. 		
Param:  transp enum-bool  -   -  		
LDesc:  (defaults to: transp1)
Param:  unit1 string  -   -  		unit on the first axis
Param:  unit2 string  -   -  		unit on the second axis
Param:  unit3 string  -   -  		unit on the third axis
Param:  wantaxis enum-bool  -   -  		if draw axes 
Param:  wantaxis1 enum-bool  -   -  		if draw first axis 
Param:  wantaxis2 enum-bool  -   -  		if draw second axis 
Param:  wantaxis3 enum-bool  -   -  		if draw third axis in cube plots 
Param:  wanttitle enum-bool  -  y 		
Param:  wherebarlabel string  -   -  		where to put bar label (top,bottom,left,right) 
Param:  wherebartics string  -   -  		( wherebartics where to put scalebar ticmarks )(where to put scalebar ticmarks)
Param:  wheretics string  -   -  		( wheretics where to put ticmarks )(where to put ticmarks)
Param:  wheretitle string  -   -  		where to put title (top,bottom,left,right)
Param:  wherexlabel string  -   -  		where to put horizontal axis (top,bottom)
Param:  whereylabel string  -   -  		checking to see if wantaxis is fetched (where to put vertical label (left,right))
Param:  xinch float  -   -  		
Param:  xll float  -   -  		
Param:  xreverse enum-bool  -  n 		
Param:  xur float  -   -  		
Param:  yinch float  -   -  		
Param:  yll float  -   -  		
Param:  yreverse enum-bool  -   -  		
LDesc:  (defaults to: yreverse1)
Param:  yur float  -   -  		

