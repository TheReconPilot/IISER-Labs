import numpy as np 
import matplotlib.pyplot as plt 
from uncertainties import unumpy as unp 
from uncertainties import ufloat
from scipy.optimize import curve_fit


def display(plist, decimals, format_type = "eP"):
    # format_string = f"{{:.{decimals}{format_type}P}}"
    
    # Target:
    # {:.3eP}       in format_string
    format_string = (u"%." + str(decimals) + format_type) % tuple(plist)
    for i in range(len(plist)):
        print(f"{format_string}".format(plist[i]))

# Load Data
# Mass (g), Relative Order (n), Left [cm], Right [cm], Up [cm], Down [cm]
data = np.loadtxt("Data - Cornu's Method.csv", delimiter = ",", skiprows = 1)

mass = data[:, 0]
order = data[:, 1]
left = data[:, 2]
right = data[:, 3]
up = data[:, 4]
down = data[:, 5]

down = unp.uarray(down, 0.01)
display(down, 2, format_type="s")
