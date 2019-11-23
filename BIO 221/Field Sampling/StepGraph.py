import numpy as np 
import matplotlib.pyplot as plt 

data = np.loadtxt("Florets Graph Data.csv", skiprows = 1, delimiter = ",")

labels = ["Florets", "White-top", "Purple-top", "White-side", "Purple-side"]

x = data[:,0]

markers = ["s-", "x-.", "o--", "D:"]

for i in range(4):
    plt.step(x, data[:,i+1], markers[i])
plt.legend(labels[1:])

plt.xlabel("Number of florets per inflorescence")
plt.ylabel("Fractional Occurences")

plt.show()