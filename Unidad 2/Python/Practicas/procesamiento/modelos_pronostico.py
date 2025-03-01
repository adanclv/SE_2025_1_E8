import numpy as np
from statsmodels.tsa.arima.model import ARIMA

def interpolacion_lineal(data, index):
    x1, y1 = None, None
    if index > 0:
        x1 = data[index - 1][0]
        y1 = data[index - 1][1]

    x2, y2 = None, None
    if index < len(data) - 1:
        x2 = data[index + 1][0]
        y2 = data[index + 1][1]

    if x1 is not None and x2 is not None:
        newValue = y1 + (y2 - y1) / (x2 - x1) * (data[index][0] - x1)
    elif x1 is None:
        newValue = y2
    elif x2 is None:
        newValue = y1

    return newValue

def calc_suavizado_exponencial(serie, alfa):
    # El parámetro alfa controla el peso que se le da a los datos
    # valores cercanos a 1 hacen que los datos recientes tengan más influencia
    # valores cercanos a 0 dan más importancia a los datos antiguos

    new_serie = np.zeros_like(serie) # reserva memoria y rellena con ceros
    new_serie[0] = serie[0]  # El primer valor suavizado es el primer valor de la serie real
    for t in range(1, len(serie)): #calcula los nuevos valores para la serie suavizada
        new_serie[t] = round(alfa * serie[t] + (1 - alfa) * new_serie[t-1], 4)
    return new_serie

def calc_ARIMA(serie):
    p = 1
    d = 1
    q = 1
    n = len(serie)
    modelo = ARIMA(serie, order=(p, d, q))
    ajuste = modelo.fit()
    pronostico = ajuste.forecast(steps=n)  # Un paso adelante
    return pronostico