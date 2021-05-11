import numpy as np

GHz=6.626e-25
hbarConst=6.62607e-34/(2*np.pi)
eConst=1.60217e-19
Phi_0Const=hbarConst*np.pi/eConst
Joules_To_Hz=1.50919e33
Joules_To_GHz=Joules_To_Hz/1e9

GHzToOmega=1e9*2*np.pi
omegaToGHz=1/GHzToOmega

lengthUnits="um"
traceBuffer=0.0001