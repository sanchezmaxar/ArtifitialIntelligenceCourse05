import random
boolean={0:"False",1:"True"}
neg={"False":"True","True":"False"}
def  Decode(propi,vars,vals):
	exp = "|".join(propi)
	for i in range(len(vars)):
		exp = exp.replace(vars[i],vals[i])
	return exp
def FClause(prop,vars,vals):
	for j in range(len(prop)):
		exp = Decode(prop[j],vars,vals)
		if not eval(exp):
			return j
	return -1
def WALKSAT(prop,n,m):
	vars = []
	vals = []
	propaux = ""
	prop=prop.replace("F","0")
	prop=prop.replace("T","1")
	for c in prop:
		if c not in vars and c.isalnum():
			vars.append(c)
	prop = prop.replace("(","")
	prop = prop.replace(")","")
	propaux = prop.replace("!","")
	prop = prop.replace("!","not ")
	prop = [["("+ el + ")" for el in p.split("|")] for p in prop.split("&")]
	propaux = [[el for el in p.split("|")] for p in propaux.split("&")]
	for i in range(n):
		vals = [boolean[random.randrange(2)] for j in range(len(vars))]
		for j in range(m):
			ind = FClause(prop[:],vars,vals)
			if ind==-1:
				return "True"
			else:
				if random.randrange(2)==0:
					x = vars.index(propaux[ind][random.randrange(len(propaux[ind]))])
					vals[x] = neg[vals[x]]
				else:
					ind2= vars.index(propaux[ind][0])
					mini = [eval(Decode(p,vars,vals)) for p in prop].count(False)
					for k in range(1,len(propaux[ind])):
						x = vars.index(propaux[ind][k])
						vals[x] = neg[vals[x]]
						cost = [eval(Decode(p,vars,vals)) for p in prop].count(False)
						if cost<mini:
							mini=cost
							ind2=x
						vals[x] = neg[vals[x]]
					vals[x] = neg[vals[x]]
	return "False"
print WALKSAT( "(A|B|C)&(A|B|!C)&(A|!B|C)&(A|!B|!C)&(!A|B|C)&(!A|B|!C)&(!A|!B|C)&(!A|!B|!C)",1,10)