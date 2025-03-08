# 03 marzo
import random as rand

minimo = -10
maximo = 10
n = 5

def funcion_objetivo(solucion):
    fo = sum(s**2 for s in solucion)
    return fo

def vecindario(solucion, index):
    new_solucion = solucion[:]
    new_solucion[index] = rand.randint(minimo, maximo)
    return new_solucion


if __name__ == '__main__':
    solucion_inicial = [rand.randint(minimo, maximo) for i in range(n)]
    best_solucion = solucion_inicial.copy()
    best_vo = funcion_objetivo(solucion_inicial)
    it = 100
    print(f'Solución inicial: {solucion_inicial}')
    print(f'Best vo: {best_vo}')

    while it > 0 and best_vo != 0:
        n_solucion = vecindario(solucion_inicial[:], rand.randint(0, n - 1))
        vn_solucion = funcion_objetivo(n_solucion)

        if vn_solucion < best_vo:
            best_vo = vn_solucion
            best_solucion = n_solucion
        solucion_inicial = n_solucion
        it -= 1

    print(f'Best Solución: {best_solucion}')
    print(f'Best valor: {best_vo}')