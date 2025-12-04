[sfsegyheader]
Cat:    RSF/system/seismic
Desc:   Make a trace header file for segywrite
DocCmd: sfsegyheader | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  d1 float  -   -  		trace sampling 
Param:  n1 int  -   -  		number of samples in a trace 
Param:  o1 float  -  0 		trace origin 
Param:  tfile string  -   -  		auxiliary input file name

