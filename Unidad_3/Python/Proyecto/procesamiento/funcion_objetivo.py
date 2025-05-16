from Unidad_3.Python.Proyecto.procesamiento.Satisfaccion import Satisfaccion
from Unidad_3.Python.Proyecto.procesamiento.Energia import Energia

def calcula_ganancia(alfa, beta, preferencias, valor_actual, valor_optimizado):
    objSatisfaccion = Satisfaccion(preferencias)
    satisfaccion_usuario = objSatisfaccion.calcula_satisfaccion(valor_optimizado)
    ganancia_satisfaccion = objSatisfaccion.ganacia_satisfaccion(satisfaccion_usuario)
    # print(f'Ganancia Satisfacción: {ganancia_satisfaccion}')

    objEnergia = Energia(preferencias)
    satisfaccion_energia = objEnergia.calcula_energia(valor_actual, valor_optimizado)
    ganancia_energia = objEnergia.calcula_ganancia_energia(satisfaccion_energia)
    # print(f'Ganancia Energia: {ganacia_energia}')

    ganancia_solucion = alfa * ganancia_satisfaccion + beta * ganancia_energia
    return ganancia_solucion