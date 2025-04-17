from Unidad_3.Python.Problema import SatisfaccionUsuario as s_user
from Unidad_3.Python.Problema import ComodidadConsumoEnergia as s_energia

def calcula_ganancia(alfa, beta, criterios, v_actuales, v_optimizados):
    objSatisfacion = s_user.satisfaccion(criterios)
    satisfaccion_usuario = objSatisfacion.calcula_satisfaccion(v_optimizados)
    ganancia_satisfaccion = objSatisfacion.calcula_ganancia_satisfaccion(satisfaccion_usuario)
    # print(f'Ganancia Satisfacción: {ganancia_satisfaccion}')

    objEnergia = s_energia.energia(criterios)
    satisfaccion_energia = objEnergia.calcula_energia(v_optimizados, v_actuales)
    ganacia_energia = objEnergia.calcula_ganancia_energia(satisfaccion_energia)
    # print(f'Ganancia Energia: {ganacia_energia}')

    ganancia_solucion = alfa * ganancia_satisfaccion + beta * ganacia_energia
    return ganancia_solucion

if __name__ == '__main__':
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

    # Si alfa > beta, se inclina por satisfaccion usurio; si alfa < beta, se inclina por el consumo
    # No recuerdo jeje
    alfa = 0.5
    beta = 0.5

    ganancia_modelo = calcula_ganancia(alfa, beta, prefServicios, valoresActuales, valoresOptimizados)
    print(f'Ganancia del modelo: {ganancia_modelo}')
