#####
# scan the average and the range of the output of KinA_changed and KinC_changed
# save them in the directory
# 3/3/2016
####
from DS_solver import bioDS
import numpy as np
import matplotlib.pyplot as plt
kina=bioDS(path="KinA_sim/")
kinc=bioDS(path="KinC_sim/")
kina.load()
kinc.load()
a_scan=[]
c_scan=[]
#####

# for different parameters(kcat of phosphorylation)

#####
'''
c_scan={}

k2=[20,50,100,150,200,300]
ap=[2,5,8,11,14]
for i in ap:
	c_scan[i]=[]

for i in np.linspace(1,10,30):
	kina.set("viKinA",i)
	T,Pa=kina.simulate(tmax=20)
	kina.display(["Spo0A_p"],save=True,show=False,fname="vkina=%f"%i)
	a_scan.append(Pa)
	print i
for k in ap:
	kinc.set("kap",k)# kd2
	print("k=%d,\n"%k)
	for i in np.linspace(1,10,30):
		kinc.set("viKinC",i)
		T,Pc=kinc.simulate(tmax=20)
		c_scan[k].append(Pc)
		print(i)
ave_a=[]
ave_c={}
ran_a=[]
ran_c={}
for i in a_scan:
	j=i[-300:]
	ave_a.append(np.mean(j,0))
	ran_a.append(np.max(j,0)-np.mean(j,0))
for k in c_scan.keys():
	ave_c[k]=[]
	ran_c[k]=[]
	for i in c_scan[k]:
		j=i[-300:]
		ave_c[k].append(np.mean(j,0))
		ran_c[k].append(np.max(j,0)-np.mean(j,0))
ai=kina.components.index("Spo0A_p")
ci=kinc.components.index("Spo0A_p")
path="3_3_2016/"
	
l=np.linspace(1,10,30)
plt.clf()
yy=np.array(ave_a)[:,ai]
plt.plot(l,yy,linewidth=2,label="KinA")
for i in ap:
	yy=np.array(ave_c[i])[:,ci]
	plt.plot(l,yy,linewidth=1.5,label="kap=%d"%i)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.xlabel("v_kinase")
plt.ylabel("Spo0A_p")
plt.title("Mean_of_0a_p_vs_kinase_at_different_kap")
plt.savefig(path+"Mean_of_0a_p_vs_kinase_at_different_kap.png")
plt.clf()


yy=np.array(ran_a)[:,ai]
plt.plot(l,yy,linewidth=2,label="KinA")
for i in ap:
	yy=np.array(ran_c[i])[:,ci]
	plt.plot(l,yy,linewidth=1.5,label="kap=%d"%i)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.xlabel("v_kinase")
plt.ylabel("Spo0A_p")
plt.title("Range_of_0a_p_vs_kinase_at_different_kap")
plt.savefig(path+"range_of_0a_p_vs_kinase_at_different_kap.png")
plt.clf()
'''
'''
for i in np.linspace(1,30,30):
	kina.set("viKinA",i)
	T,Pa=kina.simulate(tmax=20)
	kina.display(["ss","ps"],save=True,show=False,fname="vkina=%f"%i)
	a_scan.append(Pa)
	print i
'''
for i in np.linspace(11,20,10):
	kinc.set("viKinC",i)
	T,Pc=kinc.simulate(tmax=40)
	kinc.display(["ss","ps","Spo0A_p"],save=True,show=False,fname="vkinc=%f"%i)
	c_scan.append(Pc)
	print i
ave_a=[]
ave_c=[]
ran_a=[]
ran_c=[]
for i in a_scan:
	j=i[-300:]
	ave_a.append(np.mean(j,0))
	ran_a.append(np.max(j,0)-np.mean(j,0))
for i in c_scan:
	j=i[-300:]
	ave_c.append(np.mean(j,0))
	ran_c.append(np.max(j,0)-np.mean(j,0))

ai1=kina.components.index("ss")
ci1=kinc.components.index("ss")
ai2=kina.components.index("ps")
ci2=kinc.components.index("ps")
path=""
	
l=np.linspace(1,30,30)
'''
plt.clf()
yy=np.array(ave_a)[:,ai1]
plt.plot(l,yy,linewidth=2,label="P1")
yy=np.array(ave_a)[:,ai2]
plt.plot(l,yy,linewidth=2,label="P2")

plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.xlabel("v_kinase")
plt.ylabel("C")
plt.title("KinA_vs_P1_P2")
plt.savefig(path+"KinA_vs_P1_P2.png")
plt.clf()
l=np.linspace(1,10,30)


'''
plt.clf()
yy=np.array(ave_c)[:,ai1]
plt.plot(l,yy,linewidth=2,label="P1")
yy=np.array(ave_c)[:,ai2]
plt.plot(l,yy,linewidth=2,label="P2")

plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.xlabel("v_kinase")
plt.ylabel("C")
plt.title("KinC_vs_P1_P2")
plt.savefig(path+"KinC_vs_P1_P2.png")
plt.clf()


