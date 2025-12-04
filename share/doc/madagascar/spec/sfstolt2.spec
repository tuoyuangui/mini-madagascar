[sfstolt2]
Cat:    RSF/system/seismic
Desc:   Post-stack Stolt modeling/migration
DocCmd: sfstolt2 | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  nf int  -  2 		Interpolation accuracy 
Param:  pad int  -   -  		padding on the time axis 
LDesc:  (defaults to: nt)
Param:  vel float  -   -  		Constant velocity (use negative velocity for modeling) 

