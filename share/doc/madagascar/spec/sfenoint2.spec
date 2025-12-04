[sfenoint2]
Cat:    RSF/system/generic
Desc:   ENO interpolation in 2-D slices
DocCmd: sfenoint2 | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   head rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  interp int  -  2 		interpolation order 
Param:  xkey int  -   -  		x key number 
Param:  ykey int  -   -  		y key number 

