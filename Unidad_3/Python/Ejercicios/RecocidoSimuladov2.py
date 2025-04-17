import random as rand
import math

minimo = -10
maximo = 10
n = 5

def funcion_objetivo(solucion):
    fo = sum(s ** 2 for s in solucion)
    return fo

def vecindario(solucion, index):
    new_solucion = solucion[:]
    new_solucion[index] = rand.randint(minimo, maximo)
    return new_solucion

if __name__ == '__main__':
    T = 100
    umbral = 0.05
    it = 100
    alfa = 0.999

    solucion_inicial = [rand.randint(minimo, maximo) for i in range(n)]
    best_solucion = solucion_inicial[:]
    best_vo = funcion_objetivo(best_solucion)

    continuar = True
    while continuar:
        aux_solucion = best_solucion[:]
        temp_solucion = best_solucion[:]
        temp_vo = funcion_objetivo(temp_solucion)

        for i in range(it):
            aux_solucion = vecindario(aux_solucion, rand.randint(0, n - 1))
            aux_vo = funcion_objetivo(aux_solucion)
            dif = aux_vo - temp_vo
            if dif < 0:
                temp_solucion = aux_solucion[:]
                temp_vo = aux_vo
            else:
                index = rand.uniform(0, 1)
                if index < math.exp(dif / T):
                    temp_solucion = aux_solucion[:]
            T *= alfa
        if temp_vo < best_vo:
            best_solucion = temp_solucion[:]
            best_vo = temp_vo
        print(f'Solución: {best_solucion} - Best vo: {best_vo}')
        if T < umbral: continuar = False