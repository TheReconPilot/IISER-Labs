import numpy as np
import matplotlib.pyplot as plt

run = "6"

file = np.loadtxt(f"Run{run}.csv", delimiter = ",", skiprows = 20, usecols = (0, 1, 5, 9, 13), dtype = int)
#file = np.loadtxt(f"Ethnic Groups Two.csv", delimiter = ",", skiprows = 20, usecols = (0, 1, 5, 9, 13), dtype = int)


x = file[:,0]
CC = file[:, 1]
CD = file[:, 2]
DC = file[:, 3]
DD = file[:, 4]

#plt.plot(x, CC, ".", x, CD, "-", x, DC, "|", x, DD, "+")
#plt.show()

n = 60

x1 = [file[i, 0] for i in range(len(x)) if i % n == 0]
CC1 = [file[i, 1] for i in range(len(x)) if i % n == 0]
CD1 = [file[i, 2] for i in range(len(x)) if i % n == 0]
DC1 = [file[i, 3] for i in range(len(x)) if i % n == 0]
DD1 = [file[i, 4] for i in range(len(x)) if i % n == 0]


print(f"CC: {CC[-1]}")
print(f"CD: {CD[-1]}")
print(f"DC: {DC[-1]}")
print(f"DD: {DD[-1]}")

plt.plot(x1, CC1, "g^-", x1, CD1, "ro-", x1, DC1, "y|-", x1, DD1, "bx-")
plt.xlabel("Ticks")
plt.ylabel("Population")
plt.legend(["CC", "CD", "DC", "DD"])
#plt.plot(x, CC, "g", x, CD, "r", x, DC, "y", x, DD, "b")
plt.title(f"Run {run}")

ii = 5
mi = 25
ri = 5

txt = f"Initial Immigrants = {ii}\nMax Immigrants = {mi}\nReduced Immigrants = {ri}"

plt.text(3000, 1050, txt, bbox=dict(facecolor = "none", edgecolor='navy'))
#plt.savefig(f"{number_of_ethnic_groups} Ethnic Groups.png")
plt.show()