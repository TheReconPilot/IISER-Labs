import numpy as np
from uncertainties import ufloat 
from uncertainties import unumpy as unp 
from scipy.optimize import curve_fit

# Display List function to conveniently print lists 
# with a given number of decimals in an uncertainties object
# and a specific format
def display(plist, decimals, format_type="e"):
    format_string = f"{{:.{decimals}{format_type}P}}"
    for i in range(len(plist)):
        print(f"{format_string}".format(plist[i]))
    print()     # Empty Line for formatting aesthetics
    return

# Load Data
# Droplet No., Fall Time, Rise Time, Voltage
data = np.loadtxt("Data - Dynamic Method.csv", delimiter=",", skiprows=1)

number_of_droplets = int(max(data[:,0]))

# Create array of required data
fall_time = []
rise_time = []
V = []

## Here, fall_time and rise_time are 2D arrays, while V is a 1D list 
## V has 0th entry in every list in the 2D array generated from data
for i in range(number_of_droplets):
    fall_time.append(unp.uarray([data[j,1] for j in range(len(data)) if data[j,0]==i+1], 0.1))
    rise_time.append(unp.uarray([data[j,2] for j in range(len(data)) if data[j,0]==i+1], 0.1))
    V.append(unp.uarray([data[j,3] for j in range(len(data)) if data[j,0]==i+1][0], 0.5))

# CONSTANTS
d = 0.005       # Distance between parallel plates, in m
L = 0.0005       # Distance between lines, in m
d_rho = 928     # Difference in density of oil and air, in kg/m^3
P = 0.76        # Atmospheric Pressure, in m of Hg
eta = 1.8432e-5 # Coefficient of viscosity of air, in kg / (m.s)
g = 9.78563     # Gravitational Acceleration in Pune, in m/s^2 (Data from Wolfram Alpha)
c = 6.17e-8     # Correction Factor, in m of Hg

# CALCULATED CONSTANTS
C = 4 * np.pi * d * g * d_rho / 3
D = (9 * eta) / (2 * g * d_rho)
sigma = c / (2 * P)

# Calculate Mean Fall and Rise times
tf = [np.mean(i) for i in fall_time]
tr = [np.mean(i) for i in rise_time]

# Mean Free Fall Velocity
vf = [L / tf[i] for i in range(len(tf))]

# Calculating Final Parameters
xi = [D * vf[i] for i in range(len(vf))]
r = [-sigma + unp.sqrt(sigma**2 + xi[i]) for i in range(len(xi))]
r3 = [r[i]**3 for i in range(len(r))]
T = [1 + (tf[i]/tr[i]) for i in range(len(tf))]
ne = [C * T[i] * r3[i] / V[i] for i in range(len(V))]


# Calculating GCD

min_ne = ne[0]
min_ne_index = 0
for i in range(len(ne)):
    if(ne[i] < min_ne):
        min_ne = ne[i]
        min_ne_index = i

new_ne = [i for i in ne]
new_ne.pop(min_ne_index)
# Now, new_ne has minimum element removed

# ne divided by lowest ne
ne_by_min_ne = []
for i in range(len(ne)):
    if(i == min_ne_index):
        continue
    ne_by_min_ne.append(ne[i] / min_ne)


# Nearest effective integer 
## It rounds down to 0.5
nearest_neff = []
for i in range(len(ne_by_min_ne)):
    temp = (ne_by_min_ne[i] * 10) % 5

    if(temp < 2.5):
        nearest_neff.append(((ne_by_min_ne[i] * 10) // 5) * 0.5)
    elif (temp < 7.5):
        nearest_neff.append(((ne_by_min_ne[i] * 10) // 5) * 0.5 + 0.5)
    else:
        nearest_neff.append(((ne_by_min_ne[i] * 10) // 5) * 0.5 + 1)

# ne divided by nearest effective integer 
ne_by_neff = []

# Defining x and y lists for later use in linear regression
x = []      # nearest_neff - Nearest Effective Integer, with 0.5 cases removed
y = []      # new_ne - ne with cases corresponding to 0.5 closest integer removed

for i in range(len(nearest_neff)):
    if(nearest_neff[i]%1 == 0):     # Reject the 0.5 cases
        ne_by_neff.append(new_ne[i] / nearest_neff[i])
        x.append(nearest_neff[i].n)
        y.append(new_ne[i].n)


# Trying out all differences in ne and finding lowest         
lowest_diff_ne = abs(ne[1] - ne[0])
for i in range(1, len(ne)):
    for j in range(i):
        diff = abs(ne[i] - ne[j])
        if(diff < lowest_diff_ne):
            lowest_diff_ne = diff 

# Define a linear function for regression
def linear(x, m):
    return m*x

# Fitting the curve with scipy.optimize.curve_fit
popt, pcov = curve_fit(linear, x, y) 

# Final values of e

## e as approximate gcd
e = np.mean(ne_by_neff)

## e from linear regression through points obtained above
e_lr = ufloat(popt[0], np.sqrt(np.diag(pcov)))

## Literature Value of e
e_lv = 1.602E-19

# Printing all the required stuff

print("----------DYNAMIC METHOD----------")
print("---Fall Times---")
for i in range(len(fall_time)):
    print(f"Droplet {i+1}")
    display(fall_time[i], 1, "u")

print("---Rise Times---")
for i in range(len(rise_time)):
    print(f"Droplet {i+1}")
    display(rise_time[i], 1, "u")

print("---Voltage---")
display(V, 1, "u")    

print("---Mean Fall Time---")
display(tf, 1, "u")

print("---Mean Rise Time---")
display(tr, 1, "u")

print("---Fall Velocity---")
display(vf, 3)

# Xi
print("---\u03BE---")
display(xi, 3)

print("---r---")
display(r, 3)

# r^3
print("---r\u00B3---")
display(r3, 3)

print("---T---")
display(T, 1, "u")

print("---ne---")
display(ne, 3)

print("---ne divided by lowest---")
display(ne_by_min_ne, 1, "u")

print("---Nearest integer neff---")
for i in nearest_neff:
    print(i.n)
print()

print("---ne/neff---")
print("The 0.5 values are rejected automatically")
display(ne_by_neff, 3)

print("---Value of e---")
print("Value of e as approximate gcd: {:.3eP}".format(e))
print("Error = {:.2f}%\n".format((abs(e.n - e_lv) / e_lv) * 100))

print("Value of e from regression: {:.3eP}".format(e_lr))
print("Error = {:.2f}%\n".format((abs(e_lr.n - e_lv) / e_lv)*100))

print("Lowest difference in values of ne: {:.3eP}".format(lowest_diff_ne))

print()
print("---Other Constants---")
print("C = {:.3f}".format(C))
print("D = {:.3e}".format(D))
print("\u03C2 = {:.3e}".format(sigma))