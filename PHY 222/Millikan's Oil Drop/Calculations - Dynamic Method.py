import numpy as np 
from uncertainties import ufloat
from uncertainties import unumpy as unp 

# Display List function to conveniently check lists
def display(plist):
    for i in range(len(plist)):
        print(plist[i])
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
L = 0.001       # Distance between lines, in m
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
tf = []     # Mean Free Fall Time
tr = []     # Mean Rise Time

# Length of fall_time and rise_time is same
for i in range(len(fall_time)):
    Sum_ft = 0
    Sum_rt = 0
    for j in range(len(fall_time[i])):
        Sum_ft += fall_time[i][j]
        Sum_rt += rise_time[i][j]

    tf.append(Sum_ft/len(fall_time[i]))
    tr.append(Sum_rt/len(fall_time[i]))


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
for i in range(len(nearest_neff)):
    if(nearest_neff[i]%1 == 0):     # Reject the 0.5 cases
        ne_by_neff.append(new_ne[i] / nearest_neff[i])

# Trying out all differences in ne and finding lowest

lowest_diff_ne = abs(ne[1] - ne[0])
for i in range(1, len(ne)):
    for j in range(i):
        diff = abs(ne[i] - ne[j])
        if(diff < lowest_diff_ne):
            lowest_diff_ne = diff 

