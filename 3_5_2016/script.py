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
cs={}
for i in vi:
	print(i)
	kinc.set("ki",i)
	cs[i]=tools.scan_range(kinc,parameter='viKinA',exp='Spo0A_p',space=np.linspace(0,20,60),save=True,show=False,fname="range_ki_%d"%i,savelog=False,time=30)
	print len(cs[i][1])
for i in vi:
	ymax=cs[i][0]
	ymin=cs[i][1]
	yave=cs[i][2]
	plt.plot(np.linspace(0,20,60),ymax,"b--",linewidth=0.5)
	plt.plot(np.linspace(0,20,60),ymin,"b--",linewidth=0.5)
	plt.plot(np.linspace(0,20,60),yave,label="ki=%d"%i,linewidth=1.0)
#	plt.fill_between(np.linspace(0,20,60),ymax,ymin,alpha=0.1)
kincc=bioDS(path="KinC_1/")
kincc.load()
cc=tools.scan_range(kincc,parameter='viKinA',exp='Spo0A_p',space=np.linspace(0,20,60),save=False,savelog=False,show=False,time=30)
ymax=cc[0]
ymin=cc[1]
yave=cc[2]
plt.plot(np.linspace(0,20,60),ymax,"b--",linewidth=0.5)
plt.plot(np.linspace(0,20,60),ymin,"b--",linewidth=0.5)
plt.plot(np.linspace(0,20,60),yave,label="ki=Inf",linewidth=1.0)
#plt.fill_between(np.linspace(0,20,60),ymax,ymin,alpha=0.1)

plt.legend(bbox_to_anchor=(0.05, 1))
plt.xlabel("ViKinC")
plt.ylabel("Spo0A_p")
plt.savefig("KinC_0/scan_ki.pdf")
plt.show()

