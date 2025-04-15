#imports
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

#constants
NUM_BINS_LASER = 30

GREEN = '#2ecc71'
PINK = '#e84393'
BLUE = '#3498db'
ORANGE = '#e67e22'
DARK_GREY = "#222"


if __name__ == "__main__":
    #plotar o grafico de data_mao
    with open("data_acel_laser.dat", "r") as file:
        data_laser = file.readlines()
    
    data_laser = [float(x.strip()) for x in data_laser] #converts to float

    #plotting the histogram
    plt.figure(figsize=(10, 7))

    data_size, bins, c = plt.hist(
        data_laser, 
        NUM_BINS_LASER, 
        edgecolor = DARK_GREY,
        color = PINK,
        linewidth = 1.2,
        zorder = 3
    )
    plt.grid(
        zorder = 0
    )
    bins = [round(x, 4) for x in bins]

    plt.xticks(bins, rotation=45, ha = 'right')
    plt.yticks(range(0, 16))
    plt.xlabel('Aceleração [m/s²]', fontsize=12)
    plt.ylabel('Frequência', fontsize=12)
    plt.title('Histograma de dados da aceleração obtidos no experimento', pad=20)

    #plt.show()
    

    #making the fit
    media = np.mean(data_laser)
    desvio = np.std(data_laser)
    print(f"media: {media}, desvio: {desvio}")

    plot_x = np.linspace(min(data_laser), max(data_laser), 100)
    bin_width = bins[1]-bins[0]
    plot_y = norm.pdf(plot_x, media, desvio)*bin_width*len(data_laser) #faz a bell curve
    plt.plot(plot_x, plot_y, 'r-', linewidth = 2, zorder = 5)

    plt.savefig("histograma_laser_acel_fit.png")