[sfzomva]
Cat:    RSF/system/seismic
Desc:   3-D zero-offset WEMVA
DocCmd: sfzomva | cat
Port:   stdin  rsf r req 	RSF standard input (containing Pi data)
Port:   stdout rsf w req 	RSF standard output (containing Ps data)
Port:   slo rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   wfl rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  dtmax float  -  0.004 		time error 
Param:  eps float  -  0.01 		stability parameter 
Param:  inv enum-bool  -  n 		y=modeling; n=migration 
Param:  nrmax int  -  1 		maximum number of references 
Param:  pmx int  -  0 		padding on x 
Param:  pmy int  -  0 		padding on y
Param:  tmx int  -  0 		taper on x
Param:  tmy int  -  0 		taper on y 
Param:  twoway enum-bool  -  y 		two-way traveltime 
Param:  verb enum-bool  -  n 		verbosity flag 

