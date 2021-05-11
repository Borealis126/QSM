from scipy.interpolate import interp1d
from scipy.optimize import fsolve

import numpy as np
def S21TodB(val):
    return 20*np.log10(np.abs(val))
def calculateDressedFrequency(freq,Y11InterpFunc):
    Y11_Imag=[]
    for thisFreq in freq:
        Y11_Imag.append(np.imag(Y11InterpFunc(thisFreq)))
    Y11InterpFuncImag=interp1d(freq,Y11_Imag)#This function now maps xvals to imag(yVals)
    dressedFreq=fsolve(Y11InterpFuncImag,freq[int(len(freq)/2)])#Guess is just the middle frequency.
    return dressedFreq[0]