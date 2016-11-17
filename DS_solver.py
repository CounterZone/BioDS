import numpy as np
from scipy.integrate import ode,odeint 
import config
import matplotlib.pyplot as plt

class bioDS(object):
	def __init__(self,components=[],parameters={},equations={},reactions={},initials={},path=""):
		self.components=components
		self.parameters=parameters
		self.equations=equations
		self.reactions=reactions
		self.initials=initials
                self.trajectory=[[],[]]
                self.path=path
	def load(self,f_reactions="reactions.config",f_parameters="parameters.config",f_initials="initials.config"):
		self.components,self.equations,self.reactions=config.import_equations(self.path+f_reactions,{},{})
		self.parameters=config.import_parameters(self.path+f_parameters,{})
		self.initials=config.import_initials(self.components,self.path+f_initials,{})
	def add(self,reactions='',initials='',parameters=''):
		iaa={}
		for i in self.components:
			iaa[i]=self.initials[self.components.index(i)]
		if not reactions == '':
			self.components,self.equations,self.reactions=config.import_equations(self.path+reactions,equations=self.equations,reactions=self.reactions)
		if not parameters=='':
			self.parameters=config.import_parameters(self.path+parameters,parameters=self.parameters)
		self.initials=config.import_initials(self.components,self.path+initials,initials=iaa)
	def derivative(self,t,x):
		y=np.zeros(len(x))
		values={}
		for i in range(0,len(x)):
			values[self.components[i]]=x[i]
		values["t"]=t
		values.update(self.parameters)
		for i in range(0,len(y)):
			for j in self.equations[self.components[i]].keys():
				y[i]=y[i]+eval(self.reactions[j],values)*self.equations[self.components[i]][j]
		return y
        def simulate(self,tmin=0,tmax=40,tsteps=1000,option='lsoda'):
                t=np.linspace(tmin,tmax,tsteps)
                solver=ode(self.derivative)
                solver.set_initial_value(self.initials,tmin)
                solver.set_integrator(option)
                yy=[self.initials]
                for tt in t[1:]:
                    yy.append(solver.integrate(tt))
		if len(self.trajectory[1])==0:
			self.trajectory=(t,yy)		
		else:
                	self.trajectory=(np.hstack([self.trajectory[0],t]),np.vstack([self.trajectory[1],yy]))
                return t,yy
	def clear(self):
		self.trajectory=[[],[]]
	def set(self,parameter,value):
		if parameter in self.parameters.keys():
			self.parameters[parameter]=value
		elif parameter in self.components:
			self.initials[self.components.index(parameter)]=value
		else:
			print("Doesn't exist.\n")
	def update(self):
		self.initials=self.trajectory[1][-1]
	def getTrajectory(self,component):
		return np.array(self.trajectory[1])[:,self.components.index(component)]
        def display(self,exps,fname='figure',save=False,v_line=[],xlabel='t',ylabel='c',show=True):
		plt.clf()
                for i in exps:
		    yy=self.getTrajectory(i)
		    plt.plot(self.trajectory[0],yy,linewidth=2,label=i)
                plt.legend()
                ye=list(plt.axis())[-2:]
                for i in v_line:
		    te=np.ones(2)*i
                    plt.plot(te,ye,'k--')
                plt.title(fname)
		plt.xlabel(xlabel)
		plt.ylabel(ylabel)
                if save:
			plt.savefig(self.path+fname+".png")
                if show:
			plt.show()
		plt.clf()
	



		
