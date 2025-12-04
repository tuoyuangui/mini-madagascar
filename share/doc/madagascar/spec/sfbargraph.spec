[sfbargraph]
Cat:    RSF/plot/main
Desc:   Bar plot
DocCmd: sfbargraph | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Param:  pclip float  -  100. 		clip percentile 
Param:  stack enum-bool  -  y 		if stack bars on top 
Param:  transp enum-bool  -  n 		if y, transpose the axes 
Param:  wantframenum enum-bool  -   -  		if y, display third axis position in the corner 
LDesc:  (defaults to: (bool) (n3 > 1))
Param:  width float  -  0.8 		bar width 

