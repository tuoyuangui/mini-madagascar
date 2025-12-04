[sfconstfdmig2]
Cat:    RSF/system/seismic
Desc:   2-D implicit finite-difference migration in constant velocity
DocCmd: sfconstfdmig2 | cat
Port:   stdin  rsf r req 	RSF standard input (containing data data)
Port:   stdout rsf w req 	RSF standard output (containing imag data)
Param:  dz float  -   -  		vertical time sampling 
LDesc:  (defaults to: 1./(nz*dw))
Param:  hi enum-bool  -  y 		if y, use 45-degree; n, 15-degree 
Param:  movie string  -   -  		auxiliary output file name
Param:  nz int  -   -  		vertical time samples 
LDesc:  (defaults to: 2*(nw-1))
Param:  sixth float  -  1./12 		one-sixth trick 
Param:  vel float  -   -  		constant velocity 

