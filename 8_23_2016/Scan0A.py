import tools
from DS_solver import bioDS
import numpy as np
import matplotlib.pyplot as plt
test=bioDS(path='SinIR/')
test.load()

cc=tools.scan_range(test,parameter='Spo0A_p',exp='Ptap',space=np.linspace(0,4,10),save=False,savelog=False,show=False,time=60,fname='normal_pos_2.pdf')
test.set('trr',0.15)

dd=tools.scan_range(test,parameter='Spo0A_p',exp='Ptap',space=np.linspace(0,4,10),save=False,savelog=False,show=False,time=60,fname='trans_pos_2.pdf')


test=bioDS(path='SinIR2/')
test.load()

ee=tools.scan_range(test,parameter='Spo0A_p',exp='Ptap',space=np.linspace(0,4,10),save=False,savelog=False,show=False,time=60,fname='trans_pos_2.pdf')



plt.plot(np.linspace(0,4,10),cc[0],"b--",linewidth=0.5)
plt.plot(np.linspace(0,4,10),cc[1],"b--",linewidth=0.5)
plt.plot(np.linspace(0,4,10),cc[2],label="Normal_Pos",linewidth=1.0)
plt.fill_between(np.linspace(0,4,10),cc[0],cc[1],alpha=0.1)

plt.plot(np.linspace(0,4,10),dd[0],"b--",linewidth=0.5)
plt.plot(np.linspace(0,4,10),dd[1],"b--",linewidth=0.5)
plt.plot(np.linspace(0,4,10),dd[2],label="trans_Pos",linewidth=1.0)
plt.fill_between(np.linspace(0,4,10),dd[0],dd[1],alpha=0.1)


plt.plot(np.linspace(0,4,10),ee[0],"b--",linewidth=0.5)
plt.plot(np.linspace(0,4,10),ee[1],"b--",linewidth=0.5)
plt.plot(np.linspace(0,4,10),ee[2],label="Double",linewidth=1.0)
plt.fill_between(np.linspace(0,4,10),ee[0],ee[1],alpha=0.1)

plt.legend(bbox_to_anchor=(0.05, 1))

plt.xlabel("Spo0A_p")
plt.ylabel("pTapA")
plt.savefig("SinIR/scan_0A_co.pdf")
plt.show()
