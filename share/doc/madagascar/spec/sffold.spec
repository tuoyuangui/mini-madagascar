[sffold]
Cat:    RSF/system/seismic
Desc:   Make a seismic foldplot/stacking chart
DocCmd: sffold | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  d1 float  -   -  		Delta label1 - usually delta offset  
Param:  d2 float  -   -  		Delta label2 - usually delta xline  
Param:  d3 float  -   -  		Delta label3 - usually delta iline  
Param:  label1 string  -   -  		header for axis1 - usually offset 
Param:  label2 string  -   -  		header for axis2 - usually xline or cdp  
Param:  label3 string  -   -  		header for axis3 - usually iline  
Param:  n1 int  -   -  		Number label1 - usually number offset 
Param:  n2 int  -   -  		Number label2 - usually number xline 
Param:  n3 int  -   -  		Number label3 - usually number iline 
Param:  o1 float  -   -  		Minimum label1 - usually min offset 
Param:  o2 float  -   -  		Minimum label2 - usually min xline  
Param:  o3 float  -   -  		Minimum label3 - usually min iline 
Param:  verbose int  -  1 		0 terse, 1 informative, 2 chatty, 3 debug 

