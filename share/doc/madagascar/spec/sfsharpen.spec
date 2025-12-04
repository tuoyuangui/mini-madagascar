[sfsharpen]
Cat:    RSF/system/generic
Desc:   Sharpening operator
DocCmd: sfsharpen | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  fact float  -  0.5 		factor for sharpening 
Param:  other string  -   -  		auxiliary input file name
Param:  perc float  -  50.0 		percentage for sharpening 

