prefServicios = {  # 0 = minimizacion -- 1 = maximizacion
    "temperatura": [20, 28, 0, 0.4, 8],
    "humedad": [40, 80, 0, 0.2, 3],
    "ruido": [60, 120, 0, 0.1, 1],
    "int_luminosa": [400, 900, 1, 0.3, 5]
}

print(list(prefServicios.keys())[0])