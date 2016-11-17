import numpy as np
from scipy.integrate import odeint 
import pickle
from DS_solver import bioDS
from cell_cycle import cell
import matplotlib.pyplot as plt
test=cell(path='SinIR_feedback2/')
test.load()
test.set("Spo0A_p",0)
test.simulate(tmax=30)
test.update()
test.clear()
for i in range(30000):
	test.simulate(tmin=i*0.5,tmax=i*0.5+0.5,tsteps=30)
	test.parameterTurn(sigma=0.25)
	if (i/100)*100==i:
		print i
tt=test.trajectory[0]
yy=test.getTrajectory('Ptap')
pickle.dump([tt,yy],open("ttyy-fb2.pickle",'wb'))
for threshold in [60,80,100,120,140,160,180,200,250,300]:
	chain=[]
	mot=[]
	s=0
	t=0
	if yy[0]>threshold:
		s=1
	for i in range(1,len(tt)):
		if s==0:
			if yy[i]>threshold:
				s=1
				mot.append(tt[i]-t)
				t=tt[i]
		else:
			if yy[i]<threshold:
				s=0
				chain.append(tt[i]-t)
				t=tt[i]
	hist1,bin1=np.histogram(chain,bins=10)
	hist2,bin2=np.histogram(mot,bins=10)
	center=(bin1[:-1]+bin1[1:])/2
	plt.bar(center,hist1,align='center',width=0.7*(bin1[1]-bin1[0]))
	plt.savefig('SinIR_feedback2/t%d_chain.pdf'%threshold)
	plt.clf()
	center=(bin2[:-1]+bin2[1:])/2
	plt.bar(center,hist2,align='center',width=0.7*(bin2[1]-bin2[0]))
	plt.savefig('SinIR_feedback2/t%d_mot.pdf'%threshold)
	plt.clf()

			
