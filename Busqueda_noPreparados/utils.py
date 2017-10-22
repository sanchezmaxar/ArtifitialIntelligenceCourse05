def ruta (end):
	secuencia=[]
	secuencia.append(end)
	while end.parent:
		end=end.parent
		secuencia.append(end)
	secuencia.reverse()
	return secuencia[::-1]
