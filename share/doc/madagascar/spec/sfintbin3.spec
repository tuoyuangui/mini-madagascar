[sfintbin3]
Cat:    RSF/system/seismic
Desc:   4-D data binning
DocCmd: sfintbin3 | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  head string  -   -  		header file 
Param:  mask string  -   -  		output mask file 
Param:  xk string  -   -  		x key name 
Param:  xkey int  -   -  		x key number (if no xk), default is fldr 
Param:  xmax int  -   -  		x maximum 
Param:  xmin int  -   -  		x minimum 
Param:  yk string  -   -  		y key name 
Param:  ykey int  -   -  		y key number (if no yk), default is iline 
Param:  ymax int  -   -  		y maximum 
Param:  ymin int  -   -  		y minimum 
Param:  zk string  -   -  		z key name 
Param:  zkey int  -   -  		z key number (if no zk), default is xline 
Param:  zmax int  -   -  		z maximum 
Param:  zmin int  -   -  		z minimum 

