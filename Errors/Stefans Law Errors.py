from uncertainties import ufloat
from uncertainties import unumpy as unp 
import numpy as np 

f = np.loadtxt("Stefan's Law.csv", delimiter = ",", skiprows = 1, usecols = (0,1,5))

a = 5.21*(10^(-3))
b = 7.20*(10^(-7))

V = unp.uarray(f[:,0], 0.05)
I = unp.uarray(f[:,1], 0.005)

R = V / I
P = V*I

T = (-a + sqrt((a^2) - 4*b*(1-(R/1.27))))/(2*b)
T_4 = T^4

TA = unp.uarray(f[:,5],0.05)
TA_4 = TA^4

obj = V

for i in range(len(obj)):
    print("{:.5eP}".format(obj[i]))

