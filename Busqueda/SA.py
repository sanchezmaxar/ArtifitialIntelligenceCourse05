import math
import random

def SA(ti,tf,k,nveces):
	global funcion
	t=ti #temperatura= temperatura inicial
	x=[random.randint(0,len(funcion)-1),random.randint(0,len(funcion)-1)] #estimacion inicial
	v=energy(x) 
	minimo=x
	emin=v
	while t> tf:
		for i in range(nveces):
			xaux=move(x)
			vaux=energy(xaux)
			if vaux<vaux:
				#aceptar nueva x
				x=xaux
				break
			else:
				prob=random.uniform(0, 1)
				#print prob
				if prob <=k:
					x=xaux
					break	
			if emin>vaux:
				minimo=xaux
		print str(x)+"  "+str(energy(x))
		t=0.95*t
	print minimo
	return minimo

def energy(x):
	global funcion
	return funcion[x[0]][x[1]]

def move(x):
	global funcion
	menorx=False
	menor=False
	for j in range(3):
		for i in range(3):
			try:
				if menor==False and [x[0]+1-i,x[1]+1-j] != x:
					menorx=[x[0]+1-i,x[1]+1-j]
					menor=energy(menorx)
				elif menor> energy([x[0]+1-i,x[1]+1-j]) and [x[0]+1-i,x[1]+1-j] != x:
					menorx=[x[0]+1-i,x[1]+1-j]
					menor=energy(menorx)
			except:
				pass
	return menorx

def genMap(dimension):
	salida=[]
	for i in range(dimension):
		aux=[]
		for j in range(dimension):
			aux.append(random.uniform(0,100))
		salida.append(aux)
	return salida

funcion=genMap(10)
print "\n".join("\t".join(str(i)[:5] for i in j) for j in funcion)
SA(15,10,0.082,5000)