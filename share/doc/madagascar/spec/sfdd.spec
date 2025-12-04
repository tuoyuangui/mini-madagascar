[sfdd]
Cat:    RSF/system/main
Desc:   Convert between different formats
DocCmd: sfdd | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  form string  -   -  		ascii, native, xdr 
Param:  format string  -   -  		Element format (for conversion to ASCII) 
Param:  ibm enum-bool  -  n 		Special case - assume integers actually represent IBM floats 
Param:  line int  -  8 		Number of numbers per line (for conversion to ASCII) 
Param:  strip int  -  0 		If strip characters from format at the end of the line 
Param:  trunc enum-bool  -  n 		Truncate or round to nearest when converting from float to int/short 
Param:  type string  -   -  		int, float, complex, short, long 

