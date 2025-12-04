[sfvscan]
Cat:    RSF/system/seismic
Desc:   Velocity analysis
DocCmd: sfvscan | cat
Port:   stdin  rsf r req 	RSF standard input (containing cmp data)
Port:   stdout rsf w req 	RSF standard output (containing scan data)
Param:  avosemblance enum-bool  -  n 		if y, compute AVO-friendly semblance 
Param:  diffsemblance enum-bool  -  n 		if y, compute differential semblance 
Param:  dv float  -   -  		step in velocity 
Param:  extend int  -  4 		trace extension 
Param:  grad string  -   -  		auxiliary input file name
Param:  half enum-bool  -  y 		if y, the second axis is half-offset instead of full offset 
Param:  mask string  -   -  		optional mask file (auxiliary input file name)
Param:  mute int  -  12 		mute zone 
Param:  nb int  -  2 		semblance averaging 
Param:  ns int  -  1 		number of heterogeneity scans 
Param:  nv int  -   -  		number of scanned velocities 
Param:  offset string  -   -  		auxiliary input file name
Param:  semblance enum-bool  -  n 		if y, compute semblance; if n, stack 
Param:  slowness enum-bool  -  n 		if y, use slowness instead of velocity 
Param:  smax float  -  2.0 		maximum heterogeneity 
Param:  squared enum-bool  -  n 		if y, the slowness or velocity is squared 
Param:  str float  -  0.5 		maximum stretch allowed 
Param:  type string  -   -  		type of semblance (avo,diff,sembl,power,weighted) 
Param:  v0 float  -   -  		first scanned velocity 
Param:  v1 float  -   -  		reference velocity 
Param:  weight enum-bool  -  y 		if y, apply pseudo-unitary weighting 

