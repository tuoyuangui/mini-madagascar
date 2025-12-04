[sfigrad]
Cat:    RSF/system/generic
Desc:   Gradient on the first axis
DocCmd: sfigrad | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  adj enum-bool  -  n 		adjoint flag 
Param:  square enum-bool  -  n 		if y, use gradient squared 

