[sfspray]
Cat:    RSF/system/main
Desc:   Extend a dataset by duplicating in the specified axis dimension
DocCmd: sfspray | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  axis int  -  2 		which axis to spray 
Param:  d float  -   -  		Sampling of the newly created dimension 
Param:  label string  -   -  		Label of the newly created dimension 
Param:  n int  -   -  		Size of the newly created dimension 
Param:  o float  -   -  		Origin of the newly created dimension 
Param:  unit string  -   -  		Units of the newly created dimension 

