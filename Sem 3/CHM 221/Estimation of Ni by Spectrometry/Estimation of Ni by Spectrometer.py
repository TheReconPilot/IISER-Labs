import matplotlib.pyplot as plt 
from scipy.optimize import curve_fit
import numpy as np

conc = [0, 0.0841, 0.06731, 0.03364]
absorbance = [0, 0.436, 0.353, 0.179]
unknown_abs = 0.276

def f(x, m):
    return x * m

xdata = conc
ydata = absorbance

popt, pcov = curve_fit(f, xdata, ydata)

residuals = ydata - f(xdata, popt)
ss_res = np.sum(residuals**2)
ss_tot = np.sum((ydata-np.mean(ydata))**2)
r_squared = 1 - (ss_res / ss_tot)

print(popt)
print(r_squared)


m = popt[0]
xval = np.linspace(min(xdata), max(xdata), 100)
yval = f(xval, m)

bbox_props = dict(boxstyle = "square, pad = 0.4", fc = "white", ec = "black")

unknown_conc = unknown_abs / m
print(unknown_conc)

plt.plot(xdata, ydata, ".", markersize = 8)     # Plot Data Points
plt.plot(xval, yval, "g-")      # Plot the Straight Line

# Plotting the Unknown
plt.plot(unknown_conc, unknown_abs, "or")

horizontal_xval = np.linspace(0, unknown_conc, 100)
horizontal_yval = np.repeat(unknown_abs, 100)

vertical_xval = np.repeat(unknown_conc, 100)
vertical_yval = np.linspace(0, unknown_abs, 100)

plt.plot(horizontal_xval, horizontal_yval, "--r")
plt.plot(vertical_xval, vertical_yval, "--r")

# Axes and Labels
plt.axis([0, 0.1, 0, 0.5])
plt.xlabel("Concentration")
plt.ylabel("Absorbance")

# Annotate Stuff
plt.annotate("y = 5.2178 x", xy = (0.05, 0.85), xycoords = "axes fraction", bbox = bbox_props)
plt.annotate(r"$\rm R^2 = 0.999$", xy = (0.05, 0.75), xycoords = "axes fraction", bbox = bbox_props)

plt.annotate("Unknown\nA = 0.276\nC = 0.0529 M", xy = (unknown_conc + 0.001, unknown_abs), 
             xycoords = "data", xytext = (0.065, 0.20), textcoords = "data", 
             arrowprops = dict(arrowstyle = "-|>", connectionstyle = "arc3, rad = 0.2"))

plt.show()
#plt.savefig("Graph.png")