import serial as conn
import time as tm
import re
from procesamiento.consts import *
from procesamiento.AlgoritmoGenetico import main_GA
from procesamiento.Preferencias import Preferencias
from ClientREST import insertRecord, insertDecision

def leer_data(connection):
    connection.reset_input_buffer()
    data = connection.readline().decode().strip()
    print(f"Datos leídos del Arduino: {data}")
    return data

def procesar_data(data):
    if re.match(REGEX_SENSORS_DATA, data):
        data = data[1:-1]
        values = data.split('-')
        values = [int(value) for value in values]
        return values
    return None

def escribir_valor(connection, index):
    try:
        connection.write(bytes([index]))
        print(f"Valor enviado al Arduino: {index}")
    except Exception as e:
        print(f"No se pudo escribir en el puerto serial: {e}")

def cambiar_estado(connection, index, estados, new_estado):
    if estados[index] != new_estado:
        escribir_valor(connection, index)
        estados[index] = new_estado
        estado_texto = "encendido" if new_estado else "apagado"
        print(f'Cambio de estado del relé {index + 1} a {estado_texto}')
    else:
        print(f'No hubo cambio de estado para el relé {index + 1}')

    registrar_records(estados, IDS_RELE)  # POST RECORD
    return estados

def distancia(a, b):
    res = abs(a - b)
    return res

def registrar_records(values, ids):
    try:
        for i, value in enumerate(values):
            insertRecord(ids[i], value)
    except Exception as e:
        print(f"Error al registrar valores: {e}")

def registrar_decision(current_value, decision):
    try:
        insertDecision(current_value, decision)
    except Exception as e:
        print(f"Error al registrar decisión: {e}")

if __name__ == '__main__':
    print("Iniciando el programa...")
    preferencias = Preferencias(minimo=MINIMO,
                                maximo=MAXIMO,
                                problema=PROBLEMA,
                                peso=PESO,
                                costo=COSTO)
    intervalo = 10
    estados = [False, False, False]
    port = "COM5"

    try:
        arduino = conn.Serial(port=port, baudrate=9600, timeout=1)
        print(f"Conexión establecida con Arduino en {port}")

        while True:
            data = leer_data(arduino)
            values = procesar_data(data)
            if values is None:
                print("No se pudieron procesar los datos.")
                continue

            registrar_records(values, IDS_LDR) # POST RECORD
            valor_actual = values.pop(0)
            print(f'Valor actual: {valor_actual}')

            valor_optimo = main_GA(preferencias, valor_actual)
            print(f'Valor óptimo calculado: {valor_optimo}')
            registrar_decision(valor_actual, valor_optimo) #POST DECISION

            focos = [distancia(valor_actual, valor) for valor in values]
            if valor_actual < valor_optimo:
                index = focos.index(max(focos))
                estados = cambiar_estado(arduino, index, estados, True)
            elif valor_actual > valor_optimo:
                index = focos.index(min(focos))
                estados = cambiar_estado(arduino, index, estados, False)

            print('\n')
            tm.sleep(intervalo)
    except KeyboardInterrupt:
        print("\nDesconectando...")
        arduino.close()