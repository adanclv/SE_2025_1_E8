from Unidad_3.Python.Problema.FuncionObjetivo import calcula_ganancia as fo_calcula_ganancia
from Unidad_3.Python.Practicas.configs import ALFA, BETA
from Unidad_3.Python.Practicas.utils import crear_solucion_inicial, genera_vecina

def mainLS(prefServicios, valoresActuales):
    tot_mejoras_buscadas = 10
    tot_iteraciones = 100

    mejorasRealizadas = 0
    iteracionesRealizadas = 0

    solucion_inicial = crear_solucion_inicial(prefServicios)
    best_solucion = solucion_inicial.copy()
    best_vo = fo_calcula_ganancia(ALFA, BETA, prefServicios, valoresActuales, solucion_inicial)
    print(f'Solución inicial: {solucion_inicial} - Best vo: {best_vo}')

    while iteracionesRealizadas < tot_iteraciones and mejorasRealizadas < tot_mejoras_buscadas:
        vo_vecino = genera_vecina(prefServicios, solucion_inicial)
        fo_vecino = fo_calcula_ganancia(ALFA, BETA, prefServicios, valoresActuales, solucion_inicial)

        # print("Ganancia de la Vecina:", fo_vecino)

        if fo_vecino > best_vo:
            best_vo = fo_vecino
            best_solucion = vo_vecino.copy()
            mejorasRealizadas += 1
            iteracionesRealizadas -= 1
        solucion_inicial = vo_vecino
        iteracionesRealizadas += 1

    return best_solucion, best_vo

if __name__ == '__main__':
    prefServicios = {  # 0 = minimización -- 1 = maximización
        "temperatura": [20, 28, 0, 0.4, 8],
        "humedad": [40, 80, 0, 0.2, 3],
        "ruido": [60, 120, 0, 0.1, 1],
        "int_luminosa": [400, 900, 1, 0.3, 5]
    }
    # [Mínimo, Máximo, Problema, Peso, Costo]

    valoresActuales = {
        "temperatura": 18,
        "humedad": 60,
        "ruido": 90,
        "int_luminosa": 300
    }

    # VALORES OPTIMIZADOS... RECOMENDACIÓN...
    valoresOptimizados = {
        "temperatura": 20,
        "humedad": 70,
        "ruido": 95,
        "int_luminosa": 600
    }

    best_solucion, best_vo = mainLS(prefServicios, valoresActuales)
    print(f'Best solucion: {best_solucion} - Best vo: {best_vo}', end='\n\n')
