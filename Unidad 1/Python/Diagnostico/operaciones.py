import random as rand

gMin = -50
gMax = 50

def crear_vector(n):
    vector = list()
    for i in range(n):
        number = round(rand.uniform(gMin, gMax), 2)
        vector.append(number)

    return vector

def calcular_valor_objetivo(vector):
    vo = 0
    for e in vector:
        vo += e ** 2

    return round(vo, 2)

def crear_matriz(m, n):
    matriz = list()
    for i in range(m):
        a = crear_vector(n)
        matriz.append(a)

    return matriz

def get_numero(m):
    numero = rand.choice(range(2, m, 2))

    return numero


def torneo_binario(matriz, totP):
    P = list()

    for i in range(totP):
        p1 = rand.randint(0, len(matriz) - 1)
        p2 = rand.randint(0, len(matriz) - 1)

        while p1 == p2:
            p2 = rand.randint(0, len(matriz) - 1)

        vo_p1 = calcular_valor_objetivo(matriz[p1])
        vo_p2 = calcular_valor_objetivo(matriz[p2])
        if vo_p1 < vo_p2:
            P.append(matriz[p1])
        else:
            P.append(matriz[p2])

    return P

def cruza_en_un_punto(papis, n):
    h = list([0 for x in range(n)]for y in range(len(papis)))
    for i in range(0, len(papis), 2):
        r = rand.randint(0, n) # n-1?
        h[i] = papis[i][:r] + papis[i + 1][r:] # hijo 1
        h[i + 1] = papis[i + 1][:r] + papis[i][r:] # hijo 2

    return h


def mutacion(hijos, rm):
    for hijo in hijos:
        for i in range(len(hijo)):
            r = rand.randint(0, 100)
            if r > rm:
                hijo[i] = round(rand.uniform(gMin, gMax), 2)

    return hijos
