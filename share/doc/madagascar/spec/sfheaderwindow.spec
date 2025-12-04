[sfheaderwindow]
Cat:    RSF/system/main
Desc:   Window a dataset based on a header mask
DocCmd: sfheaderwindow | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   mask rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  inv enum-bool  -  n 		inversion flag 

