[sfpspen]
Cat:    RSF/pens/main
Desc:   Vplot filter for Postscript
DocCmd: sfpspen | cat
Param:  background enum-bool  -   -  		
Param:  blue float-list  -   -  		 [4]
Param:  bluepow float  -  1.0 		
Param:  break string  -   -  		
Param:  cachepipe enum-bool  -   -  		
Param:  color enum-bool  -  n 		use color 
Param:  colormask enum-bool-list  -   -  		 [5]
Param:  copies int  -  1 		number of copies 
Param:  corners enum-bool  -  y 		n - remove 'corner' group. 
Param:  dashscale float  -  1.0 		
Param:  dither int  -   -  		dithering to improve raster display, see 'man vplotraster'
LDesc:                      0    No dither,
LDesc:                      1    Random Dither
LDesc:                      2    Ordered Dither
LDesc:                      3    Minimized Average Error Method
LDesc:                      4    Digital Halftoning 
Param:  dumbfat enum-bool  -  n 		
Param:  endpause enum-bool  -   -  		
Param:  erase string  -   -  		
Param:  fat int  -  0 		base line fatness 
Param:  fatmult float  -   -  		
Param:  force enum-bool  -  n 		if y, don't replace colors with their compliments 
Param:  force_raster enum-bool  -  y 		if y, don't replace raster colors with their compliments 
Param:  forcebw enum-bool  -  n 		if y, don't replace black and white colors with their compliments 
Param:  frame enum-bool  -   -  		
Param:  green float-list  -   -  		 [4]
Param:  greenpow float  -  1.0 		
Param:  greyc float  -  1.0 		'grey correction' modifies the grey scale used to display a raster to simulate the nonlinearity of displays, see 'man vplotraster' 
Param:  hold enum-bool  -  n 		tells the printer to not print the job until you
LDesc:         add paper through the manual feed slot 
Param:  interact string  -   -  		
Param:  invras enum-bool  -   -  		
Param:  label string  -   -  		label for pages, default is user name and date
Param:  mkscale float  -  1.0 		
Param:  mono enum-bool  -  n 		no color 
Param:  overlay enum-bool  -   -  		
Param:  paper string  -   -  		
Param:  patternmult float  -  1. 		
Param:  pause int  -  0 		
Param:  pixc float  -  1.0 		'pixel  correction' controls  alteration of the grey scale, see 'man vplotraster'. 
Param:  ppi float  -   -  		pixels per inch 
Param:  printer string  -   -  		what printer to send it to 
Param:  red float-list  -   -  		 [4]
Param:  redpow float  -  1.0 		
Param:  rgb enum-bool  -  y 		For figures turned into GEOPHYSICS, use 'rgb=no'. 
Param:  rotate int  -  0 		
Param:  scale float  -  1.0 		
Param:  serifs enum-bool  -   -  		
Param:  shade enum-bool  -   -  		
Param:  size string  -   -  		
Param:  style string  -   -  		
Param:  tex enum-bool  -  n 		
Param:  txfont int  -   -  		
Param:  txovly int  -   -  		
Param:  txprec int  -   -  		
Param:  txscale float  -  1.0 		
Param:  txsquare enum-bool  -   -  		
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

