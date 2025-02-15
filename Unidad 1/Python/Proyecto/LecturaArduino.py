import serial as conn


if __name__ == '__main__':
    arduino = conn.Serial(port="COM5", baudrate=9600, timeout=1)
    datos = list()
    n = 1000

    while len(datos) < n:
        serialMonitor = arduino.readline().decode().strip()
        if not serialMonitor: continue
        serialMonitor = serialMonitor[1:-1]
        valores = serialMonitor.split('-')
        datos.append(valores)
        print(len(datos))

    arduino.close()

    with open('valoresProyecto.csv', 'w') as file:
        for dato in datos:
            file.write(",".join(dato) + "\n")
