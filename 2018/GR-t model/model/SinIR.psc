# Events


# Reactions

# DNA binding/unbinding
gsini:
	gsini0+Spo0A_p_d > gsini1
	kgsini*gsini0*Spo0A_p_d

dgsini:
 	gsini1 > gsini0+Spo0A_p_d
 	dgsini*gsini1

glsrr:
	gslrr0+SinR_t > gslrr1
	kgslrr*SinR_t*gslrr0
dgslrr:
	gslrr1 > gslrr0+SinR_t
	dgslrr*gslrr1

 	
# Transcription
sini:
	$pool > sini	
	gsini0*vsini0+gsini1*vsini1
degsini:
	sini > $pool
	sini*rnadeg
sinr:
	$pool > sinr
	vsinr*gsinr+k*(gsini0*vsini0+gsini1*vsini1)
degsinr:
	sinr > $pool
	sinr*rnadeg
slrr:
	$pool > slrr
	gslrr0*vslrr0+gslrr1*vslrr1
degslrr:
	slrr > $pool
	slrr*rnadeg
	
# Translation

SinI:
	$pool > SinI
	sini*trsini

SinR:
	$pool > SinR_d
	sinr*trsinr
SlrR:	
	$pool > SlrR_d
	slrr*trslrr


# Post_Translation

I_dimer:
	{2.0}SinI > SinI_d
	kd2*SinI*SinI
I_undimer:
	SinI_d > {2.0}SinI
	kud2*SinI_d
R_tr:
	{2.0}SinR_d > SinR_t
	kd1*SinR_d*SinR_d
R_untr:
	SinR_t > {2.0}SinR_d
	kud1*SinR_t

I_R:
	SinI_d+SinR_d >{2.0} SinI_SinR
	kb1*SinI_d*SinR_d
l_R:
	SinR_d+SlrR_d > SinR_SlrR_t
	kb2*SlrR_d*SinR_d

# Degradation


dSlrR:
	SlrR_d	>$pool
	kdeg*SlrR_d	 


# Parameters

rnadeg=8.3                                                                                                       
trsini=360
trsinr=180
trslrr=180
kdeg=0.42

kgsini=0.6
kgslrr=0.6
dgsini=72
dgslrr=36


kb1=0.32
kb2=0.32
kd1=0.32
kd2=0.32
kud1=1296
kud2=360


k=0
vsini0=0
vsini1=400
vsinr=400
vslrr0=500
vslrr1=0

Spo0A_p_d=0

# Initiation
gsini0=1
gsini1=0
gslrr0=1
gslrr1=0
gsinr=1


SinI=0
SinI_d=0
SinR_d=900
SlrR_d=0

SinR_t=0
SinI_SinR=0
SinR_SlrR_t=0




sini=0
sinr=0
slrr=0





