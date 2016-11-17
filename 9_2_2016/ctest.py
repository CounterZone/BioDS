import numpy as np
from scipy.integrate import odeint 

from DS_solver import bioDS

test=bioDS(path='SinIR_delay2/')
test.load()
#test.set("Spo0A_p",2)
#test.set("trr",0)
test.simulate(tmax=20)
test.update()
test.set("SlrR",1000)
test.simulate(tmin=20,tmax=50)
'''
test.update()
test.set("SinR",200)
test.simulate(tmin=20,tmax=30)
test.update()
test.set("SinR",100)
test.simulate(tmin=30,tmax=40)
test.update()
test.set("SinR",50)
test.simulate(tmin=40,tmax=50)

test.set("SinR",0)
test.simulate(tmin=50,tmax=65)

'''
test.display(test.components,save=True,fname='test')
#v_line=[2,6,8,12,14,18,20,24,26,30,32,36,38]
