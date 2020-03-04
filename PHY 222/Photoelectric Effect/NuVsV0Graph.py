import numpy as np 
import matplotlib.pyplot as plt 
from scipy.optimize import curve_fit
from uncertainties import ufloat

data = np.loadtxt("StoppingPotentialData.csv", delimiter=",", skiprows=1)

wavelength = data[:,0]
V0 = data[:,1]

c = 299792458   # m/s
nu = [c/(i*1E-9) for i in wavelength]

def f(x, m, c):
    return [(m*i + c) for i in x]

V0 = -1*V0
xdata = nu 
ydata = V0 


popt, pcov = curve_fit(f, xdata, ydata)
residuals = ydata- f(xdata, popt[0], popt[1])
ss_res = np.sum(residuals**2)
ss_tot = np.sum((ydata-np.mean(ydata))**2)
r_squared = 1 - (ss_res / ss_tot)

perr = np.sqrt(np.diag(pcov))

xval = np.linspace(min(nu), max(nu), 100)
yval = f(xval, popt[0], popt[1])

xext = np.linspace(0, min(nu))
yext = f(xext, popt[0], popt[1])

m = ufloat(popt[0], perr[0])
m_text = "{:.3eP}".format(m)

c = ufloat(popt[1], perr[1])
c_text = "{:.2uP}".format(c)

r_squared_text = "{:.4f}".format(r_squared)


h = m * 1.602E-19
h_text = "{:.3eP}".format(h)

print(m_text)
print(c_text)
print(r_squared_text)

bbox_props = dict(boxstyle="square, pad=0.4", ec="black", fc="white")

plt.plot(nu, V0, "o")
plt.plot(xval, yval, "g-")
plt.plot(xext, yext, "r:")
plt.xlabel(r"$\nu$ (Hz)")
plt.ylabel("$V_0$ (V)")
plt.xlim(0)
plt.annotate(f"y = mx + c\nm = {m_text}\nc = {c_text}\n$R^2$ = {r_squared_text}", xy=(0.1, 0.75), xycoords="axes fraction", bbox=bbox_props)
plt.annotate(f"h = {h_text} Js", xy=(0.1, 0.65), xycoords="axes fraction", bbox=bbox_props)
plt.title("Stopping Potential vs Frequency")
plt.show()