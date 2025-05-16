from Unidad_3.Python.Problema.FuncionObjetivo import calcula_ganancia as fo_calcula_ganancia
from Unidad_3.Python.Practicas.configs import ALFA, BETA
from Unidad_3.Python.Practicas.utils import crear_solucion_inicial, genera_vecina, perturbacion

def mainILS(pref_servicios, valores_actuales):
    max_it_ils = 50
    it_ils = 0

    max_it_local = 200
    it_local = 0

    solucion_temp = crear_solucion_inicial(pref_servicios)
    best_solucion = solucion_temp.copy()
    best_vo = fo_calcula_ganancia(ALFA, BETA, pref_servicios, valores_actuales, solucion_temp)
    print(f'Solución inicial: {solucion_temp} - Best vo: {best_vo}')

    while it_ils < max_it_ils:  # busqueda local iterada
        it_local = 0
        while it_local < max_it_local:  # busqueda local
            solucion_temp = genera_vecina(pref_servicios, solucion_temp)
            fo_temp = fo_calcula_ganancia(ALFA, BETA, pref_servicios, valores_actuales, solucion_temp)

            if fo_temp > best_vo:
                best_vo = fo_temp
                best_solucion = solucion_temp.copy()
                # print("nueva best solucion: ", solucion_temp, end="    ")
                # print("vo: ", fo_temp)
            it_local += 1

        solucion_temp = perturbacion(pref_servicios, solucion_temp)
        fo_temp = fo_calcula_ganancia(ALFA, BETA, pref_servicios, valores_actuales, solucion_temp)
        if fo_temp > best_vo:
            best_vo = fo_temp
            best_solucion = solucion_temp.copy()
            # print("Pertur best solucion: ", solucion_temp, end="    ")
            # print("vo: ", fo_temp)
        it_ils += 1

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

    for i in range(30):
        print(i)
        best_solucion, best_vo = mainILS(prefServicios, valoresActuales)
        print(f'Best solucion: {best_solucion} - Best vo: {best_vo}')
