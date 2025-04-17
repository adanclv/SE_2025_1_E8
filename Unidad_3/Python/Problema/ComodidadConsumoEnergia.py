class energia: # Que tan comodo nos encontramos con base en el consumo de energía
    def __init__(self, preferencias_energia):
        self.preferencias_energia = preferencias_energia
        self.vector = []

    def actualiza_vector(self, vector):
        self.vector = vector
        ##valida vector

    def calcula_energia(self, vector_por_aplicar, vector_actuales): # [v1, v2, v3, v4]
        self.actualiza_vector(vector_por_aplicar)

        energia = list()

        for key, vo in vector_por_aplicar.items():
            vmin, vmax, problema, peso, costo = self.preferencias_energia[key]
            va = vector_actuales[key]
            temp = -1
            if problema == 0:
                if va >= vmin:
                    Eo = self.calcula_satisfaccion_energia_min(costo, va, vo)
                    Emin = self.calcula_satisfaccion_energia_min(costo, va, vmax)
                    Emax = self.calcula_satisfaccion_energia_min(costo, va, vmin)
                else: temp = 1
            else:
                if va <= vmax:
                    Eo = self.calcula_satisfaccion_energia_max(costo, va, vo)
                    Emin = self.calcula_satisfaccion_energia_max(costo, va, vmin)
                    Emax = self.calcula_satisfaccion_energia_max(costo, va, vmax)
                else: temp = 1
            if temp != 1: temp = self.normalizar(Eo, Emin, Emax)
            temp = temp * peso
            energia.append(temp)
        return energia

    def calcula_satisfaccion_energia_min(self, costo, va, v):
        valor = 0
        if va >= v:
            valor = costo + costo * (va - v)
        return valor

    def calcula_satisfaccion_energia_max(self, costo, va, v):
        valor = 0
        if va <= v:
            valor = costo + costo * (v - va)
        return valor

    def normalizar(self, eo, emin, emax):
        consumo = 1 - (eo - emin) / (emax - emin)
        return consumo

    def calcula_ganancia_energia(self, satisfaccion):
        ganancia = sum(satisfaccion)
        return round(ganancia, 4)

if __name__ == "__main__":
    prefServicios = {  # 0 = minimizacion -- 1 = maximizacion
        "temperatura": [20, 28, 0, 0.4, 8],
        "humedad": [40, 80, 0, 0.2, 3],
        "ruido": [60, 120, 0, 0.1, 1],
        "int_luminosa": [400, 900, 1, 0.3, 5]
    }
    #[Mínimo, Máximo, Problema, Peso, Costo]

    valoresActuales = {
        "temperatura": 18,
        "humedad": 60,
        "ruido": 90,
        "int_luminosa": 300
    }

    # VALORES OPTIMIZADOS... RECOMENDACION...
    valoresOptimizados = {
        "temperatura": 20,
        "humedad": 70,
        "ruido": 95,
        "int_luminosa": 600
    }

    comodidad_energia = energia(prefServicios)
    satisfaccion_energia = comodidad_energia.calcula_energia(valoresOptimizados, valoresActuales)
    ganancia = comodidad_energia.calcula_ganancia_energia(satisfaccion_energia)
    print(f'Ganancia: {ganancia}')
