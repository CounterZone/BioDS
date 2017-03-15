import numpy as np
from scipy.integrate import odeint 

from DS_solver import bioDS
test=bioDS(path='KinA/')
test.load()
'''
test.set("trep",0)
test.set('viKinA',4.36)
test.add(reactions='SinIR_simple/reactions.config',initials='',parameters='SinIR_simple/parameters.config')
test.simulate(tmax=30,tsteps=500)
test.update()
test.clear()
test.simulate(tmax=30,tsteps=500)
q=test.display(['Spo0A_p'],save=True,v_line=[2,6,8,12,14,18,20],fname='ap1')
q=test.display(['Ptap'],save=True,v_line=[2,6,8,12,14,18,20],fname='tap1')
'''
test.set("trep",1)
test.set('tt',2)
test.set('viKinA',5)
test.simulate(tmax=50,tsteps=500)
test.update()
test.clear()
test.simulate(tmax=30,tsteps=500)
q2=test.display(['Spo0A_p'],save=True,v_line=[2,6,8,12,14,18,20],fname='ap2')
#q=test.display(['Ptap'],save=True,v_line=[2,6,8,12,14,18,20],fname='tap2')
#v_line=[2,6,8,12,14,18,20,24,26,30,32,36,38]
		