from datetime import datetime
import time as tm
import serial as conn

intervalo = 5 * 60  # minutos
nolectura = 1 # lectura en la que va
maxecturas = 144 # hasta donde llega

arduino = conn.Serial(port="COM6", baudrate=9600, timeout=1)

with open("../Archivos/lecturaFotoS4.csv", "w") as archivo:
    archivo.write("No.Lectura,Valor,Fecha,Hora\n")

    while nolectura <= maxecturas:
        tm.sleep(intervalo)
        arduino.reset_input_buffer()  # Limpiar el buffer de entrada y solo se lea el dato mas reciente enviado por el arduino
        linea = arduino.readline().decode().strip()

        fecha = datetime.today().strftime("%Y-%m-%d")
        hora = datetime.today().strftime("%H:%M:%S")

        archivo.write(f"{nolectura},{linea},{fecha},{hora}\n")
        print(f"Lectura: {nolectura}, Valor:{linea}, Fecha: {fecha}, Hora:{hora}")
        nolectura += 1

arduino.close()