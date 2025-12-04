[sfstoltstretch]
Cat:    RSF/system/seismic
Desc:   Stolt stretch
DocCmd: sfstoltstretch | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (containing st data)
Port:   velocity rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  eps float  -  0.01 		stretch regularization 
Param:  inv enum-bool  -  n 		if y, inverse stretch 
Param:  nstretch int  -  1 		number of steps 
Param:  pad int  -   -  		time axis padding 
LDesc:  (defaults to: nt)
Param:  vel float  -   -  		reference velocity 

