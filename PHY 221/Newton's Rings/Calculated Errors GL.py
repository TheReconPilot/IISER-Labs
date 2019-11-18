import numpy as np 
from uncertainties import ufloat
from uncertainties import unumpy as unp 

lambda_SL = 589.2*1E-9        # Sodium Lamp Wavelength
lambda_GL = 532*1E-9        # Green Laser Wavelength

R_SL = ufloat(56.917, 0.426)    # cm

filename = "Green Laser"

if filename == "Sodium Lamp":
    lambda_light = lambda_SL
else:   # Green Laser
    lambda_light = lambda_GL

# Extract Data
data_file = np.loadtxt(f"{filename} Data.csv", delimiter = ",", skiprows = 1)

# Load the data into variables
order = data_file[:, 0]
up = unp.uarray(data_file[:, 1], 0.01)      # mm
down = unp.uarray(data_file[:, 2], 0.01)    # mm
left = unp.uarray(data_file[:, 3], 0.01)    # mm
right = unp.uarray(data_file[:, 4], 0.01)   # mm

# Calculate diameters
D_ud = down - up
D_lr = right - left
D_avg = (D_ud + D_lr) / 2 

# The final array for D
D = D_avg

D = D / 1000    # m
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

lambda_calculated = [y[i] * 1E11 / (x[i] * 4 * R_SL) for i in range(len(x))]
lambda_mean = np.mean(lambda_calculated)    # nm

print(f"{filename}")
print("Lambda = {:.3uP} nm".format(lambda_mean))
print("Actual Lambda = 532 nm")

error = ((532 - lambda_mean.n)*100)/532
print("Percentage Error = {:.3f}".format(error))