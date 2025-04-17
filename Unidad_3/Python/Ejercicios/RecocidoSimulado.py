# 31 marzo Recocido simulado
import random as rand
import math

minimo = -10
maximo = 10
n = 5

def funcion_objetivo(solucion):
    fo = sum(s**2 for s in solucion)
    return fo

def vecindario(solucion):
    new_solucion = solucion[:]
    index = rand.randint(0, n - 1)
    new_solucion[index] = rand.randint(minimo, maximo)
    return new_solucion

if __name__ == '__main__':
    solucion_inicial = [rand.randint(minimo, maximo) for i in range(n)]
    best_solucion = solucion_inicial.copy()
    best_vo = funcion_objetivo(solucion_inicial)

    better_solucion = solucion_inicial.copy()
    better_vo = funcion_objetivo(solucion_inicial)
    # Seleccionar temperatura inicial T0 > 0
    T = 1000

    #Seleccionar una función de reducción de la temperatura
    alfa = 0.8

    #Seleccionar un número de iteraciones N
    max_it = 100
    it = 0

    print(f'Solución inicial: {solucion_inicial}')
    print(f'Best vo: {best_vo}')

    while T > 1: # umbral
        it = 0
        while it < max_it:
            n_solucion = vecindario(solucion_inicial)
            vn_solucion = funcion_objetivo(n_solucion)

            delta_f = vn_solucion - better_vo

            if delta_f < 0:
                better_vo = vn_solucion
                better_solucion = n_solucion.copy()
                print(f"Better solución: {better_solucion} - better vo: {better_vo}")
            else:
                t = rand.random()
                compare = math.pow(math.e, delta_f/T)
                if t < compare:
                    better_vo = vn_solucion
                    better_solucion = n_solucion.copy()
                    print(f"SINO: Better solución: {better_solucion} - better vo: {better_vo}")
            it += 1

        if better_vo < best_vo:
            best_vo = better_vo
            best_solucion = better_solucion.copy()
            print(f"Best solución: {best_solucion} - best vo: {best_vo}")
        T *= alfa

    print(f'Best Solución: {best_solucion}')
    print(f'Best valor: {best_vo}')