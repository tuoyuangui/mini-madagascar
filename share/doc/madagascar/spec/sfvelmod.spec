[sfvelmod]
Cat:    RSF/system/seismic
Desc:   Velocity transform
DocCmd: sfvelmod | cat
Port:   stdin  rsf r req 	RSF standard input (containing scan data)
Port:   stdout rsf w req 	RSF standard output (containing cmp data)
Param:  extend int  -  4 		trace extension 
Param:  half enum-bool  -  y 		if y, the second axis is half-offset instead of full offset 
Param:  slowness enum-bool  -  n 		if y, use slowness instead of velocity 

