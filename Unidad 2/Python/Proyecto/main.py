# w = 0.4
# nValor = w * lecturaActual + (1 - w) * nValor
from procesamiento.tratamiento import tratamiento_vacios, tratar_outliers_return_solo_valores
from procesamiento.modelos_pronostico import suavizar_dato
import serial as conn
import time as tm

def leer_valor(conexion):
    conexion.reset_input_buffer()
    value = conexion.readline().decode().strip()
    return value

def escribir_valor(conexion, valor):
    if valor > 35:
        conexion.write(bytes([255]))
    elif valor > 15:
        conexion.write(bytes([63]))
    else:
        conexion.write(bytes([3]))

def peso_formula1(real, suavizado):
    numerador = abs(real - suavizado)
    denominador = abs(real) + abs(suavizado)
    return numerador/denominador

def peso_formula2(peso, x, real, suavizado):
    peso = peso + x*(real - suavizado)
    return peso

if __name__ == "__main__":
    arduino = conn.Serial(port="COM5", baudrate=9600, timeout=1)
    alfa = 0.75
    w = 0.5
    x = 0.2
    max_lecturas = 24
    intervalo = 1.5
    real = [0 for _ in range(max_lecturas)]
    suavizada = [0 for _ in range(max_lecturas)]
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
                if n == 0:
                    suavizada[n] = real[n]
                else:
                    nValor = suavizar_dato(real[n], suavizada[n - 1], alfa)
                    # dobleu = w
                    # dobleu = peso_formula1(int(value), nValor)
                    dobleu = peso_formula2(w, x, int(value), nValor)
                    #print(w,x,dobleu, value, nValor)
                    nValor = dobleu * int(value) + (1 - dobleu) * nValor  # Promedio Ponderado
                    suavizada[n] = round(nValor, 4)

                escribir_valor(arduino, suavizada[n])
                print(f'{dias[dia]}: {n:02}:00 - Valor: {suavizada[n]}')
                n += 1

                if n == max_lecturas:
                    real = suavizada
                    dia = (dia + 1) % 7
                    n = 0
    except KeyboardInterrupt:
        print("\nDesconectando...")
        arduino.close()