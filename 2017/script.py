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

kinc.set('trep',0)

kina=bioDS(path="KinA/")
kina.load()

kina.set('trep',0)


cs2=tools.scan_range(kina,parameter='viKinA',exp='Spo0A_p',space=np.linspace(0,20,10),save=True,show=False,fname="skina",savelog=False,time=40)

'''
ymax=cs[0]
ymin=cs[1]
yave=cs[2]
plt.plot(np.linspace(0,20,5),ymax,"b--",linewidth=0.5)
plt.plot(np.linspace(0,20,5),ymin,"b--",linewidth=0.5)
plt.plot(np.linspace(0,20,5),yave,label="WT",linewidth=1.0)
#	plt.fill_between(np.linspace(0,20,60),ymax,ymin,alpha=0.1)
'''




kinc.set("ka2",100)

cs=tools.scan_range(kinc,parameter='viKinA',exp='KinA_p',space=np.linspace(0,20,10),save=True,show=False,fname="skina",savelog=False,time=40)
ymin=cs[1]
yave=cs[2]
ymax=cs[0]
plt.plot(np.linspace(0,20,10),ymax,"b--",linewidth=0.5)
plt.plot(np.linspace(0,20,10),ymin,"b--",linewidth=0.5)
plt.plot(np.linspace(0,20,10),yave,label="kinC",linewidth=1.0)




ymin=cs2[1]
yave=cs2[2]
ymax=cs2[0]
plt.plot(np.linspace(0,20,10),ymax,"b--",linewidth=0.5)
plt.plot(np.linspace(0,20,10),ymin,"b--",linewidth=0.5)
plt.plot(np.linspace(0,20,10),yave,label="kinA",linewidth=1.0)
plt.ylabel("Spo0A_p")
plt.xlabel("v_kinase")
plt.legend()



plt.show()
