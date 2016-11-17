import numpy as np
from scipy.integrate import odeint 

from DS_solver import bioDS
from cell_cycle import cell
test=cell(path='SinIR_delayf2_d/')
test.load()
test.set("Spo0A_p",0)
test.simulate(tmax=30)
test.update()
test.clear()
for i in range(200):
	test.simulate(tmin=i*0.5,tmax=i*0.5+0.5,tsteps=50)
	print(1)
	test.parameterTurn(sigma=0.25)



test.display(['Ptap','Pmot'],save=True,fname='test')
#v_line=[2,6,8,12,14,18,20,24,26,30,32,36,38]
