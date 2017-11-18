# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from collections import deque
from utils import ruta

from puzzle import *
class BFS:
    @staticmethod
    def search(origen,stop):
        if stop(origen):
            return ruta(origen)
        agenda = deque()
        expandidos = set()
        agenda.append(origen)
        while agenda:
            nodo = agenda.popleft()
            expandidos.add(nodo)
            for hijo in nodo.expand():
                if stop(hijo):
                    return ruta(hijo)
                if hijo not in expandidos:
                    agenda.append(hijo)
tablero = Puzzle()
print BFS().search(tablero.shuffle(10),lambda x: x == Puzzle())