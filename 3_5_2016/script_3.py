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
kinccc=bioDS(path="KinC_2/")
kinccc.load()
kinc=bioDS(path="KinC_3/")
kinc.load()
kd2=[1000,500,300,100]
cs={}
kincc=bioDS(path="KinC_0/")

kincc.load()

for i in kd2:
	print(i)
	kinc.set("kd2",i)
	cs[i]=tools.scan_range(kinc,parameter='viKinA',exp='Spo0A_p',space=np.linspace(0,20,60),save=True,show=False,fname="range_k2_%d"%i,savelog=False,time=30)
cc=tools.scan_range(kincc,parameter='viKinA',exp='Spo0A_p',space=np.linspace(0,20,60),save=False,savelog=False,show=False,time=30)
ccc=tools.scan_range(kinccc,parameter='viKinA',exp='Spo0A_p',space=np.linspace(0,20,60),save=False,savelog=False,show=False,time=30)
for i in kd2:
	plt.plot(np.linspace(0,20,60),cs[i][0],"b--",linewidth=0.5)
	plt.plot(np.linspace(0,20,60),cs[i][1],"b--",linewidth=0.5)
	plt.plot(np.linspace(0,20,60),cs[i][2],label="kd2=%d"%i,linewidth=1.0)
	plt.fill_between(np.linspace(0,20,60),cs[i][0],cs[i][1],alpha=0.1)

plt.plot(np.linspace(0,20,60),cc[0],"b--",linewidth=0.5)
plt.plot(np.linspace(0,20,60),cc[1],"b--",linewidth=0.5)
plt.plot(np.linspace(0,20,60),cc[2],label="KinA",linewidth=2.0)
plt.fill_between(np.linspace(0,20,60),cc[0],cc[1],alpha=0.1)
plt.plot(np.linspace(0,20,60),ccc[0],"b--",linewidth=0.5)
plt.plot(np.linspace(0,20,60),ccc[1],"b--",linewidth=0.5)
plt.plot(np.linspace(0,20,60),ccc[2],label="without_dp",linewidth=2.0)
plt.fill_between(np.linspace(0,20,60),ccc[0],ccc[1],alpha=0.1)
plt.legend(bbox_to_anchor=(0.15, 1))
plt.xlabel("ViKinC")
plt.ylabel("Spo0A_p")
plt.savefig("KinC_3/scan_kd2.pdf")
plt.show()

