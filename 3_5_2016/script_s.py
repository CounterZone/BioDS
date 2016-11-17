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
sc=bioDS(path="KinC_3_ir/")
sc.load()
sa=bioDS(path="KinA_0/")
sa.load()
sa.add(parameters="../s_parameter",reactions="../s_reaction")
sc.add(parameters="../s_parameter",reactions="../s_reaction")


atap=tools.scan_range(sa,parameter='viKinA',exp='ptapa',space=np.linspace(0,20,60),save=False,savelog=False,show=False,time=30)
aspo=tools.scan_range(sa,parameter='viKinA',exp='pspoIIg',space=np.linspace(0,20,60),save=False,savelog=False,show=False,time=30)
ctap=tools.scan_range(sc,parameter='viKinA',exp='ptapa',space=np.linspace(0,20,60),save=False,savelog=False,show=False,time=30)
cspo=tools.scan_range(sc,parameter='viKinA',exp='pspoIIg',space=np.linspace(0,20,60),save=False,savelog=False,show=False,time=30)

plt.plot(np.linspace(0,20,60),atap[0],"b--",linewidth=0.5)
plt.plot(np.linspace(0,20,60),atap[1],"b--",linewidth=0.5)
plt.plot(np.linspace(0,20,60),atap[2],label="KinA_tap",linewidth=2.0)
plt.fill_between(np.linspace(0,20,60),atap[0],atap[1],alpha=0.1)

plt.plot(np.linspace(0,20,60),aspo[0],"b--",linewidth=0.5)
plt.plot(np.linspace(0,20,60),aspo[1],"b--",linewidth=0.5)
plt.plot(np.linspace(0,20,60),aspo[2],label="KinA_spo",linewidth=2.0)
plt.fill_between(np.linspace(0,20,60),aspo[0],aspo[1],alpha=0.1)

plt.plot(np.linspace(0,20,60),ctap[0],"b--",linewidth=0.5)
plt.plot(np.linspace(0,20,60),ctap[1],"b--",linewidth=0.5)
plt.plot(np.linspace(0,20,60),ctap[2],label="KinC_tap",linewidth=2.0)
plt.fill_between(np.linspace(0,20,60),ctap[0],ctap[1],alpha=0.1)

plt.plot(np.linspace(0,20,60),cspo[0],"b--",linewidth=0.5)
plt.plot(np.linspace(0,20,60),cspo[1],"b--",linewidth=0.5)
plt.plot(np.linspace(0,20,60),cspo[2],label="KinC_spo",linewidth=2.0)
plt.fill_between(np.linspace(0,20,60),cspo[0],cspo[1],alpha=0.1)



plt.legend(bbox_to_anchor=(0.15, 1))
plt.xlabel("ViKin")
plt.ylabel("Reporter")
plt.savefig("KinC_3_ir/a_c_4.pdf")
plt.show()

