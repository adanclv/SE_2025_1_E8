import serial as conn
import pandas as pd
import numpy as np

if __name__ == '__main__':
    print('Práctica 1 Unidad 2')
    arduino = conn.Serial(port='COM5', baudrate=9600, timeout=1)
    print('Conectado')
    valores = list()

    while len(valores) < 100:
        serialMonitor = arduino.readline().decode().strip()

        if not serialMonitor: continue
        val = list(map(int, serialMonitor.split(',')))
        valores.append(val)

    arduino.close()
    df = pd.DataFrame(valores)
    # df.to_csv('../Archivos/valores_P1.csv', index=False, header=False)
    print(df)
    print("Media", np.std(df[0]))
    print("Mediana", np.std(df[1]))
    print("Mayor", np.std(df[2]))
    print("Menor", np.std(df[3]))
    print("Moda", np.std(df[4]))
    print("Base", np.std(df[5]))
