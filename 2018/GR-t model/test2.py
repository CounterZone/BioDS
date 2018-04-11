import stochpy
model=stochpy.CellDivision()
model.Model(r"C:\Users\czczc\Documents\GitHub\BioDS\2018\GR-t model\model\SinIR.psc")
gr=1
model.SetDelayParameters({'SlrR':('fixed',0.006),'SinI':('fixed',0.006),'SinR':('fixed',0.006)})
model.SetInitialVolume(1)
model.SetGrowthFunction(0.5,"exponential")
model.SetVolumeDistributions(Phi= ('beta',2,2),K=('beta',5,5),Phi_beta_mean=2)
model.DoCellDivisionStochSim(end=15, trajectories=1)
model.PlotSpeciesTimeSeries(species2plot=["SinR","SinR_SlrR",'TapA'],xlabel="Time (h)",title="",linestyle="dashed",linewidth=1)
stochpy.plt.savefig(r"C:\Users\czczc\Documents\GitHub\BioDS\2018\GR-t model\myfigure.pdf")