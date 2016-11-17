import numpy as np
from scipy.integrate import odeint 

from DS_solver import bioDS
test=bioDS(path='SinIR_simple/')
test.load()
test.set("Spo0A_p",0)
test.simulate(tmax=30)
test.update()
test.clear()
test.simulate(tmax=5)

test.set("Spo0A_p",2)
test.simulate(tmin=5,tmax=45)

test.update()

test.set("Spo0A_p",0)
test.simulate(tmin=45,tmax=65)

test.display(test.components,save=True,fname='test',v_line=[5,45])
#v_line=[2,6,8,12,14,18,20,24,26,30,32,36,38]
