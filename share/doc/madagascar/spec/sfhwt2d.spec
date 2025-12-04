[sfhwt2d]
Cat:    RSF/system/seismic
Desc:   2-D Huygens wavefront tracing traveltimes
DocCmd: sfhwt2d | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fv data)
Port:   stdout rsf w req 	RSF standard output (containing Fw data)
Param:  dg float  -  1 		
Param:  dt float  -  0.001 		
Param:  ng int  -  360 		
Param:  nt int  -  100 		
Param:  og float  -  -180 		
Param:  ot float  -  0 		
Param:  rays enum-bool  -  n 		velocity file 
Param:  verb enum-bool  -  n 		
Param:  xsou float  -   -  		
LDesc:  (defaults to: sf_o(ax) + nx*sf_d(ax)/2)
Param:  zsou float  -   -  		
LDesc:  (defaults to: sf_o(az) + nz*sf_d(az)/2)

