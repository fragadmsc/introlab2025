#imports
import numpy as np

#constants
CTE_MAO = 2
DIST_ENTRE_LASER = 0.965
DIST_ATE_LASER = 0.068
CTE_LASER = 2*pow((DIST_ATE_LASER + DIST_ENTRE_LASER)**(0.5)-(DIST_ATE_LASER)**(0.5), 2)

if __name__ == "__main__":
    print(CTE_LASER)
    #convert the laser data into acceleration data
    data = np.loadtxt("data_laser.dat")
    data = CTE_LASER/data**2
    np.savetxt('data_acel_laser.dat', data, fmt='%.4f', delimiter=' ')
    print(np.mean(data))
    print(np.std(data))
    #convert the hand data into acceleration data
    data = np.loadtxt("data_mao.dat")
    data = CTE_MAO/data**2
    np.savetxt('data_acel_mao.dat', data, fmt='%.4f', delimiter=' ')
    print(np.mean(data))
    print(np.std(data))

