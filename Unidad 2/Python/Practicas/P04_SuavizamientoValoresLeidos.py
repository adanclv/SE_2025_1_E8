from procesamiento.modelos_pronostico import calc_suavizado_exponencial
from procesamiento.visualizacion import suavizamiento_view
from load_data import cargar_data

if __name__ == '__main__':
    semana = 4
    data = cargar_data(f'../Archivos/lecturaFotoS{semana}_tratada.csv')
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
    suavizada = calc_suavizado_exponencial(data, alfa)
    suavizamiento_view(data, suavizada)

    print(data)
