import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

filename = "Ebonite.csv"

f = np.loadtxt(filename, skiprows = 1, delimiter = ",")

n = len(f)

time = f[:,0]
temp = f[:,1]
temp = [i + 273.15 for i in temp]   # K
#temp_error = [0.25 for i in range(len(temp))]

# plt.plot(time, temp, "o")
# plt.show()

def exponential_decay(x, a, b, c):
    return a + b * np.exp(-c*x)

popt, pcov = curve_fit(exponential_decay, time, temp, p0=[60, 20, 0.3])

a = popt[0]
b = popt[1]
c = popt[2]

residuals = temp - exponential_decay(time, a, b, c)
ss_res = np.sum(residuals**2)
ss_tot = np.sum((temp-np.mean(temp))**2)
r_squared = 1 - (ss_res / ss_tot)


print(popt)
print(r_squared)

def slope(cparam, aparam, T):
    return cparam * (aparam - T)

T1 = 67.5 + 273.15 

def t_from_T(T, A, B, C):
    return np.log((T-a)/b) * (-1 / c)

t1 = t_from_T(T1, a, b, c)

m = slope(c, a, T1)
delta = 0.75
xslope = np.linspace(t1 - delta, t1 + delta, 100)
yslope = m * xslope + (T1-m*t1)


x = np.linspace(time[0], time[-1], 100)
y = exponential_decay(x, a, b, c)


plt.plot(time, temp, ".")
#plt.errorbar(time, temp, temp_error, fmt = "b.")
plt.plot(x, y, "g-")
plt.plot(xslope, yslope, "r-")
plt.plot(t1, T1, "o")
plt.xlabel("Time (min)")
plt.ylabel("Temperature (°C)")
print(m)
plt.text(2.5, 67.6, "Slope = -3.139")
plt.text(3, 71, r'$\rm T = a + b e^{-ct}$' + "\n\na = 56.985\nb = 20.228\nc = 0.298\n\n" + r'$R^2 = 0.9960$', 
        bbox=dict(facecolor = "none", edgecolor='navy'))
plt.text(1.7, 65.0, r'$\rmT_1 = $' + "\n" + r'$\rm67.5^{\circ}C$')
plt.title("Ebonite Disk")
plt.show()
#plt.savefig("Ebonite.png")
