from matplotlib import pyplot as plt

def outliers_view(data):
    plt.boxplot(data, vert = False)
    plt.show()

def suavizamiento_view(real, suavizada):
    x = [i+1 for i in range(len(real))]
    plt.figure(figsize=(12, 6))
    plt.plot(x, real, label='REAL', color='blue')
    plt.plot(x, suavizada, label='SUAVIZADA', color='green')
    plt.title('Comparación de Series')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.grid(True)
    plt.show()