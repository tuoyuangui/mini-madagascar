[sfkirchnew]
Cat:    RSF/system/seismic
Desc:   Kirchhoff 2-D post-stack time migration and modeling with antialiasing
DocCmd: sfkirchnew | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  adj enum-bool  -  y 		yes: migration, no: modeling 
Param:  hd enum-bool  -  y 		if y, apply half-derivative filter 
Param:  sw int  -  0 		if > 0, select a branch of the antialiasing operation 
Param:  v0 float  -   -  		constant velocity (if no velocity=) 
Param:  velocity string  -   -  		velocity file (auxiliary input file name)

