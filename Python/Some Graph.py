import numpy as np
import matplotlib.pyplot as plt

number_of_ethnic_groups = "Sixteen"

file = np.loadtxt(f"Ethnic Groups {number_of_ethnic_groups}.csv", delimiter = ",", skiprows = 20, usecols = (0, 1, 5, 9, 13), dtype = int)

x = file[:,0]
CC = file[:, 1]
CD = file[:, 2]
DC = file[:, 3]
DD = file[:, 4]

#plt.plot(x, CC, ".", x, CD, "-", x, DC, "|", x, DD, "+")
#plt.show()

n = 25

x1 = [file[i, 0] for i in range(len(x)) if i % n == 0]
CC1 = [file[i, 1] for i in range(len(x)) if i % n == 0]
CD1 = [file[i, 2] for i in range(len(x)) if i % n == 0]
DC1 = [file[i, 3] for i in range(len(x)) if i % n == 0]
DD1 = [file[i, 4] for i in range(len(x)) if i % n == 0]


print(f"CC: {CC[-1]}")
print(f"CD: {CD[-1]}")
print(f"DC: {DC[-1]}")
print(f"DD: {DD[-1]}")

plt.plot(x1, CC1, "^-", x1, CD1, ".-", x1, DC1, "|-", x1, DD1, "x-")
plt.xlabel("Ticks")
plt.ylabel("Population")
plt.legend(["CC", "CD", "DC", "DD"])
plt.title(f"{number_of_ethnic_groups} Ethnic Groups")
plt.savefig(f"{number_of_ethnic_groups} Ethnic Groups.png")
