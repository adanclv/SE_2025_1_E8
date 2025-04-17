import random as rand
from Unidad_3.Python.Problema.FuncionObjetivo import calcula_ganancia as fo_calcula_ganancia
from Unidad_3.Python.Practicas.configs import ALFA, BETA, N_POP, N_PARENTS, N_SERVICIOS, PROBABILIDAD_MUTA

def get_random_value(pref):
    minimo, maximo, *_ = pref
    valor = rand.randint(minimo, maximo)
    return valor

def crear_solucion(pref_servicios):
    solucion = {
        key: get_random_value(pref_servicios[key]) for key in pref_servicios.keys()
    }
    return solucion

def crear_poblacion_inicial(pref_servicios):
    poblacion_inicial = list()
    for i in range(N_POP):
        solucion = crear_solucion(pref_servicios)
        poblacion_inicial.append(solucion)
    return poblacion_inicial

def torneo_binario(pref_servicios, poblacion, valores_actuales):
    padres = list()
    for i in range(N_PARENTS):
        p1 = rand.randint(0, N_POP - 1)
        p2 = rand.randint(0, N_POP - 1)

        while p1 == p2:
            p2 = rand.randint(0, N_POP - 1)

        fo_p1 = fo_calcula_ganancia(ALFA, BETA, pref_servicios, valores_actuales, poblacion[p1])
        fo_p2 = fo_calcula_ganancia(ALFA, BETA, pref_servicios, valores_actuales, poblacion[p2])

        padres.append(poblacion[p1] if fo_p1 > fo_p2 else poblacion[p2])
    return padres

def cruza_en_un_punto(pref_servicios, padres):
    hijos = list()
    keys = list(pref_servicios.keys())
    for i in range(0, N_PARENTS, 2):
        r = rand.randint(0, N_SERVICIOS - 1)
        papi1 = padres[i]
        papi2 = padres[i + 1]
        hijo1 = dict()
        hijo2 = dict()
        for key in keys[:r]:
            hijo1[key] = papi1[key]
            hijo2[key] = papi2[key]
        for key in keys[r:]:
            hijo1[key] = papi2[key]
            hijo2[key] = papi1[key]
        hijos.append(hijo1)
        hijos.append(hijo2)
    return hijos

def mutacion(pref_servicios, hijos):
    new_hijos = hijos.copy()
    for hijo in new_hijos:
        for key in hijo.keys():
            r = rand.randint(0, 100)
            if r < PROBABILIDAD_MUTA:
                hijo[key] = get_random_value(pref_servicios[key])
    return new_hijos

def seleccion(pref_servicios, valores_actuales, poblacion, hijos=list()):
    temp = poblacion.copy() + hijos.copy()
    for e in temp:
        fo = fo_calcula_ganancia(ALFA, BETA, pref_servicios, valores_actuales, e)
        e['fo'] = fo

    new_poblacion = sorted(temp, key=lambda x: x['fo'], reverse=True)
    fo_value = new_poblacion[0]['fo']
    for pob in new_poblacion:
        del pob['fo']

    new_poblacion = new_poblacion[:N_POP]
    return new_poblacion, fo_value

def mainGA(pref_servicios, valores_actuales):
    max_it = 100
    it = 0
    poblacion = crear_poblacion_inicial(pref_servicios)
    poblacion, best_global = seleccion(pref_servicios, valores_actuales, poblacion)
    best_solucion = poblacion[0]
    print(f'Solucion inicial: {best_solucion} - Best vo: {best_global}')
    while it < max_it:
        padres = torneo_binario(pref_servicios, poblacion, valores_actuales)
        hijos = cruza_en_un_punto(pref_servicios, padres)
        hijos = mutacion(pref_servicios, hijos)
        poblacion, best_actual = seleccion(pref_servicios, valores_actuales, poblacion, hijos)
        if best_actual > best_global:
            best_global = best_actual

        it += 1

    best_solucion = poblacion[0]
    return best_solucion, best_global

if __name__ == '__main__':
    pref_servicios = {  # 0 = minimizacion -- 1 = maximizacion
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

    best_solucion, best_global = mainGA(pref_servicios, valoresActuales)
    print(f'Best solucion: {best_solucion} - Best vo: {best_global}')

# Poblacion inicial - Array de dicts ('servicio1': value, ...) ✅
# Torneo binario - Seleccionar padres - Array de dicts ✅
# Cruza en un punto - Tomar dos padres ✅
# Mutación ✅
# Seleccion ✅