import numpy as np 
import matplotlib.pyplot as plt 
from scipy.optimize import curve_fit

# Load File
filename = "Brass 2"
f = np.loadtxt(f"{filename}.csv", delimiter = ",", skiprows = 1)

# Set Up Data Arrays
Tr = f[:,0]
R = f[:,1]

L = np.array([R[i] - R[-1] for i in range(len(R))])
T = np.array([Tr[i] - Tr[-1] for i in range(len(Tr))])

# Function for Curve Fit
def linear(x, m):
    return m*x

# Fitting the Curve
popt, pcov = curve_fit(linear, T, L)

m = popt[0]

residuals = L - linear(T, m)
ss_res = np.sum(residuals**2)

ss_tot = np.sum((L - np.mean(L))**2)
r_squared = 1 - (ss_res / ss_tot)


x = np.linspace(T[0]+3, T[-1], 100)
y = linear(x, m)


# Plotting 
r_squared_text = "{:.3f}".format(r_squared)
m_text = "{:.4f}".format(m)

bbox_props = dict(boxstyle = "square, pad=0.4", fc = "white", ec = "black")

plt.plot(T, L, ".")
plt.plot(x, y, "g-")
plt.xlabel(r'$\Delta\ T$')
plt.ylabel(r'$\Delta\ L$')
plt.title(filename)
plt.annotate("y = {} x\nR^2 = {}".format(m_text, r_squared_text), xy = (0.1, 0.75), xycoords = "axes fraction", bbox = bbox_props)
plt.savefig(f"{filename}.png")
# plt.show()

# Print Optimal Parameters and R^2
print(popt)
print(r_squared)