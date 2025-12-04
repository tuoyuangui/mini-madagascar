[sfxtpen]
Cat:    RSF/pens/main
Desc:   Vplot filter for X windows using the X Toolkit (Xt)
DocCmd: sfxtpen | cat
Param:  aspect float  -   -  		aspect ratio 
Param:  background enum-bool  -   -  		
Param:  bgcolor string  -   -  		background color 
Param:  blue float-list  -   -  		 [4]
Param:  bluepow float  -  1.0 		
Param:  boxy enum-bool  -  n 		output coordinates and labels suitable for sfbox 
Param:  break string  -   -  		
Param:  buttons enum-bool  -   -  		if y, display a panel of buttons on top of the plot 
LDesc:  (defaults to: (bool) app_data.buttons)
Param:  cachepipe enum-bool  -   -  		
Param:  colormask enum-bool-list  -   -  		 [5]
Param:  dashscale float  -  1.0 		
Param:  depth int  -   -  		Choose a visual 
LDesc:  (defaults to: app_data.vis_depth)
Param:  dither int  -   -  		dithering to improve raster display, see 'man vplotraster'
LDesc:                      0    No dither,
LDesc:                      1    Random Dither
LDesc:                      2    Ordered Dither
LDesc:                      3    Minimized Average Error Method
LDesc:                      4    Digital Halftoning 
Param:  endpause enum-bool  -   -  		
Param:  erase string  -   -  		
Param:  fat int  -  0 		base line fatness 
Param:  fatmult float  -   -  		
Param:  frame enum-bool  -   -  		
Param:  green float-list  -   -  		 [4]
Param:  greenpow float  -  1.0 		
Param:  greyc float  -  1.0 		'grey correction' modifies the grey scale used to display a raster to simulate the nonlinearity of displays, see 'man vplotraster' 
Param:  images enum-bool  -   -  		copy the image created by plotting each frame and save it in
LDesc:         the client program (xtpen). This will increase memory usage in
LDesc:         the machine that runs the pen command. If you have a fast
LDesc:         connection to your X-server it will make redisplay of frames
LDesc:         faster. If you have a slow connection, it may make replotting
LDesc:         slower. 
LDesc:  (defaults to: (bool) app_data.images)
Param:  interact string  -   -  		* save the command line arguments
Param:  invras enum-bool  -   -  		
Param:  labels enum-bool  -   -  		if y, display frame number and inter-frame delay at the top of plot 
LDesc:  (defaults to: (bool) app_data.labels)
Param:  message string  -   -  		
Param:  mkscale float  -  1.0 		
Param:  mono enum-bool  -  n 		no color 
Param:  numcol int  -   -  		number of colors (take a default from the resource database) 
LDesc:  (defaults to: app_data.num_col)
Param:  overlay enum-bool  -   -  		
Param:  patternmult float  -  1. 		
Param:  pause int  -  0 		
Param:  pixc float  -  1.0 		'pixel  correction' controls  alteration of the grey scale, see 'man vplotraster'. 
Param:  pixmaps enum-bool  -   -  		Copy the image created by plotting each frame and save it in
LDesc:         the X-server. This will increase memory usage of the machine that
LDesc:         displays the window! Redisplay of frames will be very fast and
LDesc:         the network traffic is very low so this is a suitable option for
LDesc:         slow connections.  If your X-server is a workstation with plenty
LDesc:         of memory and swap space then this option should be very useful.
LDesc:         If your X-server has limited memory, this option may have
LDesc:         undesirable effects on the response of your terminal. 
LDesc:  (defaults to: (bool) app_data.pixmaps)
Param:  ppi float  -   -  		pixels per inch 
Param:  red float-list  -   -  		 [4]
Param:  redpow float  -  1.0 		
Param:  rotate int  -  0 		
Param:  scale float  -  1.0 		
Param:  see_progress enum-bool  -  n 		show progress of each frame, slow 
Param:  serifs enum-bool  -   -  		
Param:  shade enum-bool  -   -  		
Param:  size string  -   -  		
Param:  stretchy enum-bool  -   -  		if y, use the stretchy mode and fill the window 
LDesc:  (defaults to: (bool) app_data.stretchy)
Param:  style string  -   -  		
Param:  txfont int  -   -  		
Param:  txovly int  -   -  		
Param:  txprec int  -   -  		
Param:  txscale float  -  1.0 		
Param:  txsquare enum-bool  -   -  		
Param:  want_text enum-bool  -   -  		if y, display a message window 
LDesc:  (defaults to: (bool) app_data.textpane)
Param:  wantras enum-bool  -   -  		
Param:  window enum-bool  -   -  		
Param:  xcenter float  -   -  		
Param:  xscale float  -  1.0 		
Param:  xshift float  -  0. 		
Param:  xwmax float  -   -  		
Param:  xwmin float  -   -  		
Param:  ycenter float  -   -  		
Param:  yscale float  -  1.0 		
Param:  yshift float  -  0. 		
Param:  ywmax float  -   -  		
Param:  ywmin float  -   -  		

