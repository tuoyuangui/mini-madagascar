[sfstripes]
Cat:    RSF/system/seismic
Desc:   Model the positions and dips of the constant offset, source, midpoint, and receiver strikes in a source vs. offset space
DocCmd: sfstripes | cat
Port:   stdin  rsf r req 	RSF standard input (containing inp data)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  mo int  -   -  		offset parameter, a constant offset line will appear in the output every o offset 
Param:  mr int  -   -  		receiver parameter, a constant receiver line will appear in the output every r receiver 
Param:  ms int  -   -  		source parameter, a constant source line will appear in the output every s source 
Param:  my int  -   -  		midpoint parameter, a constant midpoint line will appear in the output every y midpoint 

