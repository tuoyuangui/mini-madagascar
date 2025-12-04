[sfmakevel]
Cat:    RSF/su/main
Desc:   Make a velocity function v(x,y,z)
DocCmd: sfmakevel | cat
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  d1 float  -  1.0 		1st dimension sampling interval
Param:  d2 float  -  1.0 		2nd dimension sampling interval
Param:  d3 float  -  1.0 		3rd dimension sampling interval
Param:  dlens float  -  1.0 		diameter of parabolic lens
Param:  dvdx1 float  -  0.0 		velocity gradient with respect to 1st dimension
Param:  dvdx2 float  -  0.0 		velocity gradient with respect to 2nd dimension
Param:  dvdx3 float  -  0.0 		velocity gradient with respect to 3rd dimension
Param:  exc float  -  1.0 		exponent of chirp
Param:  l1c float  -   -  		wavelength at beginning of chirp
LDesc:  (defaults to: dz)
Param:  l2c float  -   -  		wavelength at end of chirp
LDesc:  (defaults to: dz)
Param:  n1 int  -   -  		number of z samples (1st dimension)), must be provided!
Param:  n2 int  -   -  		number of x samples (2nd dimension), must be provided!
Param:  n3 int  -  1 		number of y samples (3rd dimension)
Param:  o1 float  -  0.0 		Origin 1st dimension
Param:  o2 float  -  0.0 		Origin 2nd dimension
Param:  o3 float  -  0.0 		Origin 3rd dimension
Param:  tlens float  -  1.0 		thickness of parabolic lens
Param:  v000 float  -  2.0 		velocity at (x=0,y=0,z=0)
Param:  vlens float  -  0.0 		velocity perturbation in parabolic lens
Param:  vran float  -  0.0 		standard deviation of random perturbation
Param:  vx1c float  -  0.0 		1st dimension v(z) chirp amplitude
Param:  vx1file string  -   -  		file containing v(z) 1st dimension profile
Param:  vx1ran float  -  0.0 		standard deviation of random perturbation to 1st dimension
Param:  vzfile string  -   -  		
Param:  x11c float  -   -  		1st dimension at which to begin chirp
LDesc:  (defaults to: fz)
Param:  x12c float  -   -  		1st dimension at which to end chirp
LDesc:  (defaults to: fz+(nz-1)*dz)
Param:  x1lens float  -   -  		1st dimension coordinate of center of parabolic lens
LDesc:  (defaults to: fz)
Param:  x2lens float  -   -  		2nd dimension coordinate of center of parabolic lens
LDesc:  (defaults to: fx)
Param:  x3lens float  -   -  		3rd dimension coordinate of center of parabolic lens
LDesc:  (defaults to: fy)

