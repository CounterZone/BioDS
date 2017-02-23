import numpy as np
from scipy.integrate import odeint 

from DS_solver import bioDS
test=bioDS(path='KinA_0/')
test.load()
test.simulate(tmax=30,tsteps=500)

test.display(['Spo0A_p'],save=True,v_line=[2,6,8,12,14,18,20],fname='test')
#v_line=[2,6,8,12,14,18,20,24,26,30,32,36,38]
		
