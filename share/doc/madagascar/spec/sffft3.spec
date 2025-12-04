[sffft3]
Cat:    RSF/system/generic
Desc:   FFT transform on extra axis
DocCmd: sffft3 | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  axis int  -  2 		Axis to transform 
Param:  inv enum-bool  -  n 		if y, perform inverse transform 
Param:  opt enum-bool  -  y 		if y, determine optimal size for efficiency 
Param:  pad int  -  2 		padding factor 
Param:  sign int  -   -  		transform sign (0 or 1) 
LDesc:  (defaults to: inv? 1: 0)
Param:  sym enum-bool  -  n 		if y, apply symmetric scaling to make the FFT operator Hermitian 

