import numpy as np 
from uncertainties import unumpy as unp 
from uncertainties import ufloat 

filename = "Slit"
f = np.loadtxt(f"{filename}.csv", delimiter = ",", skiprows = 1)

# D measured with normal ruler
D = unp.uarray(f[:,0], 1)             # Distance from slit to screen (cm)

m = f[:,1]                            # Order of dark fringe

# Inner and Outer distances between borders of dark fringes
# measured with Vernier Callipers
Outer = unp.uarray(f[:,2], 0.1)     # Distance between outer lines (cm)
Inner = unp.uarray(f[:,3], 0.1)     # Distance between inner lines (cm)

given_lambda = 650      # nm
given_slit_b = 0.2      # mm

xm = (Inner + Outer)/2

if (filename == "Wire"):        # Calculate Wire Thickness b
    wire_b = (2*m*given_lambda*1e-9*D*1e3)/xm       # mm
    object = wire_b
else:                           # Calculate Laser Wavelength Lambda
    calculated_lambda = (given_slit_b*1e-3*xm*1e9)/(2*D*m)  # nm
    object = calculated_lambda  

for i in range(len(object)):    # Print all values
    print("{:.2uP}".format(object[i]))

print("Average = {:.2uP}".format(np.mean(object)))