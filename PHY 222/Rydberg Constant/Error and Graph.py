import numpy as np 
import matplotlib.pyplot as plt 
from uncertainties import unumpy as unp 
from uncertainties import ufloat 
from scipy.optimize import curve_fit

def display(plist, decimals, format_type="e"):
    format_string = f"{{:.{decimals}{format_type}P}}"
    for i in range(len(plist)):
        print(f"{format_string}".format(plist[i]))
    print()     # Empty Line for formatting aesthetics
    return

# Load data
# Colour - m - ni - Left Deg - Left Min - Right Deg - Right Min
data = np.loadtxt("Data - Rydberg Constant.csv", delimiter = ",", skiprows = 1, usecols = (1,2,3,4,5,6))

m = data[:,0]   # Order
ni = data[:,1]  # Initial Energy Level [nf = 2]
ld = data[:,2]  # Left Degree
lm = data[:,3]  # Left Minute
rd = data[:,4]  # Right Degree
rm = data[:,5]  # Right Minute

# Constants
g = 600     # Lines per mm
d = 0.001/g       # Distance between lines

theta = [((rd[i] + (rm[i]/60) - ld[i] - (lm[i]/60))/2) for i in range(len(ld))]
theta = unp.uarray(theta, 1/60)

# Calculating wavelength in m
lambda_m = [(d * unp.sin((np.pi * theta[i])/180) / m[i]) for i in range(len(m))]

lambda_nm = [i * 1E9 for i in lambda_m]

inv_lambda = [1/i for i in lambda_m]    # Inverse of Lambda
diff_1_by_4_and_ni_sq = [1/4 - 1/(i*i) for i in ni]

R = [inv_lambda[i]/diff_1_by_4_and_ni_sq[i] for i in range(len(inv_lambda))]
R_avg = np.mean(R)
R_litval = 1.09737E7
litval_err = (abs(R_litval - R_avg.n) / R_litval)*100
print("R")
display(R, 4)
print("Average = {:.4eP}".format(R_avg))
print("Error from Literature Value = {:.2f}%".format(litval_err))
# Getting Ready for Plotting

# Define linear fit with zero intercept
def f(x, m):
    return m*x

# Define curve fit variables
xdata = diff_1_by_4_and_ni_sq
ydata = [i.n for i in inv_lambda]

# Curve Fit
popt, pcov = curve_fit(f, xdata, ydata)

perr = np.sqrt(np.diag(pcov))   # Error in Parameter

# Calculating R^2
residuals = ydata- f(xdata, popt)
ss_res = np.sum(residuals**2)
ss_tot = np.sum((ydata-np.mean(ydata))**2)
r_squared = 1 - (ss_res / ss_tot)

# Defining plor variables
# xval and yval contain the line with obtained parameters
xval = np.linspace(min(xdata), max(xdata), 100)
yval = f(xval, popt[0])

m = ufloat(popt[0], perr)
m_text = "{:.4eP}".format(m)    # Define slope text with 4 decimals

r_squared_text = "{:.4f}".format(r_squared) # Define R^2 text

bbox_props = dict(boxstyle = "square, pad=0.4", fc="white", ec="black")

# Actual Plotting
plt.plot(xdata, ydata, "o")
plt.plot(xval, yval, "g-")
plt.xlabel(r'$\dfrac{1}{4} - \dfrac{1}{n_i^2}$')
plt.ylabel(r'$\dfrac{1}{\lambda} \quad [m^{-1}]$')
plt.annotate(f"y = {(m_text)} x", xy = (0.15, 0.85), xycoords = "axes fraction", bbox = bbox_props)
plt.annotate(r'$\rm R^2$ = {}'.format(r_squared_text), xy=(0.15, 0.75), xycoords = "axes fraction", bbox = bbox_props)
plt.subplots_adjust(bottom=0.16)
plt.show()
#plt.savefig("Graph - Rydberg Constant.png")