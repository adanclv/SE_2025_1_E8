import random as rand

def genera_vecina(pref, solucion):
    new_solucion = solucion.copy()
    idx_servicio = rand.randint(0, len(pref) - 1)
    key = list(pref.keys())[idx_servicio]
    new_solucion[key] = get_random_value(pref[key])
    return new_solucion

def get_random_value(pref):
    minimo, maximo, *_ = pref
    valor = rand.randint(minimo, maximo)
    return valor

def crear_solucion_inicial(prefServicios):
    solucion_inicial = {
        key: get_random_value(prefServicios[key]) for key in prefServicios.keys()
    }
    return solucion_inicial

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
