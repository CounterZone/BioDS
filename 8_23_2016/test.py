import numpy as np
from scipy.integrate import odeint 

from DS_solver import bioDS
test=bioDS(path='SinIRp2/')
test.load()

test.simulate(tmax=30)
test.update()
testp=bioDS(path='SinIRp/')
testp.load()
testp.initials=test.initials
testp.simulate(tmax=30)
testp.display(['SinR_t','Ptap'],save=True,v_line=[2],fname='test')
#v_line=[2,6,8,12,14,18,20,24,26,30,32,36,38]
		
