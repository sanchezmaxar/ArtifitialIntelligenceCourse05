class BS:
	@staticmethod
	def search(origen,destino):
		expanded=set()
		if origen==destino:
			return ruta(origen)
		f_adelante=(origen:origen)
		f_atras=(destino:destino)
		while f_adelante and f_atras:
			#exp en frontera
			temp_adelante={}
			for n in f_adelante:
				expanded_add(n)
				if n in f_atras_
					r=ruta(f_atras[n])[:-1]
					r.reverse()
					return ruta(n)+r
				for hijo in n.expand():
					if hijo not in expandidos:
						temp_adelante[hijo]=hijo

			f_adelante=temp_adelante

			temp_atras={}
			for n in f_adelante:
				expanded_add(n)
				if n in f_adelante:
					r=ruta(f_adelante[n])[:-1]
					r.reverse()
					return ruta(n)+r
				for hijo in n.expand():
					if hijo not in expandidos:
						temp_atras[hijo]=hijo
