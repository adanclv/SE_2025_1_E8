from datetime import datetime
import time as tm
import serial as conn

intervalo = 5 * 60  # minutos
no_lectura = 1 # lectura en la que va
max_lecturas = 144 # hasta donde llega
semana = 7 # cambiar cada semana

arduino = conn.Serial(port="COM5", baudrate=9600, timeout=1)

with open(f"../Archivos/lecturaFotoS{semana}.csv", "w") as archivo:
    archivo.write("No.Lectura,Valor,Fecha,Hora\n")

    while no_lectura <= max_lecturas:
        tm.sleep(intervalo)
        arduino.reset_input_buffer()  # Limpiar el buffer de entrada y solo se lea el dato mas reciente enviado por el arduino
        linea = arduino.readline().decode().strip()

        fecha = datetime.today().strftime("%Y-%m-%d")
        hora = datetime.today().strftime("%H:%M:%S")

        archivo.write(f"{no_lectura},{linea},{fecha},{hora}\n")
        print(f"Lectura: {no_lectura}, Valor:{linea}, Fecha: {fecha}, Hora:{hora}")
        no_lectura += 1

arduino.close()