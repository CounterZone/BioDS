ppath='SinIR_delayf2/'
import numpy as np
from scipy.integrate import odeint 
import pickle
from DS_solver import bioDS
from cell_cycle import cell
import matplotlib.pyplot as plt
import 	scipy.ndimage.filters as filters
#for ppath in ['SinIR_delayf2_d/','SinIR_delayf2/','SinIR_delayk05/','SinIR_delayk05_2/','SinIR_delayk05_3/','SinIR_delayf2_2/','SinIR_delayf2_3/','SinIR_delayf3/','SinIR_delayk02/','SinIR_delayk1/']:
for kkk in [5]:
	print(ppath)	
	tt,yy,zz=pickle.load(open(ppath+"f.pickle"))
	yy=filters.gaussian_filter(yy,5)
	maximx=[]
	maximy=[]
	for k in range(len(zz)-1):
		if yy[k]>yy[k-1] and yy[k]>yy[k+1]:
			maximx.append(yy[k])
			maximy.append(zz[k])
	hist1,bin1=np.histogram(maximx,bins=50)
	center=(bin1[:-1]+bin1[1:])/2
	plt.bar(center,hist1,align='center',width=0.7*(bin1[1]-bin1[0]))
	#plt.scatter(maximx,maximy)
	plt.show()		
