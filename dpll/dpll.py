#!/usr/bin/python
# -*- coding: utf-8 -*-
def getExpression(linea):
	return [i[1:-1].split("v") for i in linea.split("^")]
def phi(expresion,literal):
	i=0
	while i<len(expresion):
		j=0
		while j<len(expresion[i]):
			if expresion[i][j]==literal:
				expresion.pop(i)
				i-=1
				break #por que ya no hay mas cosas en este arreglo alv
			if (len(literal)==1 and expresion[i][j][0]=="!" and expresion[i][j][-1]==literal) or (expresion[i][j]==literal[-1]):
				expresion[i].pop(j)
				j-=1
			j+=1
		i+=1
	return expresion
def dpll(expresion):
	cond=False
	unica=""
	if expresion==None:
		return True
	elif expresion==[]:
		return True
	elif [] in expresion:
		return False
	for i in expresion:
		if len(i)==1:
			cond=True
			letra=i[0]
		for j in i:
			if unica=="":
				unica=j
				cond2=True
				br=False
				for k in range(len(expresion)):
					for m in range(len(expresion[k])):
						if ((expresion[k][m] in unica) or (unica in expresion[k][m])) and unica!=expresion[k][m]:
							cond2=False
							br=True
							break
					if br:
						break
				if cond2==False:
					unica=""
	if cond:
		return dpll(phi(expresion,letra))
	elif unica!="":
		return dpll(phi(expresion,unica))
	else :
		if dpll(phi(expresion[:],expresion[:][0][0])):
			return True
		else:
			return dpll(phi(expresion,"!"+expresion[0][0]))
#trae ejemplos precargados
e="(P)^(P)^(Q)"
f="(Av!BvC)^(!B)^(BvDvF)^(!Dv!F)^(!Cv!D!F)^(H)"
h="(AvB)^(Av!B)^(!AvB)^(!Av!B)"
print dpll(getExpression(h))
print dpll(getExpression(e))
print dpll(getExpression(f))