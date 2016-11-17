# Tools for playing with BioDS models
import matplotlib.pyplot as plt
import numpy as np
from DS_solver import bioDS

def scan_range(model,parameter,exp,space,save="False",fname="range_scan",time=15,show=True,steps=1000,period=6,savelog=False):
	# For oscilating system, scan the range vs given parameter
	# Space is the scanning space, such as [1,2,3,4,5] or np.linspace(1,10,30)
	# exp is the displayed component 
	scan=[]
	plt.clf()
	model.simulate(tmax=time,tsteps=steps)
	model.update()
	for i in space:
		model.set(parameter,i)
		print "processing i=%f"%i
		model.simulate(tmax=time,tsteps=steps)
		if savelog:
			model.display([exp],save=True,show=False,fname=parameter+"=%.2f"%i)
		model.update()
		scan.append(model.trajectory[1])
	trmax=[]
	trmin=[]
	trave=[]
	for i in scan:
		j=i[int(-1.0*period/time*steps):]
		trave.append(np.mean(j,0))
		trmax.append(np.max(j,0))
		trmin.append(np.min(j,0))
	ind=model.components.index(exp)
	ymax=np.array(trmax)[:,ind]
	ymin=np.array(trmin)[:,ind]
	yave=np.array(trave)[:,ind]
	plt.plot(space,ymax,"b--",linewidth=0.5)
	plt.plot(space,ymin,"b--",linewidth=0.5)
	plt.plot(space,yave,'k',label=parameter,linewidth=1.0)
	plt.fill_between(space,ymax,ymin,alpha=0.1)
	plt.xlabel(parameter)
	plt.ylabel(exp)
	plt.legend(bbox_to_anchor=(0.05, 1))
	if save:
		plt.savefig(model.path+fname+".png")
	if show:
		plt.show()
	plt.clf()
	return ymax,ymin,yave
