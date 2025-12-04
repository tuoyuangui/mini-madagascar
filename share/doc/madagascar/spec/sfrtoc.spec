[sfrtoc]
Cat:    RSF/system/main
Desc:   Convert real data to complex (by adding zero imaginary part)
DocCmd: sfrtoc | cat
Port:   stdin  rsf r req 	RSF standard input (containing real data)
Port:   stdout rsf w req 	RSF standard output (containing cmplx data)
Param:  pair enum-bool  -  n 		y - use odd elements for real part and even ones for imaginary part 

