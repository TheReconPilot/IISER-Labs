import numpy as np
from uncertainties import ufloat
from uncertainties import unumpy as unp
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt


# Function to display individual elements of list with errors with a given number of decimals
def display(dlist, decimals = 3):
    for i in dlist:
        format_string = f"{{:.{decimals}eP}}"
        print(f"{format_string}".format(i))
    print()

set_name = "Set 1"
data = np.loadtxt(f"Export Data {set_name}.csv", delimiter = ",", skiprows = 1)

V = unp.uarray(data[:,0], 10)       # Voltage (in volt)
I = unp.uarray(data[:,1], 0.1)      # Current (in A)
d_r = unp.uarray(data[:,2], 0.1)    # Left Reading (in cm)
d_l = unp.uarray(data[:,3], 0.1)    # Right Reading (in cm)

d = (d_r - d_l) / 100               # Diameter (in m)
d2 = [x**2 for x in d]

e_by_m = [(7.576E+6 * V[i]) / (I[i]**2 * d[i]**2) for i in range(len(V))]

# Graph

xdata = [i.n for i in V]
ydata = [i.n for i in d2]

def f(x, m):
    return m*x

popt, pcov = curve_fit(f, xdata, ydata)

## Calcualting r_squared

residuals = ydata - f(xdata, popt)
ss_res = np.sum(residuals**2)
ss_tot = np.sum((ydata - np.mean(ydata))**2)
r_squared = 1 - (ss_res / ss_tot)

I_0 = I[0].n
slope = ufloat(popt[0], np.sqrt(np.diag(pcov)))
e_by_m_graph = 7.576E+6 / (slope * I_0)

## Plotting

xval = np.linspace(xdata[0], xdata[-1], 100)
yval = f(xval, popt[0])


print("R^2 =",r_squared)

plt.plot(xdata, ydata, ".")
plt.plot(xval, yval, "-")
plt.title(f"I = {I_0} A")
plt.xlabel("Accelerating Voltage (V)")
plt.ylabel(r"Square of Diameter ($m^2$)")
plt.show()


# Printing Stuff

print(f"File: Export Data {set_name}.csv")

print("--- Diameter d (m) ---")
display(d)

print("--- d^2 ---")
display(d2)

print("--- e/m ---")
display(e_by_m)

e_by_m_avg = np.mean(e_by_m)
print(e_by_m_avg)
e_by_m_lit_val = 1.758820E+11

print("Average: {:.3eP}".format(np.mean(e_by_m)))
print("Error from literature value = {:.2f}%".format((abs(e_by_m_avg.n - e_by_m_lit_val) / e_by_m_lit_val)*100))

print()

print("--- e/m from graph ---")
print("{:.3eP}".format(e_by_m_graph))
print("Error from literature value = {:.2f}%".format((abs(e_by_m_graph.n - e_by_m_lit_val) / e_by_m_lit_val)*100))

