import numpy as np 
import matplotlib.pyplot as plt 
from scipy.optimize import curve_fit

# SST, pH, pCO2
data = np.loadtxt("pCO2 vs pH with SST.csv", delimiter = ",", skiprows = 1)

SST = data[:,0]
pH = data[:,1]
pCO2 = data[:,2]

def f(x, m):
    return m*x 


xdata = pH 
ydata = pCO2 

popt, pcov = curve_fit(f, xdata, ydata)

m = popt[0]
m_text = "{:.3f}".format(m)

xval = np.linspace(min(xdata), max(xdata), 100)
yval = f(xval, m)

bbox_props = dict(boxstyle = "square, pad=0.4", fc="white", ec="black")

plt.scatter(pH, pCO2, c=SST, cmap="magma")
plt.colorbar(label="Sea Surface Temperature ($^{\circ}C$)")
plt.plot(xval, yval, "b:")
plt.annotate(f"y = {m_text} x", xy = (0.1, 0.85), xycoords = "axes fraction", bbox = bbox_props)
plt.xlabel("pH")
plt.ylabel("pCO$_2$")
plt.title("pCO$_2$ vs pH")
plt.show()
#plt.savefig("pCO2 vs pH with SST Graph.png")