import random as rand
from Unidad_3.Python.Problema.FuncionObjetivo import calcula_ganancia as fo_calcula_ganancia
from Unidad_3.Python.Practicas.configs import ALFA, BETA

def get_random_value(pref):
    minimo, maximo, *_ = pref
    valor = rand.randint(minimo, maximo)
    return valor

def crea_solucion(prefServicios):
    solucion_inicial = {
        key: get_random_value(prefServicios[key]) for key in prefServicios.keys()
    }
    return solucion_inicial

def genera_vecina(pref, solucion):
    new_solucion = solucion.copy()
    idx_servicio = rand.randint(0, len(pref) - 1)
    key = list(pref.keys())[idx_servicio]
    new_solucion[key] = get_random_value(pref[key])
    return new_solucion

def perturbacion(pref_servicios, solucion):
    keys = list(pref_servicios.keys())
    new_solucion = solucion.copy()

    index1 = rand.randint(0, len(keys) - 1)
    index2 = index1  ####
    while index2 == index1:
        index2 = rand.randint(0, len(keys) - 1)

    new_valor1 = get_random_value(pref_servicios[keys[index1]])
    new_valor2 = get_random_value(pref_servicios[keys[index2]])

    new_solucion[keys[index1]] = new_valor1
    new_solucion[keys[index2]] = new_valor2

    return new_solucion

'''def perturbacion2(solucion):
    new_solucion = solucion.copy()
    num = rand.randint(minimo, maximo)
    while num == 0:
        num = rand.randint(minimo, maximo)
    new_solucion = [s%num for s in new_solucion]
    return new_solucion'''

def mainILS(pref_servicios, valores_actuales):
    max_it_ils = 50
    it_ils = 0

    max_it_local = 200
    it_local = 0

    solucion_temp = crea_solucion(pref_servicios)
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
