[sfbandpass]
Cat:    RSF/system/generic
Desc:   Bandpass filtering
DocCmd: sfbandpass | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  fhi float  -   -  		High frequency in band, default is Nyquist 
Param:  flo float  -   -  		Low frequency in band, default is 0 
Param:  nphi int  -  6 		number of poles for high cutoff 
Param:  nplo int  -  6 		number of poles for low cutoff 
Param:  phase enum-bool  -  n 		y: minimum phase, n: zero phase 
Param:  verb enum-bool  -  n 		verbosity flag 

