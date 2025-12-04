[sfshotholes]
Cat:    RSF/system/seismic
Desc:   Remove random shot gathers from a 2-D dataset
DocCmd: sfshotholes | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (containing mask data)
Param:  perc float  -  0.75 		how many shots to remove 

