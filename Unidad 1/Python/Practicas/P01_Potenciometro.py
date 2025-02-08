import serial as conn
import pandas as pd

def funcion_objetivo(vector):
    vo = 0
    for e in vector:
        vo += e ** 2

    return round(vo, 2)

if __name__ == '__main__':
    arduino = conn.Serial(port="COM5", baudrate=9600, timeout=1)
    n = 10
    valores = list()
    vo = list()

    print('Conectado')

    while len(valores) < n:
        serialMonitor = arduino.readline()
        serialMonitor = serialMonitor.decode().strip()
        if not serialMonitor: continue
        serialMonitor = serialMonitor[1:-1]
        val = serialMonitor.split('-')
        valores.append([float(v) for v in val])

    arduino.close()
    vo = [funcion_objetivo(e) for e in valores]

    valores = pd.DataFrame(valores)
    vo = pd.DataFrame(vo)

    df_completo = pd.DataFrame()
    df_completo = pd.concat([valores, vo], axis=1, ignore_index=True)
    df_completo.to_csv('../Archivos/valores_P1.csv', index=False, header=False)

    print(df_completo)

# [[377. 354. 341. 301.]
#  [317. 324. 327. 310.]
#  [307. 312. 318. 312.]
#  [305. 305. 308. 303.]
#  [297. 297. 299. 297.]
#  [293. 295. 297. 295.]
#  [289. 288. 289. 285.]
#  [282. 283. 284. 282.]
#  [281. 282. 284. 280.]
#  [275. 275. 276. 273.]]
