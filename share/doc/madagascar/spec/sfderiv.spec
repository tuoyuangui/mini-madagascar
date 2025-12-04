[sfderiv]
Cat:    RSF/system/generic
Desc:   First derivative with a maximally linear FIR differentiator
DocCmd: sfderiv | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  order int  -  6 		filter order 
Param:  scale enum-bool  -  n 		if scale by 1/dx 

