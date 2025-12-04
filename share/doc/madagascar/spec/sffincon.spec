[sffincon]
Cat:    RSF/system/seismic
Desc:   Offset continuation by finite differences
DocCmd: sffincon | cat
Port:   stdin  rsf r req 	RSF standard input (containing input data)
Port:   stdout rsf w req 	RSF standard output (containing output data)
Param:  all enum-bool  -  n 		if y, output all offsets 
Param:  dh float  -   -  		Offset step size 
Param:  h0 float  -   -  		Initial offset 
Param:  nh int  -   -  		Number of steps in offset 

