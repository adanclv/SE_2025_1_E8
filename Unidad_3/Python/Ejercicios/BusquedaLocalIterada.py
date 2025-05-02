# 04 marzo
import random as rand

minimo = -10
maximo = 10
rand.seed(5)
n = 5

def funcion_objetivo(solucion):
    fo = sum(s**2 for s in solucion)
    return fo

def vecindario(solucion):
    new_solucion = solucion[:]
    index = rand.randint(0, n - 1)
    new_solucion[index] = rand.randint(minimo, maximo)
    return new_solucion

def perturbacion(solucion): # modificación brusca
    new_solucion = solucion[:]
    index1 = rand.randint(0, n - 1)
    index2 = rand.randint(0, n - 1)
    while index2 == index1:
        index2 = rand.randint(0, n - 1)
    new_solucion[index1] = rand.randint(minimo, maximo)
    new_solucion[index2] = rand.randint(minimo, maximo)
    return new_solucion

def perturbacion2(solucion):
    new_solucion = solucion[:]
    num = rand.randint(minimo, maximo)
    while num == 0:
        num = rand.randint(minimo, maximo)
    new_solucion = [s%num for s in new_solucion]
    return new_solucion


if __name__ == '__main__':
    solucion_inicial = [rand.randint(minimo, maximo) for i in range(n)]
    best_solucion = solucion_inicial.copy()
    best_vo = funcion_objetivo(solucion_inicial)
    it_ils = 100
    it = 1000
    print(f'Solución inicial: {solucion_inicial}')
    print(f'Best vo: {best_vo}')

    while it_ils > 0:
        while it > 0:
            n_solucion = vecindario(solucion_inicial)
            vn_solucion = funcion_objetivo(n_solucion)

            if vn_solucion < best_vo:
                best_vo = vn_solucion
                best_solucion = n_solucion
            it -= 1
            solucion_inicial = n_solucion.copy()
        solucion_inicial = perturbacion(solucion_inicial)
        vn_solucion = funcion_objetivo(solucion_inicial)

        if vn_solucion < best_vo:
            best_vo = vn_solucion
            best_solucion = solucion_inicial
        it_ils -= 1
        it = 1000

    print(f'Best Solución: {best_solucion}')
    print(f'Best valor: {best_vo}')