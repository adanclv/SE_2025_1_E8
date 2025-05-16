import math
import os
import pandas as pd

def calcular_IQR(data):
    new_data = sorted(data)
    posQ1 = 1 * (len(new_data) - 1) / 4 + 1
    posQ3 = 3 * (len(new_data) - 1) / 4 + 1

    p_decimal, p_entera = math.modf(posQ1)
    p_entera = int(p_entera)
    Q1 = new_data[p_entera-1] + p_decimal * (new_data[p_entera] - new_data[p_entera-1])

    p_decimal, p_entera = math.modf(posQ3)
    p_entera = int(p_entera)
    Q3 = new_data[p_entera-1] + p_decimal * (new_data[p_entera] - new_data[p_entera-1])

    IQR = Q3 - Q1
    # whiskers = 1.5 # tolerancia
    # lower_limit = Q1 - whiskers * IQR
    # upper_limit = Q3 + whiskers * IQR

    return IQR

if __name__ == "__main__":
    path_mh = "../Archivos/ResultadosMH/"
    path_iqr = "../Archivos/ResultadosMH_IQR/"
    files = os.listdir(path_mh)
    for file in files:
        rows = list()
        contenido = pd.read_csv(path_mh + file)
        h = contenido['h'][0]
        grupos = contenido.groupby('va')
        for va_grupo, grupo in grupos:
            IQR = calcular_IQR(grupo['g'])
            rows.append([h, va_grupo, IQR])
        df = pd.DataFrame(rows, columns=['h', 'va', 'iqr'])
        df.to_csv(f'{path_iqr + file[:file.index('.')]}_IQR.csv', index=False)
