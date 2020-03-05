import numpy as np 
import matplotlib.pyplot as plt 
from scipy.optimize import curve_fit
from uncertainties import ufloat
from uncertainties import unumpy as unp 

data = np.loadtxt("Data - Dielectric Constant.csv", delimiter=",", skiprows=1)

# Volume of Cyclohexane (mL), Voltage (mV)
Volume = unp.uarray(data[:,0],0.2)        # Volume of Cyclohexane (mL)
Voltage = unp.uarray(data[:,1],0.1)          # Voltage (mV)


# --- PLOT ---

def f(x, m, c):
    return [(m*i + c) for i in x]

xdata = np.array([i.n for i in Volume])
ydata = np.array([i.n for i in Voltage])

popt, pcov = curve_fit(f, xdata, ydata)
perr = np.sqrt(np.diag(pcov))

m = ufloat(popt[0], perr[0])
c = ufloat(popt[1], perr[1])

residuals = ydata - f(xdata, m.n, c.n)
ss_res = np.sum(residuals**2)
ss_tot = np.sum((ydata-np.mean(ydata))**2)
r_squared = 1 - (ss_res / ss_tot)

xval = np.linspace(min(xdata), max(xdata), 100)
yval = f(xval, m.n, c.n)


m_text = "{:.2uP}".format(m)
c_text = "{:.3uP}".format(c)
r_squared_text = "{:.4f}".format(r_squared)

bbox_props = dict(boxstyle="square, pad=0.4", fc="white", ec="black")

plt.plot(xdata, ydata, "go")
plt.plot(xval, yval, "b-")
plt.xlim(0)
plt.ylim(0.93*min(yval))
plt.xlabel("Volume of Cyclohexane (mL)")
plt.ylabel("Voltage (mV)")
plt.title("Cyclohexane")
plt.annotate(f"y = mx + c\nm = {m_text}\nc = {c_text}\n\n$R^2$ = {r_squared_text}", xy=(0.1, 0.65), xycoords="axes fraction", bbox=bbox_props)
plt.show()

# --- PLOT ENDS ---

# --- Further Calculations ----

V_0 = 20                # Voltage due to capacitance of lead (mV)
V_air = Voltage[0]      # Voltage due to capacitance of air (mV)
M = 84.16               # Molecular Mass of Cyclohexane (g/mol)
Rho = 0.779             # Density of Cyclohexane (g/cc)
NA = 6.022E+23          # Avogadro's Number

V_liq = 90*m + c        # Voltage due to capacitance of liquid when full [at 90 mL]
Dielectric_Constant = (V_liq - V_0) / (V_air - V_0)
NB = (NA * Rho / M) * 1E6   # Number of molecules per unit volume (per m^3)

# Electronic Polarizability (in nm^3)
Alpha = ((3 * (Dielectric_Constant - 1) / (Dielectric_Constant + 2)) / NB) * 1E27   

# --- Printing Values ---

print("Dielectric Constant \u03B5 = {:.2uP}".format(Dielectric_Constant))
print("Electronic Polarizability \u03B1 = {:.2uP} nm^3".format(Alpha))