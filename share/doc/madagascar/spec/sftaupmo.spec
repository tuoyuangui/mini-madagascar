[sftaupmo]
Cat:    RSF/system/seismic
Desc:   Normal moveout in tau-p domain
DocCmd: sftaupmo | cat
Port:   stdin  rsf r req 	RSF standard input (containing taup data)
Port:   stdout rsf w req 	RSF standard output (containing nmod data)
Port:   velocity rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  extend int  -  4 		interpolation accuracy 
Param:  interval enum-bool  -  y 		use interval velocity 
Param:  mute int  -  12 		mute zone 
Param:  slope string  -   -  		auxiliary input file name
Param:  str float  -  0.5 		maximum stretch 
Param:  velx string  -   -  		auxiliary input file name

