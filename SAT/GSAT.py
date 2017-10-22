import random
boolean={0:"False",1:"True"}
neg={"False":"True","True":"False"}
def MinCost(prop,vars,vals):
	costs = []
	propaux=prop
	for i in range(len(vals)):
		for j in range(len(vars)):
			propaux = propaux.replace(vars[j],vals[i][j])
		exprs=propaux.split("&")
		costs.append([eval(exp) for exp in exprs].count(False))
		propaux = prop
	ind = 0
	mini = costs[0]
	for i in range(1,len(costs)):
		if costs[i]<mini:
			mini=costs[i]
			ind=i
	if costs[ind]==0:
		vals[ind].append("True")
	else:
		vals[ind].append("False")
	return vals[ind]
def Flip(vals):
	flips = []
	for i in range(len(vals)):
		vals[i] = neg[vals[i]]
		flips.append(map(str,vals[:]))
		vals[i] = neg[vals[i]]
	return flips
def GSAT(prop,n,m):
	vars = []
	vals = []
	propaux = ""
	neg=False
	prop=prop.replace("F","0")
	prop=prop.replace("T","1")
	for c in prop:
		if c not in vars and c.isalnum():
			vars.append(c)
	for c in prop:
		if c == "!":
			propaux+="(not "
			neg=True
		elif c.isalnum():
			propaux += c
			if neg:
				propaux+=")"
				neg=False
		else:
			propaux+=c
	prop = propaux
	for i in range(n):
		vals = [boolean[random.randrange(2)] for j in range(len(vars))]
		for j in range(m):
			vals = MinCost(prop,vars,Flip(vals))
			if vals.pop()=="True":
				return "True"
	return "False"

satis = GSAT("(A|B|C)&(A|B|!C)&(A|!B|C)&(A|!B|!C)&(!A|B|C)&(!A|B|!C)&(!A|!B|C)",1,2)
print satis