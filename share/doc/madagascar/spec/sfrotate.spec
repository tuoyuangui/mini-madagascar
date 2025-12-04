[sfrotate]
Cat:    RSF/system/main
Desc:   Rotate a portion of one or more axes in the data hypercube
DocCmd: sfrotate | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  memsize int  -   -  		Max amount of RAM (in Mb) to be used 
LDesc:  (defaults to: sf_memsize())
Param:  rot# int  -   -  		length of #-th axis that is moved to the end 
LDesc:  (defaults to: (0,0,...))
Param:  verb enum-bool  -  n 		Verbosity flag 

