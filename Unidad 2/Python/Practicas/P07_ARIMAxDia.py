from procesamiento.tratamiento import tratamiento_vacios, tratar_outliers_return_solo_valores
from procesamiento.modelos_pronostico import calc_ARIMA
import serial as conn
import time as tm

def leer_valor(conexion):
    conexion.reset_input_buffer()
    valor = conexion.readline().decode().strip()
    return valor

def escribir_valor(conexion, valor):
    if valor > 35:
        conexion.write(bytes([255]))
    elif valor > 15:
        conexion.write(bytes([63]))
    else:
        conexion.write(bytes([3]))

if __name__ == "__main__":
    arduino = conn.Serial(port="COM5", baudrate=9600, timeout=1)
    alfa = 0.75
    max_lecturas = 24
    intervalo = 1.5

    real = [0 for _ in range(max_lecturas)]
    predicha = list()
    dias = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']

    dia = 0
    n = 0
    try:
        while True:
            tm.sleep(intervalo)
            value = leer_valor(arduino)

            if dia == 0:
                real[n] = int(value) if value else None
                print(f'{dias[dia]}: {n:02}:00 - Valor: {value}')
                n += 1

                if n == max_lecturas:
                    real = tratamiento_vacios([[i + 1, real[i]] for i in range(len(real))])
                    real = tratar_outliers_return_solo_valores(real)
                    dia = 1
                    n = 0
            else:
                '''nValor = round(calc_ARIMA(real), 4) # predice de 1 en 1
                real.append(nValor)
                suavizada[n] = nValor
                real.pop(0)'''
                if n == 0:
                    predicha = calc_ARIMA(real) # predice 24, len(serie)

                escribir_valor(arduino, predicha[n])
                print(f'{dias[dia]}: {n:02}:00 - Valor: {predicha[n]}')
                n += 1

                if n == max_lecturas:
                    real = predicha
                    dia = (dia + 1) % 7
                    n = 0
    except KeyboardInterrupt:
        print("\nDesconectando...")
        arduino.close()