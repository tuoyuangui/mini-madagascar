[sfmodrefl]
Cat:    RSF/system/seismic
Desc:   Normal reflectivity modeling
DocCmd: sfmodrefl | cat
Port:   stdin  rsf r req 	RSF standard input (containing depth data)
Port:   stdout rsf w req 	RSF standard output (containing dat data)
Port:   rho rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   vp rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   vs rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  dt float  -   -  		time sampling 
Param:  nt int  -   -  		time samples 
Param:  nw int  -  4 		interpolation length 

