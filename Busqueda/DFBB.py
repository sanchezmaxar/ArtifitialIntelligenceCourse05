# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from collections import deque
from utils import *

from puzzle import *
class DFBB:
    @staticmethod
    def search(origen,stop,maxdepth):
        if stop(origen):
            return ruta(origen)
        agenda = deque()
        agenda.appendleft(origen)
        route = []
        while agenda:
            nodo = agenda.popleft()
            if(profundidad(nodo)<=maxdepth-1):
                for hijo in nodo.expand():
                    if stop(hijo):
                        route = ruta(hijo)
                        maxdepth = profundidad(hijo)-1
                    agenda.appendleft(hijo)
        return route
tablero = Puzzle()
print DFBB().search(tablero.shuffle(10),lambda x: x == Puzzle(),10)