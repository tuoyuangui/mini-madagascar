[sfpad]
Cat:    RSF/system/main
Desc:   Pad a dataset with zeros
DocCmd: sfpad | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  beg# int  -  0 		the number of zeros to add before the beginning of #-th axis 
Param:  end# int  -  0 		the number of zeros to add after the end of #-th axis 
Param:  n# int  -   -  		the output length of #-th axis - padding at the end 

