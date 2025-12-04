[sfinfill]
Cat:    RSF/system/seismic
Desc:   Shot interpolation
DocCmd: sfinfill | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  eps float  -  0.1 		regularization parameter 
Param:  positive enum-bool  -  y 		initial offset orientation 

