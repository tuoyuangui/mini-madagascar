[sffourvc2]
Cat:    RSF/system/seismic
Desc:   Velocity continuation with semblance computation
DocCmd: sffourvc2 | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  dv float  -   -  		
Param:  eps float  -  0.01 		
Param:  extend int  -  4 		trace extension 
Param:  nb int  -  2 		
Param:  nv int  -   -  		
Param:  pad int  -   -  		
LDesc:  (defaults to: n1)
Param:  pad2 int  -   -  		
LDesc:  (defaults to: 2*kiss_fft_next_fast_size((n2+1)/2))
Param:  semblance enum-bool  -  y 		if y, compute semblance; if n, stack 

