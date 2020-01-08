import numpy as np 
import matplotlib.pyplot as plt 

LeslieMatrix = np.array([ [0,2,1,1],
                          [0.5,0,0,0],
                          [0,0.2,0,0],
                          [0,0,0.1,0] ])

PopulationAtTimet = np.transpose(np.array([200,0,0,0]))
n = 200
TotalPopulationAtTimet = np.zeros(201)
PopulationRatio = np.zeros([4, 200])

TotalPopulationAtTimet[0] = np.sum(PopulationAtTimet)
Time201 = [i for i in range(0,201)]
Time200 = [i for i in range(0,200)]

for i in range(n):
    PopulationAtTimetPlus1 = np.matmul(LeslieMatrix, PopulationAtTimet)
    print(PopulationAtTimetPlus1, end = ' => ')
    
    TotalPopulationAtTimet[i+1] = np.sum(PopulationAtTimetPlus1)
    print(TotalPopulationAtTimet[i+1])
    
    for j in range(4):
        PopulationRatio[j][i] = PopulationAtTimetPlus1[j]/PopulationAtTimet[j]

    PopulationAtTimet = PopulationAtTimetPlus1

plt.plot(Time201, TotalPopulationAtTimet)
plt.xlabel('Time')
plt.ylabel('Total Population at Time t')
plt.show()
plt.clf()

for i in range(4):
    print(PopulationRatio[i])
    plt.plot(Time200, PopulationRatio[i])
    plt.xlabel('Time')
    plt.ylabel(r'$\frac{n_{x+1}}{n_{x}}$')
    plt.show()
    plt.clf()


TotalPopulationRatio = [TotalPopulationAtTimet[i+1]/TotalPopulationAtTimet[i] for i in range(200)]

plt.plot(Time200, TotalPopulationRatio)
plt.xlabel('Time')
plt.ylabel(r'$\frac{N_{x+1}}{N_{x}}$')
plt.show()
plt.clf()