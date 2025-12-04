[sfvppen]
Cat:    RSF/pens/main
Desc:   Vplot filter for the virtual vplot device
DocCmd: sfvppen | cat
Param:  align string  -   -  		aligns plot accoording to xy:
LDesc:         x is one of l, r, c, u for left, right, center, unaligned
LDesc:         y is one of b, t, c, u for bottom, top, center, unaligned.
LDesc:         In all cases the given point is aligned to have coordinate zero. 
Param:  background enum-bool  -   -  		
Param:  big enum-bool  -   -  		if y, expand the size of the device's screen (and hence
LDesc:         outermost clipping window) to nearly infinity (bad for rotated
LDesc:         style!) 
Param:  bit int  -  0 		if > 0,  then bit raster is used with bit the color 
Param:  blast enum-bool  -  y 		if y, don't try to compact the output.  If n, compaction will
LDesc:         be done.  Compaction does run-length encoding and compacts repeated
LDesc:         lines.  Compaction can make the vplot file considerably smaller, but
LDesc:         it also takes longer to create the file. 
Param:  blue float-list  -   -  		 [4]
Param:  bluepow float  -  1.0 		
Param:  break string  -   -  		
Param:  cachepipe enum-bool  -   -  		
Param:  colormask enum-bool-list  -   -  		 [5]
Param:  dashscale float  -  1.0 		
Param:  dither int  -   -  		dithering to improve raster display, see 'man vplotraster'
LDesc:                      0    No dither,
LDesc:                      1    Random Dither
LDesc:                      2    Ordered Dither
LDesc:                      3    Minimized Average Error Method
LDesc:                      4    Digital Halftoning 
Param:  dumb enum-bool  -  n 		if y, causes output to only be vectors, erases, and color changes 
Param:  endpause enum-bool  -   -  		
Param:  erase string  -   -  		
Param:  fat int  -  0 		base line fatness 
Param:  fatmult float  -   -  		
Param:  frame enum-bool  -   -  		
Param:  green float-list  -   -  		 [4]
Param:  greenpow float  -  1.0 		
Param:  greyc float  -  1.0 		'grey correction' modifies the grey scale used to display a raster to simulate the nonlinearity of displays, see 'man vplotraster' 
Param:  grid int  -  -1 		turns on drawing a grid, with the specified fatness 
Param:  gridnum int-list  -   -  		grids the screen, each part has gridsize=xwidth,ywidth
LDesc:        numy defaults to numx. [xy]size default to [xy]screensize /
LDesc:        num[xy]  [2]
Param:  gridsize float-list  -   -  		 [2]
Param:  interact string  -   -  		
Param:  invras enum-bool  -   -  		
Param:  mkscale float  -  1.0 		
Param:  mono enum-bool  -  n 		no color 
Param:  out# string  -   -  		redirect frame # to corresponding file 
Param:  outN string  -   -  		
Param:  overlay enum-bool  -   -  		
Param:  patternmult float  -  1. 		
Param:  pause int  -  0 		
Param:  pixc float  -  1.0 		'pixel  correction' controls  alteration of the grey scale, see 'man vplotraster'. 
Param:  red float-list  -   -  		 [4]
Param:  redpow float  -  1.0 		
Param:  rotate int  -  0 		
Param:  scale float  -  1.0 		
Param:  serifs enum-bool  -   -  		
Param:  shade enum-bool  -   -  		
Param:  size string  -   -  		
Param:  stat string  -   -  		if y, print plot statistics; if l, insert extra spaces
Param:  style string  -   -  		
Param:  txfont int  -   -  		
Param:  txovly int  -   -  		
Param:  txprec int  -   -  		
Param:  txscale float  -  1.0 		
Param:  txsquare enum-bool  -   -  		
Param:  vpstyle enum-bool  -   -  		if n, omit declaring absolute style in the output file 
Param:  wantras enum-bool  -   -  		
Param:  window enum-bool  -   -  		
Param:  xcenter float  -   -  		
Param:  xscale float  -  1.0 		
Param:  xshift float  -  0. 		
Param:  xsize float  -  0. 		
Param:  xwmax float  -   -  		
Param:  xwmin float  -   -  		
Param:  ycenter float  -   -  		
Param:  yscale float  -  1.0 		
Param:  yshift float  -  0. 		
Param:  ysize float  -  0. 		scale the vplot image to fit within a given size rectangle 
Param:  ywmax float  -   -  		
Param:  ywmin float  -   -  		

