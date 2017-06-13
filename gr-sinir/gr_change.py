import numpy as np
from scipy.integrate import odeint 
import matplotlib.pyplot as plt

from DS_solver import bioDS
g=bioDS(path='SinIR_simple/')
g.load()
g.set("Spo0A_p",2)
res=[]
g.set('Tg',1)
g.set('Tr',0.206+0.675) 




g.set('SinR',1000)
g.set('SlrR',000)


g.simulate(tmin=0,tmax=10)
#g.display(['Ptap'])
for i in range(2,20):
	g.load()
	g.set("Spo0A_p",2)
	g.set('Tg',i/2)
	g.set('Tr',0.0206*i*5+0.675) 
	g.set('SinR',1000)
	g.set('SlrR',000)
	g.simulate(tmin=g.trajectory[0][-1],tmax=g.trajectory[0][-1]+200)
	print(i)
	res.append(max(g.getTrajectory('Ptap')[-30:-1]))
plt.plot(np.array(range(2,20))/2.0,res)
plt.show()

