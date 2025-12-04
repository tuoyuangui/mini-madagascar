[sfwindow]
Cat:    RSF/system/main
Desc:   Window a portion of a dataset
DocCmd: sfwindow | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  d# float  -   -  		sampling in #-th dimension 
LDesc:  (defaults to: (d1,d2,...))
Param:  f# largeint  -   -  		window start in #-th dimension 
LDesc:  (defaults to: (0,...))
Param:  j# int  -   -  		jump in #-th dimension 
LDesc:  (defaults to: (1,...))
Param:  max# float  -   -  		maximum in #-th dimension 
LDesc:  (defaults to: (o1+(n1-1)*d1,o2+(n1-1)*d2,,...))
Param:  min# float  -   -  		minimum in #-th dimension 
LDesc:  (defaults to: (o1,o2,,...))
Param:  n# largeint  -   -  		window size in #-th dimension 
LDesc:  (defaults to: (0,...))
Param:  squeeze enum-bool  -  y 		if y, squeeze dimensions equal to 1 to the end 
Param:  verb enum-bool  -  n 		Verbosity flag 

