[sfricker2]
Cat:    RSF/system/seismic
Desc:   Nonstationary convolution with a Ricker wavelet. Phase and Frequency can be time-varying
DocCmd: sfricker2 | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   tfreq rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  esp float  -  0. 		if norm=y, stable parameter
Param:  freq float  -  0.2 		peak frequency for Ricker wavelet (as fraction of Nyquist) 
Param:  frequency float  -   -  		peak frequency for Ricker wavelet (in Hz) 
Param:  hiborder int  -  6 		Hilbert transformer order 
Param:  hibref float  -  1. 		
Param:  norm enum-bool  -  n 		
Param:  tphase string  -   -  		auxiliary input file name

