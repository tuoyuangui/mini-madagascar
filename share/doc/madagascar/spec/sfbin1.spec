[sfbin1]
Cat:    RSF/system/generic
Desc:   Data binning in 1-D slices
DocCmd: sfbin1 | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  clip float  -   -  		clip for fold normalization 
LDesc:  (defaults to: FLT_EPSILON)
Param:  dx float  -   -  		grid spacing 
Param:  fold string  -   -  		output fold file (optional) (auxiliary output file name)
Param:  head string  -   -  		
Param:  interp int  -  1 		interpolation method, 1: nearest neighbor, 2: linear 
Param:  nx int  -   -  		Number of bins 
Param:  pattern string  -   -  		auxiliary input file name
Param:  x0 float  -   -  		grid origin 
LDesc:  (defaults to: xmin)
Param:  xmax float  -   -  		
Param:  xmin float  -   -  		grid dimensions 

