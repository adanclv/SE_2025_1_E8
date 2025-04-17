import numpy as np


datos = np.array([
    #A1 , A2, A3      = Algoritmo -> A
    [100, 100, 90], #-> IQR de va[0]
    [20, 80, 95], #-> IQR de va[1]
    [80, 100, 75],
    [70, 100, 15],
    [96, 91, 85],
    [90, 95, 90]
])

##
#LAS PRUEBAS POSTHOC TIENEN UTILIDAD SOLO CUANDO EXISTE UNA DIFERENCIA
#ESTADISTICA ENTRE LOS GRUPOS Y SE DESEA CONCOER AL GRUPO O GRUPOS
#QUE SON DIFERENTES
############################################################

from scikit_posthocs import posthoc_conover_friedman
res = posthoc_conover_friedman(datos)
print(res)

############################################################