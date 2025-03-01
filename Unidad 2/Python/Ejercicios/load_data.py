def cargar_data(archivo):
    data = []
    with open(archivo) as file:
        for e in file:
            data.append(float(e.strip()))

    return data