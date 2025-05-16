import pandas as pd
from Unidad_3.Python.Practicas.P01_BusquedaLocal import mainLS as LS
from Unidad_3.Python.Practicas.P02_BusquedaLocalIterada import mainILS as ILS
from Unidad_3.Python.Practicas.P03_BusquedaTabu import mainTS as TS
from Unidad_3.Python.Practicas.P04_RecocidoSimulado import mainAL as AL
from Unidad_3.Python.Practicas.P05_AlgoritmoGentico import mainGA as GA
from configs import preferencias_servicios

def cargar_valores(archivo):
    with open(archivo, 'r') as file:
        n = 0
        header = file.readline().strip().split(',')
        valores = {key: [] for key in header}
        for row in file:
            n += 1
            row = row.strip().split(',')
            for i in range(len(row)):
                valores[header[i]].append(int(row[i]))
    return valores, n

if __name__ == '__main__':
    valores_actuales, n = cargar_valores('../Archivos/valores_actuales.csv')
    mh = {
        # 'LS': LS, # ✅
        # 'ILS': ILS, # ✅
        # 'TS': TS, # ✅
        # 'AL': AL, # ✅
        # 'GA': GA, # ✅
    }
    for key, func in mh.items():
        row = list()
        for i in range(n):
            va = {key: valores_actuales[key][i] for key in valores_actuales.keys()}
            for j in range(30):
                best_solucion, best_vo = func(preferencias_servicios, va)
                row.append([key, j+1, va, best_solucion, round(best_vo, 5)])
                print(f'i: {i+1} - j: {j+1} - Best solucion: {best_solucion} - Best vo: {best_vo}')

        df = pd.DataFrame(row)
        df.columns = ["h", "no", "va", "vo", "g"]
        # df.to_csv(f'../Archivos/ResultsMH/Tabla_{key}.csv', index=False)
        # print(df)
