[sfunif3]
Cat:    RSF/system/generic
Desc:   Generate 3-D layered velocity model from specified interfaces
DocCmd: sfunif3 | cat
Port:   stdin  rsf r req 	RSF standard input (containing surface data)
Port:   stdout rsf w req 	RSF standard output (containing model data)
Param:  d1 float  -   -  		Sampling of the depth axis 
Param:  dvdx float-list  -   -  		 [ninf]
Param:  dvdy float-list  -   -  		 [ninf]
Param:  dvdz float-list  -   -  		 [ninf]
Param:  layers string  -   -  		file with layer properties 
Param:  n1 int  -   -  		Number of samples on the depth axis 
Param:  o1 float  -  0. 		Origin of the depth axis 
Param:  v00 float-list  -   -  		 [ninf]
Param:  x0 float-list  -   -  		 [ninf]
Param:  y0 float-list  -   -  		 [ninf]
Param:  z0 float-list  -   -  		 [ninf]

