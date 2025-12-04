[sfomp]
Cat:    RSF/system/main
Desc:   OpenMP wrapper for embarassingly parallel jobs
DocCmd: sfomp | cat
Port:   stdin  rsf r req 	RSF standard input (containing inp data)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  join int  -   -  		axis to join (0 means add) 
LDesc:  (defaults to: axis)
Param:  split int  -   -  		axis to split 
LDesc:  (defaults to: ndim)

