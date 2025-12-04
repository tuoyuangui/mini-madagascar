[sfheadermath]
Cat:    RSF/system/seismic
Desc:   Mathematical operations, possibly on header keys
DocCmd: sfheadermath | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  key string  -   -  		key to replace 
Param:  memsize int  -   -  		Max amount of RAM (in Mb) to be used 
LDesc:  (defaults to: sf_memsize())
Param:  nkey int  -  -1 		number of key to replace 
Param:  output string  -   -  		Describes the output in a mathematical notation. 
Param:  segy enum-bool  -  y 		if SEGY headers 

