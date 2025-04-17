import random as rand
from Unidad_3.Python.Problema.FuncionObjetivo import calcula_ganancia as fo_calcula_ganancia
from Unidad_3.Python.Practicas.configs import ALFA, BETA

def get_random_value(pref):
    minimo, maximo, *_ = pref
    valor = rand.randint(minimo, maximo)
    return valor

def crea_solucion(pref_servicios):
    solucion = {
        key: get_random_value(pref_servicios[key]) for key in pref_servicios.keys()
    }
    return solucion

def genera_vecina(pref, solucion, lista_tabu):
    new_solucion = solucion.copy()
    idx_servicio = rand.randint(0, len(pref) - 1)
    while idx_servicio in lista_tabu:
        idx_servicio = rand.randint(0, len(pref) - 1)
    key = list(pref.keys())[idx_servicio]
    new_solucion[key] = get_random_value(pref[key])
    return new_solucion, idx_servicio

def perturbacion(pref_servicios, solucion, lista_tabu):
    keys = list(pref_servicios.keys())
    new_solucion = solucion.copy()

    index1 = rand.randint(0, len(keys) - 1)
    while index1 in lista_tabu:
        index1 = rand.randint(0, len(keys) - 1)
    index2 = index1  ####
    while index2 == index1 and index2 in lista_tabu:
        index2 = rand.randint(0, len(keys) - 1)

    new_valor1 = get_random_value(pref_servicios[keys[index1]])
    new_valor2 = get_random_value(pref_servicios[keys[index2]])

    new_solucion[keys[index1]] = new_valor1
    new_solucion[keys[index2]] = new_valor2

    return new_solucion, index1, index2

def mainTS(pref_servicios, valores_actuales):
    max_it_ils = 50  # iterated local search = ils
    it_ils = 0

    lista_tabu = {}
    tiempos_tabu = 2

    max_it_local = 200
    it_local = 0

    solucion_temp = crea_solucion(pref_servicios)  # S0
    best_solucion = solucion_temp.copy()  # copia de los valores
    best_vo = fo_calcula_ganancia(ALFA, BETA, pref_servicios, valores_actuales, solucion_temp)
    print(f'Solución inicial: {solucion_temp} - Best vo: {best_vo}')

    while it_ils < max_it_ils:  # busqueda local iterada
        while it_local < max_it_local:  # busqueda local
            solucion_temp, idx1 = genera_vecina(pref_servicios, solucion_temp, lista_tabu)
            fo_temp = fo_calcula_ganancia(ALFA, BETA, pref_servicios, valores_actuales, solucion_temp)

            if fo_temp > best_vo:
                best_vo = fo_temp
                best_solucion = solucion_temp.copy()
                # print("nueva best solucion: ", solucion_temp, end="    ")
                # print("vo: ", fo_temp)
                lista_tabu[idx1] = tiempos_tabu + 1

            lista_tabu_temp = lista_tabu.copy()
            for key in lista_tabu.keys():
                lista_tabu_temp[key] -= 1
                if lista_tabu_temp[key] == 0:
                    del lista_tabu_temp[key]
            lista_tabu = lista_tabu_temp
            it_local += 1

        solucion_temp, idx1, idx2 = perturbacion(pref_servicios, solucion_temp, lista_tabu)
        fo_temp = fo_calcula_ganancia(ALFA, BETA, pref_servicios, valores_actuales, solucion_temp)
        if fo_temp > best_vo:
            best_vo = fo_temp
            best_solucion = solucion_temp.copy()
            # print("nueva best solucion2: ", solucion_temp, end="    ")
            # print("vo: ", fo_temp)
            lista_tabu[idx1] = tiempos_tabu + 1
            lista_tabu[idx2] = tiempos_tabu + 1

        lista_tabu_temp = lista_tabu.copy()
        for key in lista_tabu.keys():
            lista_tabu_temp[key] -= 1
            if lista_tabu_temp[key] == 0:
                del lista_tabu_temp[key]
        lista_tabu = lista_tabu_temp
        it_ils += 1

    # print("mejor solucion: ", best_solucion)
    # print("mejor vo: ", best_vo)

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

    best_solucion, best_vo = mainTS(prefServicios, valoresActuales)
    print(f'Best solucion: {best_solucion} - Best vo: {best_vo}')
