import heapq
from utils import ruta

class GBFS:
	def search(origen,stop,heuristica):
		agenda=[]
		expandidos=set()
		if (stop()):
			return ruta(origen)
		heapq.heappush(agenda,(0,origen))
		while agenda:
			nodo=heapq.heappop(agenda)[1]
			if stop(nodo):
				return ruta(nodo)
			for hijo in nodo.expand():
				if hijo  not in explored:
					heapq.heappush(agenda,heuristica(hijo),hijo)