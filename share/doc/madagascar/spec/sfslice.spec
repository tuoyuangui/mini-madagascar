[sfslice]
Cat:    RSF/system/generic
Desc:   Extract a slice using picked surface (usually from a stack or a semblance)
DocCmd: sfslice | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   pick rsf r  -  		auxiliary input file name (containing unspecified data)

