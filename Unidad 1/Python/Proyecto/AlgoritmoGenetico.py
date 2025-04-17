import random as rand

class AlgoritmoGenetico:
    def __init__(self, n, m, t):
        self.problema = ''
        self.minv = 0
        self.maxv = 0
        self.n = n
        self.m = m
        self.t = t

    def setMinv(self, newMin):
        self.minv = newMin

    def setMaxv(self, newMax):
        self.maxv = newMax

    def setProblema(self, newProblema):
        self.problema = newProblema

    def funcion_objetivo(self, solucion):
        if self.problema == 'valor_absoluto':
            return sum(solucion)
        return sum([s ** 2 for s in solucion])

    def get_padres(self, poblacion, totP): # torneo binario
        padres = list()
        for i in range(totP):
            p1 = rand.randint(0, len(poblacion) - 1)
            p2 = rand.randint(0, len(poblacion) - 1)

            while p1 == p2:
                p2 = rand.randint(0, len(poblacion) - 1)

            fo_p1 = self.funcion_objetivo(poblacion[p1])
            fo_p2 = self.funcion_objetivo(poblacion[p2])

            padres.append(poblacion[p1 if fo_p1 < fo_p2 else p2])
        return padres

    def crear_hijos(self, padres): # cruza en un punto
        hijos = list([0 for x in range(self.m)] for y in range(len(padres)))
        for i in range(0, len(padres), 2):
            r = rand.randint(0, self.m)  # m-1?
            hijos[i] = padres[i][:r] + padres[i + 1][r:]  # hijo 1
            hijos[i + 1] = padres[i + 1][:r] + padres[i][r:]  # hijo 2
        return hijos

    def mutacion(self, hijos):
        for hijo in hijos:
            for i in range(len(hijo)):
                r = rand.randint(0, 100)
                if r < self.t:
                    hijo[i] = rand.randint(self.minv, self.maxv)
        return hijos

    def seleccion(self, poblacion, hijos):
        temp = poblacion + hijos
        for t in temp:
            t.append(self.funcion_objetivo(t))

        temp.sort(key=lambda x: x[-1])
        if self.problema == 'one_max':
            temp.reverse()
        newPob = [solucion[:-1] for solucion in temp[:self.n]]
        return newPob, temp[0][-1]
