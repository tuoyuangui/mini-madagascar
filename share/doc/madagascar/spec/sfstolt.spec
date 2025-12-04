[sfstolt]
Cat:    RSF/system/seismic
Desc:   Post-stack Stolt modeling/migration
DocCmd: sfstolt | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  extend int  -  4 		trace extension 
Param:  minstr float  -  0.0 		minimum stretch allowed 
Param:  mute int  -  12 		mute zone 
Param:  pad int  -   -  		padding on the time axis 
LDesc:  (defaults to: nt)
Param:  stretch float  -  1 		Stolt stretch parameter 
Param:  vel float  -   -  		Constant velocity (use negative velocity for modeling) 

