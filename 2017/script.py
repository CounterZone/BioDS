##############################
# 3/5/2016

# 1 modify the reaction scheme

####

# 2 Optimize the plot

####

####

####

####

####



import tools
from DS_solver import bioDS
import numpy as np
import matplotlib.pyplot as plt

kinc=bioDS(path="KinC/")
kinc.load()




cs=tools.scan_range(kinc,parameter='viKinA',exp='Spo0A_p',space=np.linspace(0,20,5),save=True,show=False,fname="skina",savelog=False,time=30)
print len(cs[1])
'''
ymax=cs[0]
ymin=cs[1]
yave=cs[2]
plt.plot(np.linspace(0,20,5),ymax,"b--",linewidth=0.5)
plt.plot(np.linspace(0,20,5),ymin,"b--",linewidth=0.5)
plt.plot(np.linspace(0,20,5),yave,label="WT",linewidth=1.0)
#	plt.fill_between(np.linspace(0,20,60),ymax,ymin,alpha=0.1)
'''
kinc.set('trep',0)
ymin=cs[1]
yave=cs[2]
ymax=cs[0]
plt.plot(np.linspace(0,20,5),ymax,"b--",linewidth=0.5)
plt.plot(np.linspace(0,20,5),ymin,"b--",linewidth=0.5)
plt.plot(np.linspace(0,20,5),yave,label="Transloc",linewidth=1.0)
plt.show()

