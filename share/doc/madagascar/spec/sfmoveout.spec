[sfmoveout]
Cat:    RSF/system/seismic
Desc:   Put spikes at an arbitrary moveout
DocCmd: sfmoveout | cat
Port:   stdin  rsf r req 	RSF standard input (containing warp data)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  d1 float  -  1. 		time sampling 
Param:  eps float  -  0.1 		stretch regularization 
Param:  n1 int  -   -  		time samples 
Param:  nw int  -  10 		wavelet length 
Param:  o1 float  -  0. 		time origin 

