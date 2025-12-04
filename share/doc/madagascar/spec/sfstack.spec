[sfstack]
Cat:    RSF/system/main
Desc:   Stack a dataset over one of the dimensions
DocCmd: sfstack | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  axis int  -  2 		which axis to stack. If axis=0, stack over all dimensions 
Param:  max enum-bool  -  n 		If y, find maximum instead of stack. Ignores rms and norm. 
Param:  min enum-bool  -  n 		If y, find minimum instead of stack. Ignores rms and norm. 
Param:  norm enum-bool  -  y 		If y, normalize by fold. 
Param:  prod enum-bool  -  n 		If y, find product instead of stack. Ignores rms and norm. 
Param:  rms enum-bool  -  n 		If y, compute the root-mean-square instead of stack. 
Param:  scale float-list  -   -  		 [nAXIS]

