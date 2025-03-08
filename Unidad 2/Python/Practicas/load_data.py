def cargar_data(archivo):
    with open(archivo) as file:
        data = [float(e.strip()) for e in file]

    return data