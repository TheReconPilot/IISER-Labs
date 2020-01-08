import numpy as np
import matplotlib.pyplot as plt 
from scipy.optimize import curve_fit

data_file = np.loadtxt("Growth Curve Data.csv", delimiter = ",", skiprows = 1)

labels = ["pH 5.5, Ori","pH 7.0, Ori","pH 8.5, Ori","pH 5.5, 1:5 dilution","pH 7.0, 1:5 dilution","pH 8.5, 1:5 dilution","pH 5.5, 1:10 dilution","pH 7.0, 1:10 dilution","pH 8.5, 1:10 dilution"]

time = data_file[:,0]
markers = [".", "o", "^", "+", "*", "s", "D", "|", "_"]

for i in range(1, 10):
    plt.plot(time, data_file[:,i], markers[i-1]+"--")

plt.xlabel("Time (min)")
plt.ylabel("Optical Density")
plt.legend(labels)
plt.show()