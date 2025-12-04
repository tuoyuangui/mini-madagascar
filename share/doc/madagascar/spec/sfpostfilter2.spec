[sfpostfilter2]
Cat:    RSF/system/generic
Desc:   Convert B-spline coefficients to data in 2-D
DocCmd: sfpostfilter2 | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  horz enum-bool  -  y 		include filter on the second axis 
Param:  nw int  -   -  		filter size 
Param:  vert enum-bool  -  y 		include filter on the first axis 

