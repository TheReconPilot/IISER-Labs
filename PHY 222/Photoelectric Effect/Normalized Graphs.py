import numpy as np 
import matplotlib.pyplot as plt 

lambda_arr = [635, 460]
filename = [f"{i} nm.csv" for i in lambda_arr]

for i in range(2):
    data = np.loadtxt(filename[i], delimiter=",", skiprows=2)

    VR = data[:, 0]
    I_25 = data[:, 1]
    I_45 = data[:, 2]

    IN_25 = [i/I_25[0] for i in I_25]
    IN_45 = [i/I_45[0] for i in I_45]

    plt.plot(VR, IN_25, "go-", label="25 cm")
    plt.plot(VR, IN_45, "r^:", label="45 cm")
    plt.legend()
    plt.xlabel("$V_R$ (Voltage) [V]")
    plt.ylabel("$I_N$ (Normalized Current) [nA]")
    plt.title(f"{lambda_arr[i]} nm")
    plt.show()