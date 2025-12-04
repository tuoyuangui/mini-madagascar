[sfsegyread]
Cat:    RSF/system/seismic
Desc:   Convert a SEG-Y or SU dataset to RSF
DocCmd: sfsegyread | cat
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  bfile string  -   -  		output binary data header file 
Param:  endian enum-bool  -  y 		Whether to automatically estimate endianness or not 
Param:  format int  -   -  		Data format. 
LDesc:             The default is taken from binary header for segy input.
LDesc:  	   Default is 5 for su input.
LDesc:  	   1 is IBM floating point
LDesc:  	   2 is 4-byte integer
LDesc:  	   3 is 2-byte integer
LDesc:  	   5 is IEEE floating point
LDesc:         6 is native_float (same as RSF binary default)
LDesc:  	   7 is 1-byte integer
LDesc:  	
Param:  hfile string  -   -  		output text data header file 
Param:  mask string  -   -  		optional header mask for reading only selected traces (auxiliary input file name)
Param:  n2 int  -  0 		number of traces to read (if 0, read all traces) 
Param:  ns int  -  0 		Number of samples. The default is taken from binary header 
Param:  nsbyte int  -  0 		byte number for ns in binary header 
Param:  read string  -   -  		what to read: h - header, d - data, b - both (default) 
Param:  su enum-bool  -   -  		y if input is SU, n if input is SEGY 
Param:  suxdr enum-bool  -  n 		y, SU has XDR support.  
LDesc:             SU with xdr on (as downloaded), use endian=y suxdr=y
LDesc:             SU with xdr off in the makefiles, use endian=n suxdr=n   
LDesc:          
Param:  tape string  -   -  		input data 
Param:  tfile string  -   -  		output trace header file (auxiliary output file name)
Param:  verb enum-bool  -  n 		Verbosity flag 

