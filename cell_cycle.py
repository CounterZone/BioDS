from DS_solver import *
import numpy.random as rd
class cell(bioDS):
	def __init__(self,components=[],parameters={},equations={},reactions={},initials={},path=""):
		super(cell,self).__init__(components=components,parameters=parameters,equations=equations,reactions=reactions,initials=initials,path=path)
	def division(self,c0):
		self.update()
		for i in range(self.initials.shape[0]):
			t=self.initials[i]
			pp=c0*rd.binomial(int(t/c0),0.5)
			while pp<0 or pp>t:
				pp=c0*rd.binomial(int(t/c0),0.5)
			self.initials[i]=2*pp
	
	def parameterTurn(self,sigma):
		self.load()
		self.update()
		for i in self.parameters.keys():
			t=self.parameters[i]
			if t==0:
				continue
			pp=rd.normal(t,sigma*np.abs(t))
			while pp<0 or pp>2*t:
				pp=rd.normal(t,sigma*np.abs(t))
			self.parameters[i]=pp
