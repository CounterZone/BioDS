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

kinc=bioDS(path="KinC_0/")
kinc.load()
vi=[100,500,1000,5000]
kincc=bioDS(path="KinC_1/")
kincc.load()
cs={}
for i in vi:
	print(i)
	kinc.set("ki",i)
	cs[i]=tools.scan_range(kinc,parameter='viKinA',exp='Spo0A_p',space=np.linspace(0,20,60),save=True,show=False,fname="range_ki_%d"%i,savelog=False,time=30)
cc=tools.scan_range(kincc,parameter='viKinA',exp='Spo0A_p',space=np.linspace(0,20,60),save=False,savelog=False,show=False,time=30)
for i in vi:
	plt.plot(np.linspace(0,20,60),cs[i][0],"b--",linewidth=0.5)
	plt.plot(np.linspace(0,20,60),cs[i][1],"b--",linewidth=0.5)
	plt.plot(np.linspace(0,20,60),cs[i][2],label="ki=%d"%i,linewidth=1.0)
	plt.fill_between(np.linspace(0,20,60),cs[i][0],cs[i][1],alpha=0.1)


plt.plot(np.linspace(0,20,60),cc[0],"b--",linewidth=0.5)
plt.plot(np.linspace(0,20,60),cc[1],"b--",linewidth=0.5)
plt.plot(np.linspace(0,20,60),cc[2],label="ki=Inf",linewidth=1.0)
plt.fill_between(np.linspace(0,20,60),cc[0],cc[1],alpha=0.1)

plt.legend(bbox_to_anchor=(0.05, 1))
plt.xlabel("ViKinC")
plt.ylabel("Spo0A_p")
plt.savefig("KinC_0/scan_ki.pdf")
plt.show()

