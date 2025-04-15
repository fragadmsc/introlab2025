#imports
import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.stats import norm

#constants
NUM_BINS_mao = 30

GREEN = '#2ecc71'
PINK = '#e84393'
BLUE = '#3498db'
ORANGE = '#e67e22'
DARK_GREEN = '#27ae60'
DARK_PINK = '#d63080'
DARK_BLUE = '#2980b9'
DARK_ORANGE = '#d35400'
DARK_GREY = "#222"


if __name__ == "__main__":
    #plotar o grafico de data_completa
    matriz_valores = []
    data_completa = []
    with open("data_acel_mao.dat", "r") as file:
        for line in file:
            row = [float(x) for x in line.strip().split()]
            data_completa = data_completa + row
            matriz_valores.append(row)

    #a primeira eh que joga e a segunda eh quem marca
    duduCaua = [row[0] for row in matriz_valores]
    cauaDudu = [row[1] for row in matriz_valores]
    duduFrag = [row[2] for row in matriz_valores]
    fragDudu = [row[3] for row in matriz_valores]
    fragCaua = [row[4] for row in matriz_valores]
    cauaFrag = [row[5] for row in matriz_valores]

    #plotting the histogram
    plt.figure(figsize=(10, 7))
    
    data_size, bins, c = plt.hist(
        [duduFrag, cauaFrag, duduCaua, fragCaua, fragDudu, cauaDudu], 
        NUM_BINS_mao, 
        edgecolor = DARK_GREY,
        color = [BLUE, DARK_BLUE, GREEN, DARK_GREEN, ORANGE, DARK_ORANGE],
        stacked = True,
        linewidth = 1.2,
        zorder = 3,
        label = ["Lucas e Eduardo",
                 "Lucas e Cauan", 
                 "Cauan e Eduardo",
                 "Cauan e Lucas",
                 "Eduardo e Lucas",
                 "Eduardo e Cauan",
                 ]
    )
    plt.grid(
        zorder = 0
    )

    plt.legend()
    bins = [round(x, 4) for x in bins]

    plt.xticks(bins, rotation=45, ha = 'right')
    plt.yticks(range(0, 20))
    plt.xlabel('Aceleração [m/s²]', fontsize=12)
    plt.ylabel('Frequência', fontsize=12)
    plt.title('Histograma de dados da aceleração da gravidade obtidos no experimento com a mão', pad=20)

    #plt.show()
    #plt.savefig("histograma_mao.png")

    #making the fit
    media = np.mean(data_completa)
    desvio = np.std(data_completa)
    print(f"media: {media}, desvio: {desvio}")

    plot_x = np.linspace(min(data_completa), max(data_completa), 100)
    bin_width = bins[1]-bins[0]
    plot_y = norm.pdf(plot_x, media, desvio)*bin_width*len(data_completa) #faz a bell curve
    plt.plot(plot_x, plot_y, 'r-', linewidth = 2, zorder = 5)

    #plt.savefig("histograma_mao_acel_fit.png")
