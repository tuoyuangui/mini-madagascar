[sfscale]
Cat:    RSF/system/main
Desc:   Scale data
DocCmd: sfscale | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  axis int  -  0 		Scale by maximum in the dimensions up to this axis. 
Param:  dscale float  -  1. 		Scale by this factor (works if rscale=0) 
Param:  pclip float  -  100. 		data clip percentile 
Param:  rscale float  -  0. 		Scale by this factor. 

