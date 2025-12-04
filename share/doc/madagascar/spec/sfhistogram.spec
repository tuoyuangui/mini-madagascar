[sfhistogram]
Cat:    RSF/system/generic
Desc:   Compute a histogram of integer- or float-valued input data
DocCmd: sfhistogram | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  d1 float  -   -  		histogram sampling 
Param:  n1 int  -   -  		number of histogram samples 
Param:  o1 float  -   -  		histogram origin 

