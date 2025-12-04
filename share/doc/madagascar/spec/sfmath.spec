[sfmath]
Cat:    RSF/system/main
Desc:   Mathematical operations on data files
DocCmd: sfmath | cat
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  d# float  -   -  		sampling on #-th axis 
LDesc:  (defaults to: (1,1,...))
Param:  label string  -   -  		data label 
Param:  label# string  -   -  		label on #-th axis 
Param:  n# largeint  -   -  		size of #-th axis 
Param:  nostdin enum-bool  -  n 		y - ignore stdin 
Param:  o# float  -   -  		origin on #-th axis 
LDesc:  (defaults to: (0,0,...))
Param:  output string  -   -  		Mathematical description of the output 
Param:  type string  -   -  		output data type [float,complex] 
Param:  unit string  -   -  		data unit 
Param:  unit# string  -   -  		unit on #-th axis 

