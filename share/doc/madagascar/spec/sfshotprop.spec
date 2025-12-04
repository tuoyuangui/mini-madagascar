[sfshotprop]
Cat:    RSF/system/seismic
Desc:   Shot propagation
DocCmd: sfshotprop | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  ds float  -   -  		shot sampling 
Param:  eps float  -  0.1 		regularization parameter 
Param:  ns int  -   -  		number of shots 
Param:  positive enum-bool  -  y 		initial offset orientation 

