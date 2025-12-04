[sfadd]
Cat:    RSF/system/main
Desc:   Add, multiply, or divide  RSF datasets
DocCmd: sfadd | cat
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  abs enum-bool-list  -   -  		If true take absolute value  [nin]
Param:  add float-list  -   -  		Scalar values to add to each dataset  [nin]
Param:  exp enum-bool-list  -   -  		If true compute exponential  [nin]
Param:  log enum-bool-list  -   -  		If true take logarithm  [nin]
Param:  mode string  -   -  		'a' means add (default), 
LDesc:  	  'p' or 'm' means multiply, 
LDesc:  	  'd' means divide 
LDesc:         
Param:  scale float-list  -   -  		Scalar values to multiply each dataset with  [nin]
Param:  sqrt enum-bool-list  -   -  		If true take square root  [nin]

