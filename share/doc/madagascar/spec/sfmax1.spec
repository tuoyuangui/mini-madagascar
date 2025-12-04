[sfmax1]
Cat:    RSF/system/generic
Desc:   Picking local maxima on the first axis
DocCmd: sfmax1 | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  max float  -   -  		maximum value of time 
LDesc:  (defaults to: o1+(n1-1)*d1)
Param:  min float  -   -  		minimum value of time 
LDesc:  (defaults to: o1)
Param:  np int  -   -  		maximum number of picks 
LDesc:  (defaults to: n1)
Param:  sorted enum-bool  -  y 		if y, sort by amplitude 

