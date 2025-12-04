[sfintbin]
Cat:    RSF/system/seismic
Desc:   Data binning by trace sorting
DocCmd: sfintbin | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  head string  -   -  		header file 
Param:  inv enum-bool  -  n 		inversion flag 
Param:  map string  -   -  		output map file 
Param:  mask string  -   -  		output mask file 
Param:  xk string  -   -  		x key name 
Param:  xkey int  -   -  		x key number (if no xk), default is fldr 
Param:  xmax int  -   -  		x maximum 
Param:  xmin int  -   -  		x minimum 
Param:  yk string  -   -  		y key name 
Param:  ykey int  -   -  		y key number (if no yk), default is tracf 
Param:  ymax int  -   -  		y maximum 
Param:  ymin int  -   -  		y minimum 

