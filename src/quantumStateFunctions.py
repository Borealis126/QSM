from qutip import tensor,fock
from math import floor
def qutipState(stateList,dim):
    tensorList=[fock(dim,i) for i in stateList] 
    return tensor(tensorList)
def stateFromHeader(header):
    return [int(i) for i in header[1:-1].split("-")]
def baseRepresentation(num,base,places):
    numBaseList=[0]*places
    for i in range(places):
        nthPlace=base**(places-i-1)
        numBaseList[i]=floor(num/nthPlace)
        num=num-nthPlace*numBaseList[i]
    return numBaseList
def H_Header(stateList):#
    return "["+'-'.join([str(i) for i in stateList])+"]"