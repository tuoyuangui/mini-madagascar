[sfattr]
Cat:    RSF/system/main
Desc:   Display dataset attributes
DocCmd: sfattr | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Param:  lval int  -  2 		norm option, lval is a non-negative integer, computes the vector lval-norm 
Param:  want string  -   -  		'all'(default), 'rms', 'mean', 'norm', 'var', 
LDesc:         'std', 'max', 'min', 'nonzero', 'samples', 'short' 
LDesc:          want=   'rms' displays the root mean square
LDesc:          want=   'norm' displays the square norm, otherwise specified by lval.
LDesc:          want=   'var' displays the variance
LDesc:          want=   'std' displays the standard deviation
LDesc:          want=   'nonzero' displays number of nonzero samples
LDesc:          want=   'samples' displays total number of samples
LDesc:          want=   'short' displays a short one-line version
LDesc:       

