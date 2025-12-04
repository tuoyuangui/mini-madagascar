[sfreg2tri]
Cat:    RSF/system/generic
Desc:   Decimate a regular grid to triplets for triangulation
DocCmd: sfreg2tri | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  edgeout string  -   -  		auxiliary output file name
Param:  nt int  -   -  		number of triplets 
Param:  zero float  -  0. 		level surface 

