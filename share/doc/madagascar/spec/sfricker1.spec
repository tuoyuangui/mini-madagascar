[sfricker1]
Cat:    RSF/system/seismic
Desc:   Convolution with a Ricker wavelet
DocCmd: sfricker1 | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  deriv enum-bool  -  n 		apply a half-order derivative filter 
Param:  freq float  -  0.2 		peak frequency for Ricker wavelet (as fraction of Nyquist) 
Param:  frequency float  -   -  		peak frequency for Ricker wavelet (in Hz) 

