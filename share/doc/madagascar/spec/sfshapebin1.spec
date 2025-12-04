[sfshapebin1]
Cat:    RSF/system/generic
Desc:   1-D inverse interpolation with shaping regularization
DocCmd: sfshapebin1 | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  dx float  -   -  		grid sampling 
Param:  eps float  -   -  		regularization parameter 
LDesc:  (defaults to: 1./nd)
Param:  filter float  -  3. 		smoothing length 
Param:  gauss enum-bool  -  n 		if y, use Gaussian shaping 
Param:  head string  -   -  		
Param:  interp int  -  2 		forward interpolation method, 1: nearest neighbor, 2: linear 
Param:  niter int  -   -  		number of conjugate-gradient iterations 
LDesc:  (defaults to: nx)
Param:  nx int  -   -  		number of bins 
Param:  pad int  -  0 		padding for Gaussian shaping 
Param:  pef enum-bool  -  n 		if y, use monofrequency regularization 
Param:  verb enum-bool  -  y 		verbosity flag 
Param:  x0 float  -   -  		grid origin 
LDesc:  (defaults to: xmin)
Param:  xmax float  -   -  		
Param:  xmin float  -   -  		grid size 

