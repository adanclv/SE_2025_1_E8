def get_satisfacciones_totales(vo, minimo, maximo, minimiza):
    satisfaccion = round((maximo - vo) / (maximo - minimo), 3)
    return satisfaccion if minimiza else 1 - satisfaccion

def get_costos_min(va, vo, minimo, maximo, costo):
    eo = costo + costo * (va - vo) if va > vo else 0
    emin = costo + costo * (va - maximo) if va >= maximo else 0
    emax = costo + costo * (va - minimo) if va >= minimo else 0
    return eo, emin, emax

def get_costos_max(va, vo, minimo, maximo, costo):
    eo = costo + costo * (vo - va) if vo > va else 0
    emin = costo + costo * (va - maximo) if va >= maximo else 0
    emax = costo + costo * (va - minimo) if va >= minimo else 0
    # Falta editar

    return eo, emin, emax

def normalizar(eo, emin, emax):
    consumo = (emax - eo) / (emax - emin)
    return round(1 - consumo, 4)


if __name__ == '__main__':
    criterios = [[20, 28, True, 0.4, 40], [40, 80, True, 0.2, 25], [60, 120, True, 0.1, 12], [400, 900, False, 0.3, 3]]
    # [Valor minimo, Valor maximo, Minimización, Peso, Costo]
    opciones_vo = [[21, 41, 76, 666], [23, 42, 78, 797], [20, 60, 90, 777]]
    opciones_va = [[24, 46, 85, 700], [21, 55, 70, 500], [26, 58, 112, 888]]

    for vo, va in zip(opciones_vo, opciones_va):
        niveles_satisfaccion = list()
        for i in range(len(criterios)):
            minimo, maximo, minimiza, peso, costo = criterios[i]
            niveles_satisfaccion.append(get_satisfacciones_totales(vo[i], minimo, maximo, minimiza))
            eo, emin, emax = get_costos_min(va[i], vo[i], minimo, maximo, costo)
            consumo = normalizar(eo, emin, emax)
            print(f"Consumo: {consumo}")

        ganancia = sum(niveles_satisfaccion[i] * criterios[i][3] for i in range(len(vo)))
        print(f'Vo: {niveles_satisfaccion} - Ganancia: {ganancia}')
