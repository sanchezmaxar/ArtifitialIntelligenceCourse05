# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from collections import deque
from utils import *

from puzzle import *
class ID:
    @staticmethod
    def search(origen,stop,maxdepth):
        for i in range(maxdepth+1):
            if stop(origen):
                return ruta(origen)
            agenda = deque()
            expandidos = set()
            agenda.appendleft(origen)
            while agenda:
                nodo = agenda.popleft()
                expandidos.add(nodo)
                if(profundidad(nodo)<=i):
                    for hijo in nodo.expand():
                        if stop(hijo):
                            return ruta(hijo)
                        if hijo not in expandidos:
                            agenda.appendleft(hijo)

