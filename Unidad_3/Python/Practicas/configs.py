preferencias_servicios = {  # 0 = minimizacion -- 1 = maximizacion
    "temperatura": [20, 28, 0, 0.4, 8],
    "humedad": [40, 70, 0, 0.2, 3],
    "ruido": [30, 65, 0, 0.1, 1],
    "int_luminosa": [300, 1000, 1, 0.3, 5]
} # [minimo, maximo, problema, peso, costo]

multiplicador = {
    "temperatura": 1.4,
    "humedad": 1.4,
    "ruido": 2,
    "int_luminosa": 0.1
}

N_SERVICIOS = len(preferencias_servicios)
ALFA = 0.5
BETA = 0.5

# Algoritmo Genético
N_POP = 100
N_PARENTS = 50
PROBABILIDAD_MUTA = 5