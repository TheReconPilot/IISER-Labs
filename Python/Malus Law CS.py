import numpy as np 
import matplotlib.pyplot as plt 
from scipy.optimize import curve_fit 

f = np.loadtxt("Data.csv", delimiter = ",", skiprows = 1)

theta = np.deg2rad(f[:,0])

I_Clockwise = f[:,1]        # microamperes
I_AntiClockwise = f[:,2]    # microamperes

def linear(theta, I0, delta):
    return (I0*(1+np.cos(2*(theta+delta))))/2

xdata = theta
ydata = I_Clockwise
f = linear

p0 = [100, np.pi]
popt, pcov = curve_fit(f, xdata, ydata, p0)

print(popt)

I0 = popt[0]
delta = popt[1]

residuals = ydata - f(xdata, popt[0], popt[1])
ss_res = np.sum(residuals**2)
ss_tot = np.sum((ydata-np.mean(ydata))**2)
r_squared = 1 - (ss_res / ss_tot)

print(r_squared)

cos2td = np.power(np.cos(theta+delta), 2)

r_squared_text = "{:.3f}".format(r_squared)
I0_text = "{:.3f}".format(I0)
delta_text = "{:.3f}".format(delta)

text = [I0_text, delta_text, r_squared_text]
print(text)

bbox_props = dict(boxstyle = "square, pad=0.4", fc = "white", ec = "black")

plt.plot(cos2td, I_Clockwise, ".")      # Data Plot
plt.plot(cos2td, I0*cos2td, "g-")             # Curve Fit Plot
plt.xlabel(r'$\rm \cos^2(\theta + \delta)$')
plt.ylabel(r'$\rm I\ (\mu A)$')
plt.title("Clockwise")
plt.annotate(r'$\rm I = 102.951\ \cos^2 (\theta + 3.946)$', 
             xy = (0.1, 0.85), xycoords = "axes fraction",
             bbox = bbox_props)
plt.annotate(r'$R^2 = 0.991$', xy = (0.1, 0.75),
             xycoords = "axes fraction", bbox = bbox_props)
#plt.show()
plt.savefig("Clockwise Straight.png")