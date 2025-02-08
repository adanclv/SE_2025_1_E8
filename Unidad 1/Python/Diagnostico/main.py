import operaciones as op
import pandas as pd

if __name__ == '__main__':
    n = 100
    m = 100

    # vector = op.crear_vector(n)

    # vo = op.calcular_valor_objetivo(vector)

    soluciones = op.crear_matriz(m, n)
    #totP = op.get_numero(m)
    padres = op.torneo_binario(soluciones, 50)
    hijos = op.cruza_en_un_punto(padres, n)
    hijos = op.mutacion(hijos, 50)

    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', 1000)
    pd.set_option('display.colheader_justify', 'center')
    hijos = pd.DataFrame(hijos)

    print(hijos)