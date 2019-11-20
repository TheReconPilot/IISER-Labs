import numpy as np 

f = np.loadtxt("inflorescence_rawdata.csv", delimiter = ",", skiprows = 2, dtype = int)

names = ["White Top", "Purple Top", "White Side", "Purple Side"]
raw_data_array = []


x_list = f[:,0]
for i in range(2):
    current_list = f[:,i+1]
    raw_data_list = []
    for j in range(len(current_list)):
        for k in range(current_list[j]):
            raw_data_list.append(x_list[j])
    raw_data_array.append(raw_data_list)


#print(raw_data_array)
#raw_data_array = np.array(raw_data_array)

np.savetxt("inflorawdata.csv", raw_data_array, delimiter = ",", fmt = "%s")