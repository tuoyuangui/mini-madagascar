[sfkdmig2d]
Cat:    RSF/su/main
Desc:   2-D Prestack Kirchhoff depth migration (SU version)
DocCmd: sfkdmig2d | cat
Port:   stdin  rsf r req 	RSF standard input (containing infp data)
Port:   stdout rsf w req 	RSF standard output (containing outfp data)
Param:  absoff int  -  0 		1 - use absolute value of offset, 0 - use offset =gx-sx 
Param:  angmax float  -  60. 		migration angle aperature from vertical 
Param:  aperx float  -   -  		migration lateral aperature 
LDesc:  (defaults to: 0.5*nxt*dxt)
Param:  csfile string  -   -  		input file of cosine tables 
Param:  doff float  -  0.1 		offset increment in output 
Param:  dvz float  -  0 		reference velocity vertical gradient 
Param:  dxm float  -   -  		sampling interval of midpoints 
LDesc:  (defaults to: 0.5*ds)
Param:  dxo float  -   -  		horizontal spacing of output trace 
LDesc:  (defaults to: dxt*0.5)
Param:  dzo float  -   -  		vertical spacing of output trace 
LDesc:  (defaults to: dzt*0.2)
Param:  fmax float  -   -  		frequency-highcut for input traces 
LDesc:  (defaults to: 0.25/dt)
Param:  fxo float  -   -  		x-coordinate of first output trace 
LDesc:  (defaults to: fxt)
Param:  fzo float  -   -  		z-coordinate of first point in output trace 
LDesc:  (defaults to: fzt)
Param:  limoff int  -  0 		1 - limit traces used by offset, 0 - use all traces 
Param:  ls int  -  1 		flag for line source 
Param:  mtr int  -  100 		print verbal information at every mtr traces 
Param:  noff int  -  1 		number of offsets in output 
Param:  npv int  -  0 		1 - compute quantities for velocity analysis 
Param:  ntr int  -   -  		maximum number of input traces to be migrated 
LDesc:  (defaults to: sf_leftsize (infp, 1))
Param:  nxo int  -   -  		number of output traces 
LDesc:  (defaults to: (nxt-1)*2+1)
Param:  nzo int  -   -  		number of points in output trace 
LDesc:  (defaults to: (nzt-1)*5+1)
Param:  off0 float  -  0. 		first offest in output 
Param:  offmax float  -  3.0 		maximum absolute offset allowed in migration 
Param:  outfile1 string  -   -  		file containning additional migration output 
Param:  rscale float  -   -  		scaling for roundoff error suppression 
LDesc:  (defaults to: RSCALE_KDMIG)
Param:  ttfile string  -   -  		input traveltime tables 
Param:  tvfile string  -   -  		input file of traveltime variation tables 
Param:  v0 float  -  1.5 		reference velocity value at surface 
Param:  verb enum-bool  -  n 		verbosity flag 

