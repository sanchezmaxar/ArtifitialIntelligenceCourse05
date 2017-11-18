#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 12:39:57 2017

@author: stan
"""
import heapq
from utils import *

from puzzle import *
from manhattan import *

class Astar:
    @staticmethod
    def search(origen,stop,heuristica):
        agenda = []
        expandidos = set()
        if stop(origen):
            return ruta(origen)
        heapq.heappush(agenda,(0,origen))
        while agenda:
            nodo = heapq.heappop(agenda)[1]
            expandidos.add(nodo)
            if stop(nodo):
                return ruta(nodo)
            for hijo in nodo.expand():
                if hijo not in expandidos:
                    heapq.heappush(agenda,\
                                   (heuristica(hijo)+profundidad(hijo),hijo))
tablero = Puzzle()
tablero = tablero.shuffle(100)
print tablero
stop =lambda x: x == Puzzle()
print len(Astar().search(tablero,\
    stop,\
    ManhattanDistance().distance_to_target))