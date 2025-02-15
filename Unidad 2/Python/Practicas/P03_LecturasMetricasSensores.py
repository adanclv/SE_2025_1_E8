import numpy as np
import pandas as pd
import serial as conn

if __name__ == '__main__':
    print('Práctica 3 Unidad 2')
    arduino = conn.Serial(port='COM5', baudrate=9600, timeout=1)
    print('Conectado')

    valores = {
        i: {
            'media': [],
            'mediana': [],
            'mayor': [],
            'menor': [],
            'moda': [],
            'base': []
        } for i in range(6)
    }
    lineas = list()
    metricas = ['media', 'mediana', 'mayor', 'menor', 'moda', 'base']
    desviacion = np.zeros(shape=(6, 6))
    count = 0

    while count < 100:
        linea = arduino.readline().decode().strip()
        if not linea: continue
        print(linea)
        lineas.append(linea)
        secciones = linea.split(';')
        for i in range(6):
            pin_values = list(map(int, secciones[i].split(',')))
            for j in range(6):
                valores[j][metricas[i]].append(pin_values[j])
        count += 1
        print('Leido', count)

    arduino.close()

    for i in range(6):
        for j in range(6):
            desviacion[i][j] = np.std(valores[j][metricas[i]])

    df = pd.DataFrame(desviacion).T
    df.columns = ['Media', 'Mediana', 'Mayor', 'Menor', 'Moda', 'Base']
    df.to_csv('../Archivos/desviacion.csv', index=False)
    print(df)