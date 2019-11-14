import numpy as np 
from uncertainties import ufloat
from uncertainties import unumpy as unp 

file = np.loadtxt("Data.csv", delimiter = ",", skiprows=1, usecols=(0,1))

alpha = 5.21e-3
beta = 7.2e-7
TG = 800    # K

n = len(file)

V = [ufloat(file[i,0],0.1) for i in range(n)]       # V
I = [ufloat(file[i,1],0.1) for i in range(n)]       # mA

R = [(V[i]/I[i])*1000 for i in range(n)]   # ohm
P = [(V[i]*I[i])/1000 for i in range(n)]   # W

R0 = R[7] / (1 + (alpha*TG) + (beta*TG*TG))

T = [(-1*alpha + unp.sqrt(alpha**2 - (4 * beta * (1 - (R[i]/R0)))))/(2*beta) for i in range(n)]

T4 = [T[i]**4 for i in range(n)]
