# w = 0.4
# nValor = w * lecturaActual + (1 - w) * nValor
from procesamiento.tratamiento import tratamiento_vacios, tratar_outliers_return_solo_valores
import serial as conn
import time as tm
import pandas as pd

if __name__ == "__main__":
    arduino = conn.Serial(port="COM5", baudrate=9600, timeout=1)
    dia = 0
    alfa = 0.75
    max_lecturas = 24
    intervalo = 1.5 # segundos
    w = 0.4
    n = 0
    series = {
        'todas': [],
        'real': [0 for x in range(max_lecturas)],
        'suavizada': [0 for y in range(max_lecturas)]
    }
    dias = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']

    while True:
        if dia > len(dias): dia = 0
        try:
            tm.sleep(intervalo)
            arduino.reset_input_buffer()
            value = arduino.readline().decode().strip() # No importa leerlo siempre
            if dia == 0:
                if not value: continue
                if n < max_lecturas:
                    series['real'] = tratamiento_vacios(([[i + 1, series['real'][i]] for i in range(len(series['real']))]))
                    series['real'] = tratar_outliers_return_solo_valores(series['real'])
                    series['real'][n] = int(value)
                    print(f'{dias[dia]}: {n:02}:00 - Valor: {value}')
                    n += 1
                else:
                    series['todas'].append(series['real'])
                    dia = 1
                    n = 0
            else:
                # print(f'{dias[dia]}:'
                if n == 0: series['suavizada'][n] = series['real'][n]
                else:
                    nValor = round(alfa * series['real'][n] + (1 - alfa) * series['suavizada'][n - 1], 4)
                    nValor = w * value + (1 - w) * nValor # Promedio Ponderado
                    series['suavizada'][n] = nValor
                if series['suavizada'][n] > 35:
                    arduino.write(b'3')
                elif series['suavizada'][n] > 15:
                    arduino.write(b'2')
                else:
                    arduino.write(b'1')
                print(f'{dias[dia]}: {n:02}:00 - Valor: {series["suavizada"][n]}')
                n += 1

                if n == max_lecturas:
                    series['todas'].append(series['suavizada'])
                    series['real'] = series['suavizada']
                    dia = (dia + 1) % 7
                    n = 0
        except KeyboardInterrupt:
            print("\nDesconectando...")
            df = pd.DataFrame(series['todas'])
            df.to_csv('../Archivos/valores_P06.csv', index=False)
            arduino.close()