[sfitaupmo]
Cat:    RSF/system/seismic
Desc:   Inverse normal moveout in tau-p domain
DocCmd: sfitaupmo | cat
Port:   stdin  rsf r req 	RSF standard input (containing cmp data)
Port:   stdout rsf w req 	RSF standard output (containing nmod data)
Port:   velocity rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  eps float  -  0.01 		stretch regularization 
Param:  eta string  -   -  		auxiliary input file name
Param:  interval enum-bool  -  y 		use interval velocity 

