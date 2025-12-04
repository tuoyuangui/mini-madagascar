[sfshot2cmp]
Cat:    RSF/system/seismic
Desc:   Convert shots to CMPs for regular 2-D geometry
DocCmd: sfshot2cmp | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  half enum-bool  -  y 		if y, the second axis is half-offset instead of full offset
Param:  mask string  -   -  		auxiliary output file name
Param:  positive enum-bool  -  y 		initial offset orientation 

