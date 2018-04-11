# Stochastic Simulation of Spo0A~P network

# Reactions
# Synthesis of upstream genes

KinA:
    $pool> KinA
    2*viKinA

Spo0A:
    $pool> Spo0A
    2*viKinA

Spo0F:
    $pool> Spo0F
    2*viKinA

Spo0B:
    $pool> Spo0B
    2*viKinA

# Upstream reactions

KinA_auto_p:
	KinA> KinA_p
	kap*KinA
	
KinA_autod_p:
	KinA_p> KinA
	kadp*KinA
	
kina_0f:
	KinA_p + Spo0F >   KinA_p_Spo0F
	kb*KinA_p*Spo0F
s0f_kina:
	KinA_p_Spo0F   >   KinA_p + Spo0F
	k1*KinA_p_Spo0F
kina_0fp:
	KinA_p_Spo0F   >   KinA + Spo0F_p
	k2*KinA_p_Spo0F
s0fp_kina:
	KinA + Spo0F_p >   KinA_p_Spo0F
	kb*KinA*Spo0F_p
	
s0f_0b:
	Spo0F_p + Spo0B > Spo0F_p_Spo0B
	kb*Spo0F_p*Spo0B
s0b_0f:
	Spo0F_p_Spo0B   > Spo0F_p + Spo0B
	k3*Spo0F_p_Spo0B
s0f_0bp:
	Spo0F_p_Spo0B   >  Spo0F + Spo0B_p
	k4*Spo0F_p_Spo0B
s0bp_0f:
	Spo0F + Spo0B_p >  Spo0F_p_Spo0B
	kb*Spo0F*Spo0B_p

s0b_0a:
	Spo0B_p + Spo0A > Spo0B_p_Spo0A
	kb*Spo0B_p*Spo0A
s0a_0b:
	Spo0B_p_Spo0A   > Spo0B_p + Spo0A
	k5*Spo0B_p_Spo0A
s0b_0ap:
	Spo0B_p_Spo0A   > Spo0A_p + Spo0B
	k6*Spo0B_p_Spo0A
s0ap_0b:
	Spo0A_p + Spo0B > Spo0B_p_Spo0A
	kb*Spo0B*Spo0A_p

	


# degradations




# Parameters
# UNIT: micromolar,hour

# Transcription

trep=2

viKinA=5.5
vg0=100
vgmax=1000
Kg=2
v0A0=1.4
v0Amax=14
K0A=0.15

v0F0=0.35
v0Fmax=7
K0F=0.2

# Post_Transcription

#Auto p/dp and binding rate

kap=8

kadp=2

kb=500


#Phosphorelay

k1=1000

k2=300

k3=500

k4=800

k5=200

k6=800

# repression

ki=80

kubr=100

kr=100

kube=100

ke=100

kdeg=0.5

# initiation

KinA=1
Spo0A=1
Spo0F=1
Spo0B=1
Spo0F_p=1
Spo0F_p_Spo0B=1
Spo0B_p=1
Spo0B_p_Spo0A=1
Spo0A_p=1
KinA_p=1
KinA_p_Spo0F=1
