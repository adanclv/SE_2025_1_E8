import random as rand
from Unidad_3.Python.Proyecto.procesamiento.funcion_objetivo import calcula_ganancia as fo_calcula_ganancia
from Unidad_3.Python.Proyecto.consts import ALFA, BETA, N_POP, N_PARENTS, PROBABILIDAD_MUTA, ITERACIONES
from Preferencias import Preferencias

class AlgoritmoGenetico:
    def __init__(self, preferencias, valor_actual):
        self.preferencias = preferencias
        self.valor_actual = valor_actual

    def crear_solucion(self):
        solucion = rand.randint(self.preferencias.minimo, self.preferencias.maximo)
        return solucion

    def crear_poblacion_inicial(self):
        poblacion_inicial = [self.crear_solucion() for _ in range(N_POP)]
        return poblacion_inicial

    def torneo_binario(self, poblacion):
        padres = []
        for _ in range(N_PARENTS):
            p1 = rand.randint(0, len(poblacion) - 1)
            p2 = rand.randint(0, len(poblacion) - 1)

            while p1 == p2:
                p2 = rand.randint(0, len(poblacion) - 1)

            fo_p1 = fo_calcula_ganancia(ALFA, BETA, self.preferencias, self.valor_actual, poblacion[p1])
            fo_p2 = fo_calcula_ganancia(ALFA, BETA, self.preferencias, self.valor_actual, poblacion[p2])

            padres.append(poblacion[p1] if fo_p1 > fo_p2 else poblacion[p2])

        return padres

    def cruza_en_un_punto(self, padres):
        hijos = []
        for i in range(0, len(padres), 2):
            if i + 1 >= len(padres):
                break
            r = rand.randint(0, 1)  # Solo hay dos opciones (padre1 o padre2)
            hijo1 = padres[i] if r == 0 else padres[i + 1]
            hijo2 = padres[i + 1] if r == 0 else padres[i]
            hijos.append(hijo1)
            hijos.append(hijo2)
        return hijos

    def mutacion(self, hijos):
        for i in range(len(hijos)):
            if rand.random() < PROBABILIDAD_MUTA:
                hijos[i] = rand.randint(self.preferencias.minimo, self.preferencias.maximo)
        return hijos

    def seleccion(self, poblacion, hijos=list()):
        temp = poblacion + hijos
        temp.sort(
            key=lambda t: fo_calcula_ganancia(ALFA, BETA, self.preferencias, self.valor_actual, t),
            reverse=True
        )
        newPob = temp[:N_POP]
        best_vo = fo_calcula_ganancia(ALFA, BETA, self.preferencias, self.valor_actual, temp[0])
        return newPob, best_vo


def main_GA(preferencias, valor_actual):
    it = 0
    ga = AlgoritmoGenetico(preferencias, valor_actual)
    poblacion = ga.crear_poblacion_inicial()
    poblacion, best_global = ga.seleccion(poblacion)
    best_solucion = poblacion[0]

    # print('Solución inicial:', best_solucion)
    # print('Mejor valor objetivo inicial:', best_global)

    while it < ITERACIONES:
        padres = ga.torneo_binario(poblacion)
        hijos = ga.cruza_en_un_punto(padres)
        hijos = ga.mutacion(hijos)
        poblacion, best_actual = ga.seleccion(poblacion, hijos)

        if best_actual > best_global:
            best_global = best_actual
            best_solucion = poblacion[0]

        it += 1

    # print('Solución final:', best_solucion)
    # print('Mejor valor objetivo final:', best_global)

    return best_solucion

if __name__ == '__main__':
    pref = Preferencias(minimo=100,
                        maximo=600,
                        problema='maximizacion',
                        peso=1,
                        costo=4)
    valor_optimo = main_GA(preferencias=pref, valor_actual=210)
    print('Valor óptimo:', valor_optimo)