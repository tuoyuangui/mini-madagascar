[sffkamo]
Cat:    RSF/system/seismic
Desc:   Computes Azimuth Move-Out (AMO) operator in the f-k log-stretch domain
DocCmd: sffkamo | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  f1 float  -   -  		input azimuth in degrees 
Param:  f2 float  -   -  		output azimuth in degrees 
Param:  h1 float  -   -  		input offset 
Param:  h2 float  -   -  		output offset 
Param:  maxe float  -  10. 		stability constraint 

