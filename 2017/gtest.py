import numpy as np
from scipy.integrate import odeint 
import matplotlib.pyplot as plt
from BioDS.DS_solver import bioDS
test=bioDS(path='KinA/')
'''
test.load()

test.set("trep",0)
#test.set("tt",6)
test.set('viKinA',5)
test.add(reactions='SinIR_simple/reactions.config',initials='',parameters='SinIR_simple/parameters.config')
test.simulate(tmax=60,tsteps=300)
test.update()
test.clear()
test.simulate(tmax=30,tsteps=300)
ap=test.getTrajectory('Spo0A_p')
tap=test.getTrajectory('Ptap')
plt.plot(test.trajectory[0],ap,label='Spo0A_p')
plt.xlabel('time/h')
plt.ylabel('intensity/nM')
plt.ylim(0,1)
plt.legend()
plt.savefig('spo0A.png')
plt.show()
q2=test.display(['Spo0A_p'],save=False,v_line=[2,6,8,12,14,18,20],fname='ap2')

plt.plot(test.trajectory[0],tap,label='tapA')
plt.xlabel('time/h')
plt.ylabel('intensity/nM')
plt.ylim(0,2000)
plt.legend()
plt.savefig('tap.png')
plt.show()

test=bioDS(path='KinA/')
test.load()

test.set("trep",2)
#test.set("tt",6)
test.set('viKinA',5)
test.add(reactions='SinIR_simple/reactions.config',initials='',parameters='SinIR_simple/parameters.config')
test.simulate(tmax=60,tsteps=300)
test.update()
test.clear()
test.simulate(tmax=30,tsteps=300)
ap=test.getTrajectory('Spo0A_p')
tap=test.getTrajectory('Ptap')
plt.plot(test.trajectory[0],ap,label='Spo0A_p')
plt.xlabel('time/h')
plt.ylabel('intensity/nM')
plt.ylim(0,1)
plt.legend()
plt.savefig('spo0A0.png')
plt.show()
q2=test.display(['Spo0A_p'],save=False,v_line=[2,6,8,12,14,18,20],fname='ap2')

plt.plot(test.trajectory[0],tap,label='tapA')
plt.xlabel('time/h')
plt.ylabel('intensity/nM')
plt.ylim(0,2000)
plt.legend()
plt.savefig('tap0.png')
plt.show()
'''
puls=[]
unpuls=[]
s0=[]
s1=[]

for i in [3,4,5,6,7,8]:
	print i
	test.load()
	test.set('viKinA',i)
	test.set("trep",2)

	test.simulate(tmax=60,tsteps=300)
	test.update()
	test.clear()
	test.simulate(tmax=6,tsteps=300)
	ap=test.getTrajectory('Spo0A_p')
	gg=test.getTrajectory('SpoIIG')
	puls.append(np.mean(gg))
	s0.append(np.mean(ap))
for i in [3,4,5,6,7,8]:
	print i
	test.load()
	test.set('viKinA',i)
	test.set("trep",0)
	test.simulate(tmax=60,tsteps=300)
	test.update()
	test.clear()
	test.simulate(tmax=6,tsteps=300)
	ap=test.getTrajectory('Spo0A_p')
	gg=test.getTrajectory('SpoIIG')
	unpuls.append(np.mean(gg))
	s1.append(np.mean(ap))
plt.plot([3,4,5,6,7,8],puls,'o-',label='pulsatile')
plt.plot([3,4,5,6,7,8],unpuls,'o-',label='non-pulsatile')
plt.legend(loc='best')
plt.xlabel('Kinase level')
plt.ylabel('SpoIIG response')
plt.savefig('gpvnp1.png')
plt.clf()
plt.plot(s0,puls,'o-',label='pulsatile')
plt.plot(s1,unpuls,'o-',label='non-pulsatile')
plt.legend(loc='best')
plt.xlabel('0A~P level')
plt.ylabel('SpoIIG response')
plt.savefig('gpvnp2.png')

'''
test.set("trep",1)
test.set('tt',2)
test.set('viKinA',5)
test.simulate(tmax=50,tsteps=500)
test.update()
test.clear()
test.simulate(tmax=30,tsteps=500)
q2=test.display(['Spo0A_p'],save=True,v_line=[2,6,8,12,14,18,20],fname='ap2')
#q=test.display(['Ptap'],save=True,v_line=[2,6,8,12,14,18,20],fname='tap2')
#v_line=[2,6,8,12,14,18,20,24,26,30,32,36,38]
		'''
