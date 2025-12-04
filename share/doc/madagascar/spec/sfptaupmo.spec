[sfptaupmo]
Cat:    RSF/system/seismic
Desc:   Slope-based tau-p moveout
DocCmd: sfptaupmo | cat
Port:   stdin  rsf r req 	RSF standard input (containing inp data)
Port:   stdout rsf w req 	RSF standard output (containing nmod data)
Port:   dip rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   dipt rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   vel2 rsf w  -  		auxiliary output file name (containing unspecified data)
Param:  eps float  -  0.01 		stretch regularization 
Param:  type string  -   -  		transform type 
Param:  v0 float  -  0. 		initial velocity 

