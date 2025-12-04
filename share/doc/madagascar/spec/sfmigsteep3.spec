[sfmigsteep3]
Cat:    RSF/system/seismic
Desc:   3-D Kirchhoff time migration for antialiased steep dips
DocCmd: sfmigsteep3 | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (containing mig data)
Port:   hdr rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  d2 float  -   -  		
Param:  d3 float  -   -  		
Param:  n1 int  -   -  		
Param:  n2 int  -   -  		
Param:  n3 int  -   -  		
Param:  o2 float  -   -  		
Param:  o3 float  -   -  		
Param:  vel float  -   -  		migration velocity 

