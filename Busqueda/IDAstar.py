# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from collections import deque
from utils import *
from puzzle import *
from manhattan import *

class IDAstar:
    @staticmethod
    def search(origen,stop,maxdepth,heuristica):
        if stop(origen):
            return ruta(origen)
        frontera=1+heuristica(origen)
        while frontera<=maxdepth:
            ac=0
            aux=0
            agenda = deque()
            agenda.appendleft(origen)
            while agenda:
                nodo = agenda.popleft()
                if(profundidad(nodo)<=frontera):
                    for hijo in nodo.expand():
                        if stop(hijo):
                            return ruta(hijo)
                        agenda.appendleft(hijo)
                x = profundidad(nodo)+heuristica(nodo)
                if ac==0:
                    aux=x
                    ac=1
                elif aux>x and x>frontera:
                    aux=x
            if aux <= frontera:
                frontera+=1
            else:
                frontera=aux
            print frontera
tablero = Puzzle()
print IDAstar().search(tablero.shuffle(20),lambda x: x == Puzzle(),20,ManhattanDistance().distance_to_target)