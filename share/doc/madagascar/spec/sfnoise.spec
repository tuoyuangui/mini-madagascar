[sfnoise]
Cat:    RSF/system/generic
Desc:   Add random noise to the data
DocCmd: sfnoise | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  mean float  -  0 		noise mean 
Param:  range float  -   -  		noise range (default=1) 
Param:  rep enum-bool  -  n 		if y, replace data with noise 
Param:  seed int  -   -  		
LDesc:  (defaults to: time(NULL))
Param:  type enum-bool  -  y 		noise distribution, y: normal, n: uniform 
Param:  var float  -   -  		noise variance 

