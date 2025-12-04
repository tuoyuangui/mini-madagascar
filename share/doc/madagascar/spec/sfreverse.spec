[sfreverse]
Cat:    RSF/system/main
Desc:   Reverse one or more axes in the data hypercube
DocCmd: sfreverse | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  memsize int  -   -  		Max amount of RAM (in Mb) to be used 
LDesc:  (defaults to: sf_memsize())
Param:  opt string  -   -  		If y, change o and d parameters on the reversed axis;
LDesc:         if i, don't change o and d 
Param:  verb enum-bool  -  n 		Verbosity flag 
Param:  which int  -  -1 		Which axis to reverse.
LDesc:         To reverse a given axis, start with 0,
LDesc:         add 1 to number to reverse n1 dimension,
LDesc:         add 2 to number to reverse n2 dimension,
LDesc:         add 4 to number to reverse n3 dimension, etc.
LDesc:         Thus, which=7 would reverse the first three dimensions,
LDesc:         which=5 just n1 and n3, etc.
LDesc:         which=0 will just pass the input on through unchanged. 

