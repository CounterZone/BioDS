ppath='SinIR_delayf2_d/'
import numpy as np
from scipy.integrate import odeint 
import pickle
from DS_solver import bioDS
from cell_cycle import cell
import matplotlib.pyplot as plt
import 	scipy.ndimage.filters as filters
length=10000
start=30000
tt,yy,zz=pickle.load(open(ppath+"f.pickle"))
yy=filters.gaussian_filter(yy,20)
plt.plot(tt[start:start+length],yy[start:start+length])
plt.plot(tt[start:start+length],zz[start:start+length])
plt.show()
