[sfimpl2]
Cat:    RSF/system/generic
Desc:   2-D anisotropic diffusion
DocCmd: sfimpl2 | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  adj enum-bool  -  n 		adjoint flag 
Param:  dist string  -   -  		inverse distance file (input) 
Param:  lin enum-bool  -  n 		if linear operator 
Param:  nsnap int  -  1 		number of snapshots 
Param:  pclip float  -  50. 		percentage clip for the gradient 
Param:  rect1 float  -   -  		vertical smoothing 
Param:  rect2 float  -   -  		horizontal smoothing 
Param:  snap string  -   -  		snapshot file (output) 
Param:  tau float  -  0.1 		smoothing time 
Param:  up enum-bool  -  n 		smoothing style 
Param:  verb enum-bool  -  n 		verbosity flag 

