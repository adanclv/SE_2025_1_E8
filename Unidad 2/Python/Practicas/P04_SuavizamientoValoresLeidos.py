import matplotlib.pyplot as plt
from procesamiento.carga_datos import cargar_data
from procesamiento.evaluacion import calcRMSE
from procesamiento.tratamiento import tratamiento_vacios, tratar_outliers
from procesamiento.suavizado import calc_suavizado_exponencial
from procesamiento.visualizacion import outliers_view, suavizamiento_view

if __name__ == '__main__':
    header, data = cargar_data('../Archivos/lecturaFoto.csv')
    data = tratamiento_vacios(data)
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