class Satisfaccion:
    def __init__(self, preferencias):
        self.minimo = preferencias.minimo
        self.maximo = preferencias.maximo
        self.problema = preferencias.problema
        self.peso = preferencias.peso
        self.valor_optimizado = None

    def set_valor_optimizado(self, valor_optimizado):
        self.valor_optimizado = valor_optimizado

    def get_valor_optimizado(self):
        return self.valor_optimizado

    def calcula_satisfaccion(self, valor_optimizado):
        self.set_valor_optimizado(valor_optimizado)
        resultado_satisfaccion = 0
        if self.problema == 'minimizacion':
            resultado_satisfaccion = self.calcula_satisfaccion_minimizacion()
        else:
            resultado_satisfaccion = self.calcula_satisfaccion_maximizacion()

        return resultado_satisfaccion

    def calcula_satisfaccion_minimizacion(self):
        resultado = (self.maximo - self.valor_optimizado) / (self.maximo - self.minimo)
        return resultado

    def calcula_satisfaccion_maximizacion(self):
        resultado = 1 - (self.maximo - self.valor_optimizado) / (self.maximo - self.minimo)
        return resultado

    def ganacia_satisfaccion(self, resultado_satisfaccion):
        satisfaccion_total = resultado_satisfaccion * self.peso
        return satisfaccion_total
