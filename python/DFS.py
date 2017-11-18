# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from collections import deque
from utils import ruta

from puzzle import *
class DFS:
    @staticmethod
    def search(origen,stop):
        if stop(origen):
            return ruta(origen)
        agenda = deque()
        expandidos = set()
        agenda.appendleft(origen)
        i=0
        while agenda and i<10000:
            nodo = agenda.popleft()
            expandidos.add(nodo)
            for hijo in nodo.expand():
                if stop(hijo):
                    return ruta(hijo)
                if hijo not in expandidos:
                    agenda.appendleft(hijo)
            i+=1
