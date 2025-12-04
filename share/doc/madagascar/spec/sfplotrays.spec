[sfplotrays]
Cat:    RSF/plot/main
Desc:   Plot rays
DocCmd: sfplotrays | cat
Port:   stdin  rsf r req 	RSF standard input (containing rays data)
Port:   stdout vpl w req 	VPL standard output (containing plot data)
Param:  frame string  -   -  		auxiliary input file name
Param:  jr int  -  1 		skip rays 
Param:  nt int  -   -  		maximum ray length 
LDesc:  (defaults to: n1*n2)

