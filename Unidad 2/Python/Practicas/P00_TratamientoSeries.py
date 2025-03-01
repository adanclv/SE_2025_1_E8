from procesamiento.carga_datos import cargar_data
from procesamiento.tratamiento import to_int, tratamiento_vacios, tratar_outliers
from procesamiento.visualizacion import outliers_view

if __name__ == '__main__':
    semana = 3
    header, data = cargar_data(f'../Archivos/lecturaFotoS{semana}.csv')
    data = list(zip(*data)) #.T
    data[0] = to_int(data[0])
    data[1] = to_int(data[1])
    data = tratamiento_vacios(list(map(list, zip(*data))))

    outliers_view([fila[1] for fila in data]) # Visualización de outliers
    data = tratar_outliers(data)

    with open(f'../Archivos/lecturaFotoS{semana}_tratada.csv', 'w') as file:
        serie = [fila[1] for fila in data]
        file.write('\n'.join([str(round(e, 4)) for e in serie]))
    print(data)