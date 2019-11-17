import numpy as np 
import matplotlib.pyplot as plt 
from scipy.optimize import curve_fit
from uncertainties import ufloat

lambda_SL = 589*1E-9        # Sodium Lamp Wavelength
lambda_GL = 532*1E-9        # Green Laser Wavelength

filename = "Sodium Lamp"

# Extract Data
data_file = np.loadtxt(f"{filename} Data.csv", delimiter = ",", skiprows = 1)

# Load the data into variables
order = data_file[:, 0]
up = data_file[:, 1]
down = data_file[:, 2]
#left = data_file[:, 3]
#right = data_file[:, 4]

# Calculate diameters
D_ud = down - up
#D_lr = right - left
#D_avg = (D_ud + D_lr) / 2 

# The final array for D
D = D_ud

n = len(D)

x = []
y = []

# Calculate all possible combinations for relative order
for i in range(n):
    for j in range(i+1, n):
        y.append(D[i]**2 - D[j]**2)
        x.append(order[i] - order[j])


# Sort the x and y lists
x, y = (list(t) for t in zip(*sorted(zip(x, y))))

# --- START CURVE_FIT AND PLOTTING ---

def linear(x, p):
    return p*x

# Set variables for curve_fit
f = linear
xdata = x
ydata = y

popt, pcov = curve_fit(f, xdata, ydata)

# Calcualting r_squared
residuals = ydata - f(xdata, popt)
ss_res = np.sum(residuals**2)
ss_tot = np.sum((ydata - np.mean(ydata))**2)
r_squared = 1 - (ss_res / ss_tot)


# Setting variables for plot based on curve_fit parameters
p = popt[0]
xval = np.linspace(x[0], x[-1], 100)
yval = f(xval, p)

r_squared_text = "{:.4f}".format(r_squared)
p_text = "{:.4f}".format(p)

print(f"p = {p} = {p_text}")
print(f"R^2 = {r_squared} = {r_squared_text}")

# Standard Deviation Error in Fitted Parameter
parameter_err = np.sqrt(np.diag(pcov))
p_error = parameter_err[0]
p_error_text = "{:.4f}".format(p_error)
print(f"p_error = {p_error} = {p_error_text}")

p = ufloat(p, p_error)
R = p / (4 * lambda_SL * 1E4)

print("R = {:.3uP}".format(R))

R_text = "{:.3uP}".format(R)

# The Plots
plt.plot(x, y, ".")
plt.plot(xval, yval, "g-")

plt.xlabel("m")
plt.ylabel(r"$\sf D_{n+m}^2 - D_{n}^2\ (cm^2)$")
plt.title(f"{filename}")

bbox_props = dict(boxstyle = "square, pad = 0.4", fc = "white", ec = "black")

plt.annotate(f"y = px", xy = (0.1, 0.85), 
             xycoords = "axes fraction", bbox = bbox_props)
plt.annotate(r'$\sf p = ${}$\pm${}'.format(p_text, p_error_text), xy = (0.1, 0.75), 
             xycoords = "axes fraction", bbox = bbox_props)
plt.annotate(r'$\sf R^2 = ${}'.format(r_squared_text),
             xy = (0.1, 0.65), xycoords = "axes fraction", bbox = bbox_props)

plt.annotate("Radius of Curvature", xy = (0.6, 0.37), xycoords = "axes fraction")
plt.annotate(r'$\sf R = \dfrac{D_{n+m}^2-D_{n}^2}{4m\lambda} = \dfrac{p}{4\lambda}$', 
             xy = (0.6, 0.25), xycoords = "axes fraction", bbox = bbox_props)
plt.annotate(f"R = {R_text} m", xy = (0.6, 0.13), xycoords = "axes fraction", 
             bbox = bbox_props)

plt.show()
#plt.savefig(f"NR {filename} Graph.png") 
