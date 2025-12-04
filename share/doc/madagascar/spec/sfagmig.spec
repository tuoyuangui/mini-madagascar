[sfagmig]
Cat:    RSF/system/seismic
Desc:   Angle-gather constant-velocity time migration
DocCmd: sfagmig | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  a float  -  80. 		maximum dip angle 
Param:  dg float  -   -  		reflection angle sampling 
Param:  g0 float  -   -  		reflection angle origin 
Param:  na int  -   -  		number of dip angles 
LDesc:  (defaults to: nx)
Param:  ng int  -   -  		number of reflection angles 
Param:  vel float  -   -  		velocity 

