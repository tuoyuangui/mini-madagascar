[sftransp]
Cat:    RSF/system/main
Desc:   Transpose two axes in a dataset
DocCmd: sftransp | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  memsize int  -   -  		Max amount of RAM (in Mb) to be used 
LDesc:  (defaults to: sf_memsize())
Param:  plane int  -   -  		Two-digit number with axes to transpose. The default is 12 

