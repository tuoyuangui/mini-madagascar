[sfovczo]
Cat:    RSF/system/seismic
Desc:   Post-stack 2-D oriented velocity continuation
DocCmd: sfovczo | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  dv float  -   -  		velocity step size 
Param:  nv int  -   -  		velocity steps 
Param:  v0 float  -   -  		starting velocity 
Param:  verb enum-bool  -  y 		verbosity flag 

