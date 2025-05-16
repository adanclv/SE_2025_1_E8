import random as rand

minimo = -10
maximo = 10
n = 5
n_pop = 100
n_parents = 50
probabilidad = 5

def crea_solucion():
    solucion = [rand.randint(minimo, maximo) for _ in range(n)]
    return solucion

def funcion_objetivo(solucion):
    fo = sum(s**2 for s in solucion)
    return fo

def crear_poblacion_inicial():
    poblacion_inicial = list()
    for i in range(n_pop):
        solucion = crea_solucion()
        poblacion_inicial.append(solucion)
    return poblacion_inicial

def torneo_binario(poblacion):
    padres = list()
    for i in range(n_parents):
        p1 = rand.randint(0, n_pop - 1)
        p2 = rand.randint(0, n_pop - 1)

        while p1 == p2:
            p2 = rand.randint(0, n_pop - 1)

        fo_p1 = funcion_objetivo(poblacion[p1])
        fo_p2 = funcion_objetivo(poblacion[p2])

        padres.append(poblacion[p1] if fo_p1 > fo_p2 else poblacion[p2])
    return padres

def cruza_en_un_punto(padres): # cruza en un punto
    hijos = list([0 for x in range(n)] for y in range(len(padres)))
    for i in range(0, len(padres), 2):
        r = rand.randint(0, n)
        hijos[i] = padres[i][:r] + padres[i + 1][r:]  # hijo 1
        hijos[i + 1] = padres[i + 1][:r] + padres[i][r:]  # hijo 2
    return hijos

def mutacion(hijos):
    for hijo in hijos:
        for i in range(len(hijo)):
            r = rand.randint(0, 100)
            if r < probabilidad:
                hijo[i] = rand.randint(minimo, maximo)
    return hijos

def seleccion(poblacion, hijos=list()):
    temp = poblacion + hijos
    for t in temp:
        t.append(funcion_objetivo(t))

    temp.sort(key=lambda x: x[-1])
    newPob = [solucion[:-1] for solucion in temp[:n_pop]]
    return newPob, temp[0][-1]

if __name__ == '__main__':
    max_it = 100
    it = 0
    poblacion = crear_poblacion_inicial()
    poblacion, best_global = seleccion(poblacion)
    best_solucion = poblacion[0]
    print('Solucion inicial:', best_solucion)
    print('Best vo:', best_global)
    while it < max_it:
        padres = torneo_binario(poblacion)
        hijos = cruza_en_un_punto(padres)
        hijos = mutacion(hijos)
        poblacion, best_actual = seleccion(poblacion, hijos)
        if best_actual < best_global:
            best_global = best_actual

        it += 1
    best_solucion = poblacion[0]
    print('Solucion inicial:', best_solucion)
    print('Best vo:', best_global)
