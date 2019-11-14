import numpy as np 
from uncertainties import ufloat
from uncertainties import unumpy as unp
from scipy.optimize import curve_fit

f = np.loadtxt("Stefan's Law.csv", delimiter = ",", skiprows=1)

alpha = 5.21e-3
beta = 7.2e-7
TG = 800    # K

n = len(f)

V = unp.uarray(f[:,0], 0.5)     # V
I = unp.uarray(f[:,1], 0.05)    # A
Ta = unp.uarray(f[:,2], 0.05)

R = [(V[i]/I[i]) for i in range(n)]   # ohm
P = [(V[i]*I[i]) for i in range(n)]   # W

R0 = R[4] / (1 + (alpha*TG) + (beta*TG*TG))

T = [(-1*alpha + unp.sqrt(alpha**2 - (4 * beta * (1 - (R[i]/R0)))))/(2*beta) for i in range(n)]

T4 = [T[i]**4 for i in range(n)]

T4_Ta4 = [T4[i] - Ta[i]**4 for i in range(n)]

obj = T

for i in range(len(obj)):
    print("{:.3eP}".format(obj[i]))


"""
def linear(x, p):
    return p * x

popt1, pcov1 = curve_fit(linear, [T4[i].n for i in range(n)], [P[i].n for i in range(n)])
popt2, pcov2 = curve_fit(linear, [T4_Ta4[i].n for i in range(n)], [P[i].n for i in range(n)])

# Error between slope of [P vs T^4] and [P vs (T^4-Ta^4)]
error = (popt2-popt1)/popt2 * 100
print(popt1)
print(popt2)
print(error)"""