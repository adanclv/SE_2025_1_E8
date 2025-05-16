class Energia:
    def __init__(self, preferencias):
        self.minimo = preferencias.minimo
        self.maximo = preferencias.maximo
        self.problema = preferencias.problema
        self.peso = preferencias.peso
        self.costo = preferencias.costo
        self.valor_actual = None
        self.valor_optimizado = None

    def set_valor_actual(self, valor_actual):
        self.valor_actual = valor_actual

    def set_valor_optimizado(self, valor_optimizado):
        self.valor_optimizado = valor_optimizado

    def calcula_energia(self, valor_actual, valor_optimizado):
        self.set_valor_actual(valor_actual)
        self.set_valor_optimizado(valor_optimizado)
        resultado_energia = 1
        if self.problema == 'minimizacion':
            if self.valor_actual >= self.minimo:
                eo = self.calcula_satisfaccion_energia_min(self.valor_optimizado)
                emin = self.calcula_satisfaccion_energia_min(self.maximo)
                emax = self.calcula_satisfaccion_energia_min(self.minimo)
                resultado_energia = self.normalizar(eo, emin, emax)
        else:
            if self.valor_actual <= self.maximo:
                eo = self.calcula_satisfaccion_energia_max(self.valor_optimizado)
                emin = self.calcula_satisfaccion_energia_max(self.minimo)
                emax = self.calcula_satisfaccion_energia_max(self.maximo)
                resultado_energia = self.normalizar(eo, emin, emax)
        return resultado_energia

    def calcula_satisfaccion_energia_min(self, valor):
        resultado = 0
        if self.valor_actual >= valor:
            resultado = self.costo + self.costo * (self.valor_actual - valor)
        return resultado

    def calcula_satisfaccion_energia_max(self, valor):
        resultado = 0
        if self.valor_actual <= valor:
            resultado = self.costo + self.costo * (valor - self.valor_actual)
        return resultado

    def normalizar(self, eo, emin, emax):
        resultado_normalizado = 1 - (eo - emin) / (emax - emin)
        return resultado_normalizado

    def calcula_ganancia_energia(self, resultado_consumo):
        consumo_total = resultado_consumo * self.peso
        return consumo_total
