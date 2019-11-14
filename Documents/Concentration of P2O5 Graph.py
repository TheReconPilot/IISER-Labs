import matplotlib.pyplot as plt 
from scipy.optimize import curve_fit
import numpy as np

x = np.array([0, 0.4, 0.8, 1.2, 1.6, 2.0])     # Concentration of P2O5 in ppm
y = np.array([0, 0.023, 0.054, 0.067, 0.099, 0.115])  # Absorbance

def f(x_param, m):
    return (m * x_param)

popt, pcov = curve_fit(f, x, y)
x1 = np.linspace(0, 2.0, 100)
y1 = f(x1, popt[0])


residuals = y- f(x, popt[0])
ss_res = np.sum(residuals**2)

ss_tot = np.sum((y-np.mean(y))**2)
r_squared = 1 - (ss_res / ss_tot)


print(popt)
print(r_squared)

plt.plot(x, y, "o", x1, y1, "g-")
plt.xlabel(r"Concentration of $\rm P_2O_5$")
plt.ylabel("Absorbance")
plt.text(0.23, 0.10, f"y = 0.0592x\n" + r"$\rm R^2 = 0.9905$", bbox=dict(facecolor = "none", edgecolor='navy'))
plt.savefig("PrajnaGraph.png")
