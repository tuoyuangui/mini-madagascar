[sfclip2]
Cat:    RSF/system/generic
Desc:   One- or two-sided data clipping
DocCmd: sfclip2 | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  lower float  -   -  		lower clip value 
LDesc:  (defaults to: -FLT_MAX)
Param:  upper float  -   -  		upper clip value 
LDesc:  (defaults to: +FLT_MAX)

