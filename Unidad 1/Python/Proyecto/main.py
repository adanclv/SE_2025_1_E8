import AlgoritmoGenetico as ag

if __name__ == '__main__':
    gMin = -50
    gMax = 50
    n = 100 # Tamaño de población
    m = 6 # Tamaño de solución
    t = 5 # Probabilidad de Mutación
    bestGlobal = float('+inf') # Óptimo global
    iteraciones = 20 # Total de iterciones
    obj = ag.AlgoritmoGenetico(gMin, gMax, n, m, t)
    pob = obj.crear_poblacion()
    count = 0

    while iteraciones > 0:
        count += 1

        iteraciones -= 1
        padres = obj.get_padres(pob, 50)
        hijos = obj.crear_hijos(padres)
        hijos = obj.mutacion(hijos)
        pob, minActual = obj.seleccion(pob, hijos)

        if minActual < bestGlobal:
            bestGlobal = minActual
            iteraciones = 20
    print(f'Best solucion: {pob[0]}, fo = {bestGlobal}')
    print(count)