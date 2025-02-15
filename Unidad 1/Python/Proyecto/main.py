import AlgoritmoGenetico as ag
import LeerCSV as rcsv
import copy

if __name__ == '__main__':
    data = rcsv.leerCSV('valoresProyecto.csv', ',')
    n = 1000  # Tamaño de población
    m = 6  # Tamaño de solución
    t = 5  # Probabilidad de Mutación
    obj = ag.AlgoritmoGenetico(n, m, t)
    problemas = {
        'minimizar': [0, 1023, 0], # [minimo, maximo, optimo]
        'one_max': [0, 1, 6],
        'valor_absoluto': [0, 1023, 0]
    }

    print('Poblacion:', n)

    for key, (gMin, gMax, opt) in problemas.items():
        iteraciones = 500  # Total de iterciones
        bestGlobal = float('-inf' if key == 'one_max' else '+inf' )  # Óptimo global
        count = 0
        obj.setProblema(key)
        obj.setMinv(gMin)
        obj.setMaxv(gMax)
        print(f'Problema: {key}')

        pob = copy.deepcopy(data)
        if key == 'one_max': pob = rcsv.vector_binario(pob)

        while count < iteraciones:
            count += 1
            padres = obj.get_padres(pob, 500)
            hijos = obj.crear_hijos(padres)
            hijos = obj.mutacion(hijos)
            pob, optActual = obj.seleccion(pob, hijos)

            if key == 'one_max':
                bestGlobal = optActual if optActual > bestGlobal else bestGlobal
                if optActual == opt: break
            else:
                bestGlobal = optActual if optActual < bestGlobal else bestGlobal
                if optActual == opt: break

        print(f'Best solucion: {pob[0]}, fo = {bestGlobal}')
        print('Iteraciones:', count, '\n')
