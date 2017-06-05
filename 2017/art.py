import numpy as np
from scipy.integrate import odeint 
import matplotlib.pyplot as plt
from DS_solver import bioDS
test=bioDS(path='KinA_art/')
test.load()
puls=[]

for i in [0.5,1,2,3,4]:
	print i
	test.load()
	test.set("k",i)
	test.add(reactions='SinIR_simple/reactions.config',initials='',parameters='SinIR_simple/parameters.config')
	test.simulate(tmax=60,tsteps=300)
	test.update()
	test.clear()
	test.simulate(tmax=30,tsteps=300)
	tap=test.getTrajectory('Ptap')
	puls.append(np.mean(tap))
plt.plot([0.5,1,2,3,4],puls,'o-',label='pulsatile')
plt.legend()
plt.xlabel('0A~P frequency')
plt.ylabel('tapA response')
plt.savefig('FF.png')
