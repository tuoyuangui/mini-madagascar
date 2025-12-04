[sfdiffraction]
Cat:    RSF/system/seismic
Desc:   Generate diffractions in zero-offset data
DocCmd: sfdiffraction | cat
Port:   stdin  rsf r req 	RSF standard input (containing w1 data)
Port:   stdout rsf w req 	RSF standard output (containing data data)
Port:   spikes rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   w12 rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   w2 rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  freq float  -   -  		peak frequency for Ricker wavelet 
LDesc:  (defaults to: 0.2/dt)

