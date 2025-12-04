[sfsrseidel]
Cat:    RSF/system/seismic
Desc:   Amplitude balancing of a 2-D amplitude map
DocCmd: sfsrseidel | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (containing off data)
Port:   mid rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   rcv rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   rv rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   so rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   src rsf w  -  		auxiliary output file name (containing unspecified data)
Param:  niter int  -  1  		number of iterations 

