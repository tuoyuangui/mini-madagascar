[sfsegywrite]
Cat:    RSF/system/seismic
Desc:   Convert an RSF dataset to SEGY or SU
DocCmd: sfsegywrite | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   tfile rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  bfile string  -   -  		input binary data header file 
Param:  endian enum-bool  -  y 		Whether to automatically estimate endianness or not 
Param:  hfile string  -   -  		input text data header file 
Param:  su enum-bool  -   -  		y if input is SU, n if input is SEGY 
Param:  suxdr enum-bool  -  n 		y, SU has XDR support 
Param:  tape string  -   -  		output data 
Param:  verb enum-bool  -  n 		Verbosity flag 

