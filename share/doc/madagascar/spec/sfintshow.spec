[sfintshow]
Cat:    RSF/system/generic
Desc:   Output interpolation filter
DocCmd: sfintshow | cat
Port:   stdout rsf w req 	RSF standard output (containing filt data)
Param:  interp string  -   -  		interpolation (lagrange,cubic,kaiser,lanczos,cosine,welch,spline,mom) 
Param:  kai float  -  4.0 		Kaiser window parameter 
Param:  nw int  -   -  		interpolator size 
Param:  x float  -   -  		interpolation shift 

