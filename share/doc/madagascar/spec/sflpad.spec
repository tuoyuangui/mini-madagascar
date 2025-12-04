[sflpad]
Cat:    RSF/system/generic
Desc:   Pad and interleave traces
DocCmd: sflpad | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   mask rsf w  -  		auxiliary output file name (containing unspecified data)
Param:  jump int  -  2 		aliasing 

