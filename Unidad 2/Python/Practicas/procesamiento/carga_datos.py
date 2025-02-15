import csv

def cargar_data(archivo):
    with open(archivo) as file:
        reader = csv.reader(file)
        data = list(reader)
    return data[0], data[1:]