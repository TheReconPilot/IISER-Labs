import numpy as np 
import matplotlib.pyplot as plt 

data_635 = np.loadtxt("635 nm.csv", delimiter=",", skiprows=2)
data_460 = np.loadtxt("460 nm.csv", delimiter=",", skiprows=2)

VR_635 = data_635[:, 0]
I_25_635 = data_635[:, 1]
I_40_635 = data_635[:, 2]

VR_460 = data_460[:, 0]
I_25_460 = data_460[:, 1]
I_40_460 = data_460[:, 2]

IN_25_635 = [i/I_25_635[0] for i in I_25_635]
IN_40_635 = [i/I_40_635[0] for i in I_40_635]

IN_25_460 = [i/I_25_460[0] for i in I_25_460]
IN_40_460 = [i/I_40_460[0] for i in I_40_460]

x_0 = np.linspace(min(min(VR_460), min(VR_635)), max(max(VR_460), max(VR_635)))
y_0 = [0 for i in x_0]

# 25 cm
plt.subplot(1, 2, 1)
plt.plot(VR_635, IN_25_635, "go-", label="635 nm")
plt.plot(VR_460, IN_25_460, "r^-", label="460 nm")
plt.plot(x_0, y_0, "b:")
plt.legend()
plt.xlabel("$V_R$ (Voltage) [V]")
plt.ylabel("$I_N$ (Normalized Current) [nA]")
plt.title("25 cm")

# 40 cm
plt.subplot(1, 2, 2)
plt.plot(VR_635, IN_40_635, "go-", label="635 nm")
plt.plot(VR_460, IN_40_460, "r^-", label="460 nm")
plt.plot(x_0, y_0, "b:")
plt.legend()
plt.xlabel("$V_R$ (Voltage) [V]")
plt.ylabel("$I_N$ (Normalized Current) [nA]")
plt.title("40 cm")
plt.show()


"""
    plt.plot(VR, IN_25, "go-", label="25 cm")
    plt.plot(VR, IN_45, "r^:", label="45 cm")
    plt.legend()
    plt.xlabel("$V_R$ (Voltage) [V]")
    plt.ylabel("$I_N$ (Normalized Current) [nA]")
    plt.title(f"{lambda_arr[i]} nm")
    plt.show()
"""