import numpy as np 
from uncertainties import ufloat
from uncertainties import unumpy as unp 

# Road File
filename = "Brass 2"
f = np.loadtxt(f"{filename}.csv", delimiter = ",", skiprows = 1)

# Set Up Data Arrays
T = f[:,0]
R = f[:,1]

R0 = R[-1]
T0 = T[-1]

L0_Aluminium = ufloat(702, 1)  # mm
L0_Brass = ufloat(701, 1)    # mm

Delta_L = unp.uarray([R[i] - R0 for i in range(len(R)-1)], 0.01)
Delta_T = unp.uarray([T[i] - T0 for i in range(len(T)-1)], 0.05)


if(filename == "Aluminium"):
    L0 = L0_Aluminium
else:
    L0 = L0_Brass

# Calculate Alpha
alpha = [Delta_L[i] / (L0 * Delta_T[i]) for i in range(len(Delta_L))]

print("{:.3eP}".format(np.mean(alpha)))

#for i in range(len(alpha)):
#    print("{:.3eP}".format(alpha[i]))