[sfdisfil]
Cat:    RSF/system/main
Desc:   Print out data values
DocCmd: sfdisfil | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Param:  col int  -  0 		Number of columns.
LDesc:         The default depends on the data type:
LDesc:         10 for int and char,
LDesc:         5 for float,
LDesc:         3 for complex 
Param:  format string  -   -  		Format for numbers (printf-style).
LDesc:         The default depends on the data type:
LDesc:         '%4d ' for int and char,
LDesc:         '%13.4g' for float,
LDesc:         '%10.4g,%10.4gi' for complex 
Param:  header string  -   -  		Optional header string to output before data 
Param:  number enum-bool  -  y 		If number the elements 
Param:  trailer string  -   -  		Optional trailer string to output after data 

