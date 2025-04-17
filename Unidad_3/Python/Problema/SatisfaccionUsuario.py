class satisfaccion:
    def __init__(self, preferencias): # [s1, s2, s3, s4]
        self.preferencias = preferencias
        self.vector = []

    def actualiza_vector(self, vector):
        self.vector = vector
        ##valida vector

    def calcula_satisfaccion(self, v_optimizados): # [v1, v2, v3, v4]
        self.actualiza_vector(v_optimizados) ###

        satisfaccion = []
        for key, vo in v_optimizados.items():
            vmin, vmax, problema, peso, *_ = self.preferencias[key]
            if problema == 0:
                temp = self.calcula_satisfaccion_minimizacion(vo, vmin, vmax)
            else:
                temp = self.calcula_satisfaccion_maximizacion(vo, vmin, vmax)
            temp *= peso
            satisfaccion.append(temp)

        return satisfaccion

    def calcula_satisfaccion_minimizacion(self, valor, vmin, vmax):
        xnew = (vmax - valor) / (vmax - vmin)
        return xnew

    def calcula_satisfaccion_maximizacion(self, valor, vmin, vmax):
        xnew = 1 - (vmax - valor) / (vmax - vmin)
        return xnew

    def calcula_ganancia_satisfaccion(self, satisfaccion):
        ganancia = sum(satisfaccion)
        return round(ganancia, 4)

if __name__ == "__main__":
    prefServicios = { # 0 = minimizacion -- 1 = maximizacion
        "temperatura":[20, 28, 0, 0.4],
        "humedad":[40, 80, 0, 0.2],
        "ruido":[60, 120, 0, 0.1],
        "int_luminosa":[400,900, 1, 0.3]
    }
    #[Mínimo, Máximo, Problema, Peso]

    # VALORES OPTIMIZADOS... RECOMENDACION...
    valoresOptimizados = {
        "temperatura": 20,
        "humedad": 70,
        "ruido": 95,
        "int_luminosa": 600
    }

    satis = satisfaccion(prefServicios)
    satisfaccion = satis.calcula_satisfaccion(valoresOptimizados)
    ganancia = satis.calcula_ganancia_satisfaccion(satisfaccion)
    print("Ganancia: ", ganancia)

    # MEJORES VALORES OPTIMIZADOS
    # valoresOptimizados = [20, 40, 60, 900]
    # satisfaccion = calcula_satisfaccion(prefServicios, valoresOptimizados)
    # ganancia = calcula_ganancia_satisfaccion(satisfaccion, pesosPreferencias)
    # print("Ganancia: ", ganancia)

    # PEORES VALORES OPTIMIZADOS
    # valoresOptimizados = [28, 80, 120, 400]
    # satisfaccion = calcula_satisfaccion(prefServicios, valoresOptimizados)
    # ganancia = calcula_ganancia_satisfaccion(satisfaccion, pesosPreferencias)
    # print("Ganancia: ", ganancia)