[sftrapez]
Cat:    RSF/system/generic
Desc:   Convolution with a trapezoidal filter
DocCmd: sftrapez | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  frequency float-list  -   -  		frequencies (in Hz), default: (0.1,0.15,0.45,0.5)*Nyquist  [4]

