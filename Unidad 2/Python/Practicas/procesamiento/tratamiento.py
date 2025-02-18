import math
from .suavizado import interpolacion_lineal

def tratamiento_vacios(data):
    for i in range(len(data)):
        if data[i][1] is None:
            data[i][1] = interpolacion_lineal(data, i)
    return data

def to_int(columna):
    col = [int(e) if e.strip() else None for e in columna]
    return col

def tratar_outliers(data):
    data.sort(key=lambda x: x[1])
    posQ1 = 1 * (len(data) - 1) / 4 + 1
    posQ3 = 3 * (len(data) - 1) / 4 + 1

    p_decimal, p_entera = math.modf(posQ1)
    p_entera = int(p_entera)
    Q1 = data[p_entera-1][1] + p_decimal * (data[p_entera][1] - data[p_entera-1][1])

    p_decimal, p_entera = math.modf(posQ3)
    p_entera = int(p_entera)
    Q3 = data[p_entera-1][1] + p_decimal * (data[p_entera][1] - data[p_entera-1][1])

    IQR = Q3 - Q1
    whiskers = 1.5 # tolerancia
    lower_limit = Q1 - whiskers * IQR
    upper_limit = Q3 + whiskers * IQR

    data.sort(key=lambda x: x[0])
    for i in range(len(data)):
        if data[i][1] < lower_limit or data[i][1] > upper_limit:
            data[i][1] = interpolacion_lineal(data, i)

    return data