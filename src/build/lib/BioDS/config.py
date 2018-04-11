############################################################################

# Import parameters, equations and initial values

# parameter

# input: XX = xx

# output: {XX:xx}

# equations

# input: A + 2*B -> C+D  |  k1*C
#	 D->C		 |  k2
# output:

# components:[A,B,C,D](sorted by name)

# equations:{A:{1:-1},B:{1:-2},C:{1:1,2:1},D:{1:1,2:-1}}

# reactions:{1:"k1*C",2:"k2"}

# initials: same to parameters

##############################################################################
import numpy as np
import os
def pre_process(string):
	return string.replace(" ","").replace("\n","").replace("\t","")
	
def import_parameters(filename,parameters={}):
	f=open(filename)
	for i in f.readlines():
		i=pre_process(i)
		if i=="" or i[0]=="#":
			continue
		parameters[i.split("=")[0]]=float(i.split("=")[1])
	return parameters

def import_equations(filename,equations={},reactions={}):
	f=open(filename)
	if reactions=={}:
		rid=1
	else:
		rid=max(reactions.keys())+1
	for i in f.readlines():
		i=pre_process(i)		
		if i=="" or i[0]=="#":
			continue
		kinetics=i.split("|")[1]
		reactions[rid]=kinetics
		i=i.split("|")[0]	
		left=i.split("->")[0]
		right=i.split("->")[1]
		for j in (left+"+"+right).split("+"):
			if j=='':
				continue
			if j.find("*")>0:
				n=float(j.split("*")[0])
				co=j.split("*")[1]
			else:
				n=1
				co=j
			if j in left.split("+"):
				n=n*(-1)
			if not co in equations.keys():
				equations[co]={rid:n}
			else:
				equations[co][rid]=n
		rid=rid+1
	components=sorted(equations.keys())
	return components,equations,reactions

def import_initials(components,filename,initials={}):
        ii=np.zeros(len(components))
	if not (filename=='' or os.path.isdir(filename)):
		f=open(filename)
		for i in f.readlines():
			i=pre_process(i)
			if i=="" or i[0]=="#":
				continue
			initials[i.split("=")[0]]=float(i.split("=")[1])
        for i in initials.keys():
            ii[components.index(i)]+=initials[i]
	return ii
