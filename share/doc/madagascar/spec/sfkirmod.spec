[sfkirmod]
Cat:    RSF/system/seismic
Desc:   Kirchhoff 2-D/2.5-D modeling with analytical Green's functions
DocCmd: sfkirmod | cat
Port:   stdin  rsf r req 	RSF standard input (containing modl data)
Port:   stdout rsf w req 	RSF standard output (containing data data)
Port:   curv rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  absoff enum-bool  -  n 		y - h0 is not in shot coordinate system 
Param:  adj enum-bool  -  n 		adjoint flag 
Param:  cmp enum-bool  -  n 		compute CMP instead of shot gathers 
Param:  dh float  -   -  		offset increment 
LDesc:  (defaults to: dx)
Param:  dip string  -   -  		reflector dip file 
Param:  ds float  -   -  		shot/midpoint increment 
LDesc:  (defaults to: dx)
Param:  dt float  -  0.004 		time sampling 
Param:  eta float  -   -  		parameter for VTI anisotropy 
Param:  freq float  -   -  		peak frequency for Ricker wavelet 
LDesc:  (defaults to: 0.2/dt)
Param:  gradx float  -   -  		horizontal velocity gradient 
Param:  gradx2 float  -   -  		converted velocity, horizontal gradient 
Param:  gradz float  -   -  		vertical velocity gradient 
Param:  gradz2 float  -   -  		converted velocity, vertical gradient 
Param:  h0 float  -  0. 		first offset 
Param:  lin enum-bool  -  n 		if linear operator 
Param:  nh int  -   -  		number of offsets 
LDesc:  (defaults to: nx)
Param:  ns int  -   -  		number of shots (midpoints if cmp=y) 
LDesc:  (defaults to: nx)
Param:  nt int  -   -  		time samples 
Param:  picks string  -   -  		auxiliary output file name
Param:  r0 float  -  1. 		normal reflectivity (if constant) 
Param:  refl string  -   -  		auxiliary input file name
Param:  refx float  -   -  		reference x-coordinate for velocity 
Param:  refz float  -   -  		reference z-coordinate for velocity 
Param:  rgrad string  -   -  		AVO gradient file (B/A) 
Param:  s0 float  -   -  		first shot (midpoint if cmp=y) 
LDesc:  (defaults to: x0)
Param:  slopes string  -   -  		auxiliary output file name
Param:  t0 float  -  0. 		time origin 
Param:  twod enum-bool  -  n 		2-D or 2.5-D 
Param:  type string  -   -  		type of velocity, 'c': constant, 's': linear sloth, 'v': linear velocity, 'a': VTI anisotropy 
Param:  type2 string  -   -  		type of velocity for the converted (receiver side) branch 
Param:  vel float  -   -  		velocity 
Param:  vel2 float  -   -  		converted velocity 
Param:  velz float  -   -  		vertical velocity for VTI anisotropy 
Param:  verb enum-bool  -  n 		verbosity flag 

