[sfcat]
Cat:    RSF/system/main
Desc:   Concatenate datasets
DocCmd: sfcat | cat
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  axis int  -  3 		Axis being merged 
Param:  d float  -   -  		axis sampling 
Param:  nspace int  -   -  		if space=y, number of traces to insert 
LDesc:  (defaults to: (int) (ni/(20*nin) + 1))
Param:  o float  -   -  		axis origin 
Param:  order int-list  -   -  		concatenation order  [nin]
Param:  space enum-bool  -   -  		Insert additional space.
LDesc:  	   y is default for sfmerge, n is default for sfcat 

