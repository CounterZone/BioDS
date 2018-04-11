import stochpy
model=stochpy.CellDivision()
model.Model(r"C:\Users\czczc\Documents\GitHub\BioDS\2018\GR-t model\model\SinIR.psc")
gr=1
model.SetDelayParameters({'SlrR':('fixed',0.02),'SinI':('fixed',0.02),'SinR':('fixed',0.02)})
model.SetInitialVolume(1.6)
model.SetGrowthFunction(2,"exponential")
model.SetVolumeDistributions(Phi= ('beta',2,2),K=('beta',5,5),Phi_beta_mean=3.2)
model.DoCellDivisionStochSim(end=1, trajectories=1)
model.PlotSpeciesTimeSeries(species2plot=["SinR_t",'SinR_SlrR_t'],xlabel="Time (h)",title="",linestyle="dashed",linewidth=1)
stochpy.plt.savefig(r"C:\Users\czczc\Documents\GitHub\BioDS\2018\GR-t model\myfigure2.pdf")