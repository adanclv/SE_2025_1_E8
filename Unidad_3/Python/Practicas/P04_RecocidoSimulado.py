import random as rand
import math
from Unidad_3.Python.Problema.FuncionObjetivo import calcula_ganancia as fo_calcula_ganancia
from Unidad_3.Python.Practicas.configs import ALFA, BETA
from Unidad_3.Python.Practicas.utils import crear_solucion_inicial, genera_vecina

def mainAL(pref_servicios, valores_actuales):
    T = 1000 # Seleccionar temperatura inicial T0 > 0
    alfa = 0.8 # Seleccionar una función de reducción de la temperatura
    max_it_local = 1000
    it_local = 0

    solucion_temp = crear_solucion_inicial(pref_servicios)
    best_solucion = solucion_temp.copy()
    best_vo = fo_calcula_ganancia(ALFA, BETA, pref_servicios, valores_actuales, solucion_temp)

    better_solucion = solucion_temp.copy()
    better_vo = fo_calcula_ganancia(ALFA, BETA, pref_servicios, valores_actuales, solucion_temp)

    print(f'Solución inicial: {solucion_temp} - Best vo: {best_vo}')

    while T > 1:  # Umbral
        it_local = 0
        while it_local < max_it_local:  # busqueda local
            solucion_temp = genera_vecina(pref_servicios, solucion_temp)
            fo_temp = fo_calcula_ganancia(ALFA, BETA, pref_servicios, valores_actuales, solucion_temp)

            delta_f = fo_temp - better_vo

            if delta_f < 0:
                better_vo = fo_temp
                better_solucion = solucion_temp.copy()
            else:
                t = rand.random()
                compare = math.pow(math.e, delta_f / T)
                if t < compare:
                    better_vo = fo_temp
                    better_solucion = solucion_temp.copy()

            it_local += 1
        if better_vo > best_vo:
            best_vo = better_vo
            best_solucion = better_solucion.copy()
            # print(f"Best solución: {best_solucion} - best vo: {best_vo}")
        T *= alfa

    return best_solucion, best_vo

if __name__ == "__main__":
    prefServicios = {  # 0 = minimizacion -- 1 = maximizacion
        "temperatura": [20, 28, 0, 0.4, 8],
        "humedad": [40, 80, 0, 0.2, 3],
        "ruido": [60, 120, 0, 0.1, 1],
        "int_luminosa": [400, 900, 1, 0.3, 5]
    }
    valoresActuales = {
        "temperatura": 31,
        "humedad": 78,
        "ruido": 140,
        "int_luminosa": 100
    }

    best_solucion, best_vo = mainAL(prefServicios, valoresActuales)
    print(f'Best solucion: {best_solucion} - Best vo: {best_vo}', end='\n\n')

    #soft and hard constrainst