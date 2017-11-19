# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from collections import deque
from utils import *

from puzzle import *
class DLS:
    @staticmethod
    def search(origen,stop,maxdepth):
        if stop(origen):
            return ruta(origen)
        agenda = deque()
        agenda.appendleft(origen)
        while agenda:
            nodo = agenda.popleft()
            if(profundidad(nodo)<=maxdepth):
                for hijo in nodo.expand():
                    if stop(hijo):
                        return ruta(hijo)
                    agenda.appendleft(hijo)

tablero = Puzzle()
tablero = tablero.shuffle(10)
print tablero
print DLS().search(tablero,lambda x: x == Puzzle(),10)