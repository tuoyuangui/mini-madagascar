[sfstacks]
Cat:    RSF/system/seismic
Desc:   Constant-velocity stacks
DocCmd: sfstacks | cat
Port:   stdin  rsf r req 	RSF standard input (containing cmp data)
Port:   stdout rsf w req 	RSF standard output (containing stk data)
Param:  CDPtype int  -   -  		
Param:  dv float  -   -  		step in velocity 
Param:  extend int  -  4 		trace extension 
Param:  h0 float  -  0. 		reference offset 
Param:  half enum-bool  -  y 		if y, the second axis is half-offset instead of full offset 
Param:  mask string  -   -  		auxiliary input file name
Param:  mute int  -  12 		mute zone 
Param:  nv int  -   -  		number of velocities 
Param:  offset string  -   -  		auxiliary input file name
Param:  slowness enum-bool  -  n 		if y, use slowness instead of velocity 
Param:  squared enum-bool  -  n 		if y, the slowness or velocity is squared 
Param:  str float  -  0.5 		maximum stretch allowed 
Param:  v0 float  -   -  		first velocity 

