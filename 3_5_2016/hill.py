from DS_solver import bioDS
import numpy as np
import matplotlib.pyplot as plt
import tools
hill=bioDS(path="hill/")
hill.parameters["Spo0A_p"]=0
hill.parameters["kdeg"]=0.7
hill.add(parameters="../s_parameter",reactions="../s_reaction")
atap=tools.scan_range(hill,parameter='Spo0A_p',exp='ptapa',space=np.linspace(0,5,60),save=False,savelog=False,show=False,time=15,period=0.2)
aspo=tools.scan_range(hill,parameter='Spo0A_p',exp='pspoIIg',space=np.linspace(0,5,60),save=False,savelog=False,show=False,time=15,period=0.2)
plt.plot(np.linspace(0,5,60),atap[2],label="tapA")
plt.plot(np.linspace(0,5,60),aspo[2],label="spoIIg")
v_line=[0.4,0.8,2.3]
ye=list(plt.axis())[-2:]
for i in v_line:
	te=np.ones(2)*i
	plt.plot(te,ye,'k--')
plt.xlabel("Spo0A_p")
plt.ylabel("Reporter")
plt.legend(bbox_to_anchor=(0.95, 0.95))
plt.savefig("hill/hill.pdf")
plt.show()
