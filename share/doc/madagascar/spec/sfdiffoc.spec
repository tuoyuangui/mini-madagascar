[sfdiffoc]
Cat:    RSF/system/seismic
Desc:   Diffraction focusing test
DocCmd: sfdiffoc | cat
Port:   stdin  rsf r req 	RSF standard input (containing inp data)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  extend int  -  4 		trace extension 
Param:  pad int  -   -  		padding for stretch 
LDesc:  (defaults to: nt)
Param:  pad2 int  -   -  		padding for FFT 
LDesc:  (defaults to: 2*kiss_fft_next_fast_size((n2+1)/2))
Param:  v float  -   -  		final velocity 
Param:  v0 float  -   -  		initial velocity 
LDesc:  (defaults to: SF_EPS)

