[sfcascade]
Cat:    RSF/system/seismic
Desc:   Velocity partitioning for cascaded migrations
DocCmd: sfcascade | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  ncut int  -  1 		number of cuts 
Param:  ntcut int-list  -   -  		 [ncut]
Param:  tcut float-list  -   -  		time cuts  [ncut]

