import math
import random

def SA(ti,tf,k,nveces,x):
	t=ti #temperatura= temperatura inicial
	v=energy(x)
	minimo=x[:]
	n=0
	while t> tf:
		for i in range(nveces):
			xaux=move(x[:])
			vaux=energy(xaux)
			if x!=xaux:
				if energy(minimo)>energy(xaux):
					minimo=xaux[:]
					emin=energy(minimo)
				if vaux<v:
					#aceptar nueva x
					x=xaux
					v=energy(x)
					n+=1
					break
				else:
					prob=random.uniform(0, 1)
					# print str(prob) + "--"+str(math.exp(-(vaux-v)/(k*t)))
					if prob <=math.exp(-(vaux-v)/(k*t)):
						x=xaux
						v=energy(x)
						n+=1
						break
		print str(n)+"  "+ str(x)+"  "+str(energy(x))
		t=0.95*t
	print "min "+str(minimo)+ "  "+str(energy(minimo))
	return minimo

def energy(x):
	global mapa
	global dictMapa
	i=0
	acum=0
	while i<len(x)-1:
		acum+=mapa[dictMapa[x[i]]][dictMapa[x[i+1]]]
		i+=1
	return acum

def move(x):
	# x puedes ser un arreglo de ciudades
	# x puede ser False
	global ciudades
	if (x==False):
		mejor=randomGet(ciudades)
		print "inicial "+str(mejor)+"--"+ str(energy(mejor))
		return mejor
	else:
		mejor=x
		mejor=swap(mejor)
		return mejor

def genMap(arreglo,maximo):
	a=[[0 for x in range(len(arreglo))] for y in range(len(arreglo))] # arreglo con ceros
	i=0
	while i<len(arreglo):
		j=i+1
		while (j<len(arreglo)):
			a[i][j]=random.randrange(maximo)
			a[j][i]=a[i][j]
			j+=1
		i+=1
	return a

def genNCities(n):
	x=[]
	for i in range(n):
		x.append(str(chr(i+65)))
	return x
def randomGet(x):
	return [x.pop(random.randrange(len(x))) for _ in range(len(x))]
def swap(x):
	a=random.randrange(len(x))
	b=random.randrange(len(x))
	x[a], x[b] = x[b], x[a]
	return x
def genDict(n):
	dicti={}
	cont=0
	for i in range(n):
		dicti[str(chr(i+65))]=cont
		cont+=1
	return dicti
dictMapa=genDict(10)
ciudadesAx=genNCities(10)
mapaAx=genMap(ciudadesAx,1000)
ciudades=ciudadesAx[:]
mapa=mapaAx[:]
print dictMapa
print "\t".join(str(i) for i in ciudades)
print "\n".join("\t".join(str(i) for i in j) for j in mapa)
print dictMapa['A']
# energy(randomGet(ciudades))
# x=move(False)
# print "-"+str(x)+"--"+ str(energy(x))
#
# funcion=genMap(10)
# print "\n".join("\t".join(str(i)[:5] for i in j) for j in funcion)
x=move(False)
SA(30,10,0.9,500,x[:])
ciudades=ciudadesAx[:]
mapa=mapaAx[:]
SA(30,10,0.1,500,x[:])
