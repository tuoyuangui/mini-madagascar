[sfkirmod3]
Cat:    RSF/system/seismic
Desc:   Kirchhoff 3-D modeling with analytical Green's functions
DocCmd: sfkirmod3 | cat
Port:   stdin  rsf r req 	RSF standard input (containing curv data)
Port:   stdout rsf w req 	RSF standard output (containing modl data)
Param:  absoff enum-bool  -  n 		y - h0x, h0y - are not in shot coordinate system 
Param:  aper float  -   -  		aperture 
LDesc:  (defaults to: hypotf(nx*dx,ny*dy))
Param:  dhx float  -   -  		inline offset increment 
LDesc:  (defaults to: dx)
Param:  dhy float  -   -  		crossline offset increment 
LDesc:  (defaults to: dy)
Param:  dipx string  -   -  		
Param:  dipy string  -   -  		
Param:  dsx float  -   -  		inline shot increment 
LDesc:  (defaults to: dx)
Param:  dsy float  -   -  		crossline shot increment 
LDesc:  (defaults to: dy)
Param:  dt float  -  0.004 		time sampling 
Param:  freq float  -   -  		peak frequency for Ricker wavelet 
LDesc:  (defaults to: 0.2/dt)
Param:  h0x float  -  0. 		first inline offset 
Param:  h0y float  -  0. 		first crossline offset 
Param:  head string  -   -  		source-receiver geometry (optional) (auxiliary input file name)
Param:  nhx int  -   -  		number of inline offsets 
LDesc:  (defaults to: nx)
Param:  nhy int  -   -  		number of crossline offsets 
LDesc:  (defaults to: ny)
Param:  nsx int  -   -  		number of inline shots 
LDesc:  (defaults to: nx)
Param:  nsy int  -   -  		number of crossline shots 
LDesc:  (defaults to: ny)
Param:  nt int  -   -  		time samples 
Param:  r0 float  -  1. 		constant reflectivity 
Param:  refl string  -   -  		auxiliary input file name
Param:  rgrad string  -   -  		
Param:  s0x float  -   -  		first inline shot 
LDesc:  (defaults to: x0)
Param:  s0y float  -   -  		first crossline shot 
LDesc:  (defaults to: y0)
Param:  t0 float  -  0. 		time origin 
Param:  type string  -   -  		type of velocity ('c': constant, 's': linear sloth, 'v': linear velocity) 
Param:  verb enum-bool  -  y 		verbosity 

