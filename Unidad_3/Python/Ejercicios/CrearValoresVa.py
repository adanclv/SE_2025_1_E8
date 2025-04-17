import random as rand
from Unidad_3.Python.Practicas.configs import preferencias_servicios, multiplicador
import pandas as pd

def get_valor_actual(minimo, maximo, problema, mult):
    if problema == 0:
        new_maximo = int(maximo * mult)
        new_valor = rand.randint(minimo, new_maximo)
    else:
        new_minimo = int(minimo * mult)
        new_valor = rand.randint(new_minimo, maximo)
    return new_valor

if __name__ == '__main__':
    valores = list()
    keys = list(preferencias_servicios.keys())
    for key in keys:
        minimo, maximo, problema, *_ = preferencias_servicios[key]
        mult = multiplicador[key]

        va = [get_valor_actual(minimo, maximo, problema, mult) for _ in range(100)]
        valores.append(va)

    df = pd.DataFrame(valores).T
    df.columns = keys
    # df.to_csv("../Archivos/valores_actuales.csv", index=False)
    print(df)