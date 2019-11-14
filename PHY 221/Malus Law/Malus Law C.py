import numpy as np 
import matplotlib.pyplot as plt 
from scipy.optimize import curve_fit

f = np.loadtxt("Data.csv", delimiter = ",", skiprows = 1)

theta = np.deg2rad(f[:,0])

I_Clockwise = f[:, 1]   # microamperes
I_AntiClockwise = f[:, 2]   # microamperes

def cosine(theta, I0, delta):
    return I0 * np.cos(theta + delta)**2 

xdata = theta
ydata = I_Clockwise
f = cosine 

pinit = [100, np.pi]
popt, pcov = curve_fit(cosine, xdata, ydata, pinit)

I0 = popt[0]
delta = popt[1]

residuals = ydata - f(xdata, popt[0], popt[1])
ss_res = np.sum(residuals**2)
ss_tot = np.sum((ydata-np.mean(ydata))**2)
r_squared = 1 - (ss_res / ss_tot)

print(popt)
print(r_squared)

cos2td = np.power(np.cos(theta+delta),2)

yval = I0 * np.power(np.cos(theta+delta),2)

r_squared_text = "{:.3f}".format(r_squared)
I0_text = "{:.3f}".format(I0)
delta_text = "{:.3f}".format(delta)

text = [I0_text, delta_text, r_squared_text]
print(text)

bbox_props = dict(boxstyle = "square, pad=0.4", fc = "white", ec = "black")

plt.plot(theta, ydata, ".")
plt.plot(theta, yval)
plt.axis([-0.5, 6.5, -10, 125])
plt.xlabel(r'$\rm \theta\ (rad)$')
plt.ylabel(r'$\rm I\ (\mu A)$')
#plt.annotate("I = {} cos^2(theta+{})\nR^2 = {}".format(I0_text, delta_text, r_squared_text), xy = (0.1, 0.75), xycoords = "axes fraction", bbox = bbox_props)
plt.annotate(r'$\rm I = 102.951\ \cos^2 (\theta+3.946)$', 
             xy = (0.05, 0.90), xycoords = "axes fraction", bbox = bbox_props)              
plt.annotate(r'$\rm R^2 = 0.991$', 
             xy = (0.05, 0.80), xycoords = "axes fraction", bbox = bbox_props)
plt.title("Clockwise")
#plt.savefig("Clockwise.png")
plt.show()