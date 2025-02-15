import AlgoritmoGenetico as ag
import LeerCSV as rcsv
# region Minimización
#
#
# if __name__ == '__main__':
#     data = rcsv.leerCSV('valoresProyecto.csv', ',')
#     gMin = 0
#     gMax = 1023
#     n = 200 # Tamaño de población
#     m = 6 # Tamaño de solución
#     t = 5 # Probabilidad de Mutación
#     bestGlobal = float('+inf') # Óptimo global
#     iteraciones = 300 # Total de iterciones
#     # problemas = {
#     #     'minimizar': algo,
#     #     'one_max': algo,
#     #     'valor_absoluto': algo
#     # }
#
#     pob = data
#     obj = ag.AlgoritmoGenetico(gMin, gMax, n, m, t)
#     count = 0
#
#     while iteraciones > 0 and bestGlobal > 0:
#         count += 1
#
#         iteraciones -= 1
#         padres = obj.get_padres(pob, 100)
#         hijos = obj.crear_hijos(padres)
#         hijos = obj.mutacion(hijos)
#         pob, minActual = obj.seleccion(pob, hijos)
#
#         if minActual < bestGlobal:
#             bestGlobal = minActual
#     print(f'Best solucion: {pob[0]}, fo = {bestGlobal}')
#     print('Iteraciones:', count)
# endregion

# region One Max Problem
# if __name__ == '__main__':
#     data = rcsv.leerCSV('valoresProyecto.csv', ',')
#     gMin = 0
#     gMax = 1
#     n = 100 # Tamaño de población
#     m = 4 # Tamaño de solución
#     t = 5 # Probabilidad de Mutación
#     bestGlobal = float('-inf') # Óptimo global
#     iteraciones = 200 # Total de iterciones
#
#     pob = rcsv.vector_binario(data)
#     obj = ag.AlgoritmoGenetico(gMin, gMax, n, m, t)
#     count = 0
#
#     while iteraciones > 0 and bestGlobal < 6:
#         count += 1
#
#         iteraciones -= 1
#         padres = obj.get_padres(pob, 50)
#         hijos = obj.crear_hijos(padres)
#         hijos = obj.mutacion(hijos)
#         pob, maxActual = obj.seleccion(pob, hijos, 2)
#
#         if maxActual > bestGlobal:
#             bestGlobal = maxActual
#     print(iteraciones)
#     print(f'Best solucion: {pob[0]}, fo = {bestGlobal}')
#     print('Iteraciones:', count)
# endregion

# region Valor Absoluto
# if __name__ == '__main__':
#     data = rcsv.leerCSV('valoresProyecto.csv', ',')
#     gMin = 0
#     gMax = 1023
#     n = 200 # Tamaño de población
#     m = 6 # Tamaño de solución
#     t = 5 # Probabilidad de Mutación
#     bestGlobal = float('+inf') # Óptimo global
#     iteraciones = 300 # Total de iterciones
#
#     pob = data.copy()
#     obj = ag.AlgoritmoGenetico(gMin, gMax, n, m, t)
#     count = 0
#
#     while iteraciones > 0 and bestGlobal > 0:
#         count += 1
#
#         iteraciones -= 1
#         padres = obj.get_padres(pob, 100)
#         hijos = obj.crear_hijos(padres)
#         hijos = obj.mutacion(hijos)
#         pob, minActual = obj.seleccion(pob, hijos)
#
#         if minActual < bestGlobal:
#             bestGlobal = minActual
#     print(f'Best solucion: {pob[0]}, fo = {bestGlobal}')
#     print('Iteraciones:', count)
# endregion