[sfzoeppritz]
Cat:    RSF/system/seismic
Desc:   Testing Zoeppritz equation
DocCmd: sfzoeppritz | cat
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  a0 float  -  0. 		first angle 
Param:  da float  -   -  		angle increment 
LDesc:  (defaults to: 90./na)
Param:  icoef int  -  4 		particle displacement, displacement potential, energy, real part 
Param:  incp enum-bool  -  y 		incident P (or S) 
Param:  na int  -  90 		number of angles 
Param:  outp enum-bool  -  y 		rellected/transmitted P (or S) 
Param:  refl enum-bool  -  y 		reflection or transmission 
Param:  rho1 float  -  1. 		
Param:  rho2 float  -  1. 		
Param:  vp1 float  -   -  		
Param:  vp2 float  -   -  		
Param:  vs1 float  -   -  		
Param:  vs2 float  -   -  		

