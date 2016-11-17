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
kinc=bioDS(path="KinC_4_ir/")
kinc.load()
kina=bioDS(path="KinC_3_ir/")
kina.load()


cc=tools.scan_range(kinc,parameter='viKinA',exp='Spo0A_p',space=np.linspace(0,20,60),save=False,savelog=False,show=False,time=30)
aa=tools.scan_range(kina,parameter='viKinA',exp='Spo0A_p',space=np.linspace(0,20,60),save=False,savelog=False,show=False,time=30)

plt.plot(np.linspace(0,20,60),cc[0],"b--",linewidth=0.5)
plt.plot(np.linspace(0,20,60),cc[1],"b--",linewidth=0.5)
plt.plot(np.linspace(0,20,60),cc[2],label="0B-",linewidth=2.0)
plt.fill_between(np.linspace(0,20,60),cc[0],cc[1],alpha=0.1)
plt.plot(np.linspace(0,20,60),aa[0],"b--",linewidth=0.5)
plt.plot(np.linspace(0,20,60),aa[1],"b--",linewidth=0.5)
plt.plot(np.linspace(0,20,60),aa[2],label="KinC",linewidth=2.0)
plt.fill_between(np.linspace(0,20,60),aa[0],aa[1],alpha=0.1)
plt.legend(bbox_to_anchor=(0.15, 1))
plt.plot([0,20],[0.4,0.4],"b--")
plt.plot([0,20],[0.8,0.8],"b--")
plt.plot([0,20],[1.5,1.5],"b--")
plt.xlabel("ViKin")
plt.ylabel("Spo0A_p")
plt.savefig("KinC_4/threshold.pdf")
plt.show()

