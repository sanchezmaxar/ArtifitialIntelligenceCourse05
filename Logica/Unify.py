bound={}
def Update():
	values = bound.values()
	keys = bound.keys()
	for i in range(len(values)):
		if values[i] in bound:
			bound[keys[i]]=bound[values[i]]
def IsVariable(x):
	if x[0].isupper():
		return False
	for i in range(len(x)):
		if not x[i].isalpha():
			return False
	return True
def IsConstant(x):
	if x[0].islower():
		return False
	for i in range(len(x)):
		if not x[i].isalpha():
			return False
	return True
def IsPredicateOrFunction(x):
	if x[0]=="[":
		return False
	for i in range(len(x)):
		if x[i]=="(":
			return True
	return False
def Args(x):
	return "["+x[x.find("(")+1:-1]+"]"
def Operator(x):
	return "".join(x.split("(")[:1])
def  Res(x):
	return "["+",".join(x.split(",")[1:])
def  First(x):
	return "".join(",".join(x.split(",")[0:1])[1:].split("]"))
def  CountArgs(x):
	return len(x.split(","))
def  Unify_var(x,y,s):
	if x in bound:
		return Unify(bound[x],y,s)
	elif y in bound:
		return Unify(x,bound[y],s)
	elif IsPredicateOrFunction(y) and (x in y):
		return "fail"
	else:
		bound[x]=y
		s=bound
		return s
def Unify(x,y,s):
	if s=="fail":
		return "fail"
	elif x==y:
		Update()
		return s
	elif IsVariable(x):
		return Unify_var(x,y,s);
	elif IsVariable(y):
		return Unify_var(y,x,s);
	elif IsPredicateOrFunction(x) or IsPredicateOrFunction(y):
		if Operator(x)==Operator(y):
			return Unify(Args(x),Args(y),s)
		else:
			return "fail"
	elif IsConstant(x) and IsConstant(y):
		return "fail"
	else:
		if CountArgs(x)==CountArgs(y):
			return Unify(Res(x),Res(y),Unify(First(x),First(y),s))
		else:
			return "fail"
print Unify("P(x,F(G(m)),B)","P(G(A),F(G(c)),A)",{})