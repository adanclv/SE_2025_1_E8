import matplotlib.pyplot as plt
from procesamiento.carga_datos import cargar_data
from procesamiento.evaluacion import calcRMSE
from procesamiento.tratamiento import to_int, tratamiento_vacios, tratar_outliers
from procesamiento.modelos_pronostico import interpolacion_lineal, calc_suavizado_exponencial
from procesamiento.visualizacion import outliers_view, suavizamiento_view

if __name__ == '__main__':
    header, data = cargar_data('../Archivos/lecturaFotoS2.csv')
    data = list(zip(*data)) #.T
    data[0] = to_int(data[0])
    data[1] = to_int(data[1])
    data = tratamiento_vacios(list(map(list, zip(*data))))

    outliers_view([fila[1] for fila in data]) # Visualización de outliers
    data = tratar_outliers(data)
    # alfas = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]  # linespace
    #
    # minErorr = 1000
    # best_alfa = -1
    # for alfa in alfas:
    #     serie_suavizada = calc_suavizado_exponencial([fila[1] for fila in data], alfa)
    #     errorRMSE = calcRMSE([fila[1] for fila in data], serie_suavizada)
    #     print(alfa, errorRMSE)
    #
    #     if minErorr > errorRMSE:
    #         minErorr = errorRMSE
    #         best_alfa = alfa
    #
    # print("Best alfa: ", best_alfa)
    alfa = 0.75
    suavizada = calc_suavizado_exponencial([fila[1] for fila in data], alfa)
    suavizamiento_view([fila[1] for fila in data], suavizada)

    print(data)