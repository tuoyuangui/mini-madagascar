[sfextract]
Cat:    RSF/system/generic
Desc:   Forward interpolation in 2-D slices
DocCmd: sfextract | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   head rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  interp int  -  2 		interpolation method, 1: nearest neighbor, 2: bi-linear 
Param:  xkey int  -  0 		x key number 
Param:  ykey int  -  1 		y key number 

