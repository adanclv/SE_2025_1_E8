import time as tm
import serial as conn
from procesamiento.tratamiento import to_int, tratamiento_vacios, tratar_outliers
from procesamiento.suavizado import calc_suavizado_exponencial
from matplotlib import pyplot as plt

def lectura_sensor(intervalo, max_lecturas):
    serie_original = list()
    no_lectura = 1
    while no_lectura <= max_lecturas:
        tm.sleep(intervalo)
        arduino.reset_input_buffer()
        linea = arduino.readline().decode().strip()
        serie_original.append([no_lectura, linea])
        print(f"Lectura: {no_lectura}, Valor:{linea}")
        no_lectura += 1
    return serie_original


if __name__ == '__main__':
    intervalo = 1
    max_lecturas = 24
    alfa = 0.75
    dias = 0
    vector = list()
    series = list()
    n = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']
    h = ['8am', '9am', '10am', '11am', '12pm', '1pm', '2pm', '3pm', '4pm', '5pm', '6pm', '7pm', '8pm', '9pm', '10pm', '11pm', '12am', '1am', '2am', '3am', '4am', '5am', '6am', '7am', '8am']

    arduino = conn.Serial(port="COM5", baudrate=9600, timeout=1)

    try:
        while True:
            if dias == 0:
                vector = lectura_sensor(intervalo, max_lecturas)
                for serie in vector:
                    serie[1] = int(serie[1]) if serie[1].strip() else None
                vector = tratamiento_vacios(vector)
                vector = tratar_outliers(vector)
                # print(series, len(series))
                series.append(vector)
                vector = [v[1] for v in vector]
                dias += 1
                continue

            # print(vector)

            nVector = [vector[0]]
            print(f'{n[dias]} - {h[0]}: {vector[0]}')
            for i in range(1, len(vector)):
                nValor = round(alfa * vector[i] + (1 - alfa) * nVector[i-1], 4)
                nVector.append(nValor)
                if nValor > 35:
                    arduino.write(b"3")
                elif nValor > 15:
                    arduino.write(b"2")
                else:
                    arduino.write(b"1")
                print(f'{n[dias]} - {h[i]}: {nValor}')

                tm.sleep(2)
            vector = nVector
            series.append(nVector)
            print(vector, '\n')
            dias = (dias + 1) % 3

    except KeyboardInterrupt:
        print(series, len(series))
        print("\nDesconectando...")
        arduino.close()