import serial as conn
import time as tm
import requests
import json

def leer_valor(connection):
    connection.reset_input_buffer()
    value = connection.readline().decode().strip()
    print(f"[INFO] Valor leído desde Arduino: {value}")
    return value

def registrar_lectura(valor, estado):
    url = "http://localhost:3000/api/v1/lectura"
    headers = {"Content-Type": "application/json"}
    body = {
        "valor": valor,
        "estado": estado
    }

    try:
        response = requests.post(url, data=json.dumps(body), headers=headers, verify=False)
        print(response.json())
    except requests.RequestException as err:
        print(f"Error al realizar la solicitud: {err}")

def escribir_valor(conexion, valor):
    try:
        valor = int(valor)
        if valor > 35:
            conexion.write(bytes([3]))
            print(f"[ACCION] Valor menor o igual a 15: Enviando byte 3")
            registrar_lectura(valor, "Actuador al 1%")
        elif valor > 15:
            conexion.write(bytes([63]))
            print(f"[ACCION] Valor entre 16 y 35: Enviando byte 63")
            registrar_lectura(valor, "Actuador al 25%")
        else:
            conexion.write(bytes([255]))
            print(f"[ACCION] Valor mayor a 35: Enviando byte 255")
            registrar_lectura(valor, "Actuador al 100%")
    except ValueError:
        print(f"[ERROR] Valor no numérico recibido: '{valor}'")

def menu():
    print("\n[MENU] Sistema de Iluminación")
    print("1. Iniciar el sistema")
    print("2. Salir")
    return input("Seleccione una opción: ")

if __name__ == '__main__':
    opcion = menu()
    if opcion == 1:
        try:
            print("[INFO] Iniciando conexión con Arduino...")
            arduino = conn.Serial(port="COM5", baudrate=9600, timeout=1)
            print("[INFO] Conexión establecida en el puerto COM5")

            while True:
                value = leer_valor(arduino)
                escribir_valor(arduino, value)
                print("[INFO] Esperando 10 segundos para la siguiente lectura...")
                tm.sleep(10)

        except KeyboardInterrupt:
            print("\n[INFO] Desconectando...")
            arduino.close()
            print("[INFO] Conexión cerrada")
        except conn.SerialException as e:
            print(f"[ERROR] No se pudo conectar con el Arduino: {e}")
        except Exception as e:
            print(f"[ERROR] Error inesperado: {e}")
    elif opcion == "2":
        print("[INFO] Saliendo del sistema...")
    else:
        print("[ERROR] Opción no válida")