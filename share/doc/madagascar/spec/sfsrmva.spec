[sfsrmva]
Cat:    RSF/system/seismic
Desc:   3-D S/R WEMVA with extended split-step
DocCmd: sfsrmva | cat
Port:   stdin  rsf r req 	RSF standard input (containing Pi data)
Port:   stdout rsf w req 	RSF standard output (containing Ps data)
Port:   rwf rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   slo rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   swf rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  adj enum-bool  -  n 		y=ADJ scat; n=FWD scat 
Param:  dtmax float  -  0.004 		max time error 
Param:  eps float  -  0.01 		stability parameter 
Param:  nrmax int  -  1 		max number of refs 
Param:  pmx int  -  0 		padding on x 
Param:  pmy int  -  0 		padding on y 
Param:  tmx int  -  0 		taper on x   
Param:  tmy int  -  0 		taper on y   
Param:  twoway enum-bool  -  y 		two-way traveltime 
Param:  verb enum-bool  -  y 		verbosity flag 

