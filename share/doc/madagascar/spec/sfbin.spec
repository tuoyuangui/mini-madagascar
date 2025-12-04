[sfbin]
Cat:    RSF/system/generic
Desc:   Data binning in 2-D slices
DocCmd: sfbin | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  clip float  -   -  		clip for fold normalization 
LDesc:  (defaults to: FLT_EPSILON)
Param:  dx float  -   -  		bin size in x 
Param:  dy float  -   -  		bin size in y 
Param:  fold string  -   -  		output file for fold (optional) (auxiliary output file name)
Param:  head string  -   -  		header file 
Param:  interp int  -  1 		interpolation method;
LDesc:         0: median, 1: nearest neighbor, 2: bi-linear,  
Param:  norm enum-bool  -  y 		if normalize 
Param:  nx int  -   -  		Number of bins in x 
LDesc:  (defaults to: (int) (xmax - xmin + 1.))
Param:  ny int  -   -  		Number of bins in y 
LDesc:  (defaults to: (int) (ymax - ymin + 1.))
Param:  x0 float  -   -  		x origin 
LDesc:  (defaults to: xmin)
Param:  xkey int  -  0 		x key number 
Param:  xmax float  -   -  		x maximum 
Param:  xmin float  -   -  		x minimum 
Param:  y0 float  -   -  		y origin 
LDesc:  (defaults to: ymin)
Param:  ykey int  -  1 		y key number 
Param:  ymax float  -   -  		y maximum 
Param:  ymin float  -   -  		y minimum 

