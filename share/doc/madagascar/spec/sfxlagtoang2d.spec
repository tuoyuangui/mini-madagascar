[sfxlagtoang2d]
Cat:    RSF/system/seismic
Desc:   SS(x-lag) to angle transformation (PP or PS waves)
DocCmd: sfxlagtoang2d | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fstk data)
Port:   stdout rsf w req 	RSF standard output (containing Fang data)
Port:   dip rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   vpvs rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  da float  -   -  		
LDesc:  (defaults to: 1./(sf_n(axs)-1))
Param:  extend int  -  4 		tmp extension 
Param:  inv enum-bool  -  n 		inverse transformation flag 
Param:  na int  -   -  		
LDesc:  (defaults to: sf_n(axs))
Param:  oa float  -  0. 		
Param:  verb enum-bool  -  n 		verbosity flag 

