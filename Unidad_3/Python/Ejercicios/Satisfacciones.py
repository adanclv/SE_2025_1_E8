def get_satisfacciones_totales(vo, minimo, maximo, minimiza):
    satisfaccion = round((maximo - vo) / (maximo - minimo), 3)
    return satisfaccion

def get_costos_min(va, vo, minimo, maximo, costo):
    eo = costo + costo * (va - vo) if va > vo else 0
    emin = costo + costo * (va - maximo) if va >= maximo else 0
    emax = costo + costo * (va - minimo) if va >= minimo else 0
    return eo, emin, emax

def get_costos_max(va, vo, minimo, maximo, costo):
    eo = costo + costo * (vo - va) if va <= vo else 0
    emin = costo + costo * (minimo - va) if va <= minimo else 0
    emax = costo + costo * (maximo - va) if va <= maximo else 0
    return eo, emin, emax

def normalizar(eo, emin, emax):
    consumo = (eo - emin) / (emax - emin)
    return round(1 - consumo, 4)

def funcion_objetivo(alfa, beta, gs, ge):
    fo = gs * alfa + beta * ge
    return fo


if __name__ == '__main__':
    criterios = [[20, 28, True, 0.4, 40], [40, 80, True, 0.2, 25], [60, 120, True, 0.1, 12], [400, 900, False, 0.3, 3]]
    # [Valor minimo, Valor maximo, Minimización, Peso, Costo]
    opciones_vo = [[21, 41, 76, 666], [23, 42, 78, 797], [20, 60, 90, 777]]
    opciones_va = [[24, 46, 85, 700], [21, 55, 70, 500], [26, 58, 112, 888]]

    alfa = 0.8
    beta = 0.2

    for vo, va in zip(opciones_vo, opciones_va):
        niveles_satisfaccion = list()
        consumo = list()
        for i in range(len(criterios)):
            minimo, maximo, minimiza, peso, costo = criterios[i]
            satisfaccion = get_satisfacciones_totales(vo[i], minimo, maximo, minimiza)
            if minimiza:
                eo, emin, emax = get_costos_min(va[i], vo[i], minimo, maximo, costo)
            else:
                eo, emin, emax = get_costos_max(va[i], vo[i], minimo, maximo, costo)
                satisfaccion = 1 - satisfaccion
            niveles_satisfaccion.append(satisfaccion)
            consumo.append(normalizar(eo, emin, emax))
        # print(f"Consumo: {consumo}")

        ganancia_satisfaccion = sum(niveles_satisfaccion[i] * criterios[i][3] for i in range(len(vo)))
        print(f'Vo: {niveles_satisfaccion} - Ganancia: {ganancia_satisfaccion}')

        ganancia_consumo = sum(consumo[i] * criterios[i][3] for i in range(len(va)))
        print(f'Va: {consumo} - Ganancia: {ganancia_consumo}')

        fo = funcion_objetivo(alfa, beta, ganancia_satisfaccion, ganancia_consumo)
        print(f'Fo: {fo}')
