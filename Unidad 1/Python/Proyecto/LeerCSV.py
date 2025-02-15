import csv

def escalar_rango(valor):
    return valor // 4

def convertir_binario(valor):
    return 1 if valor >= 127 else 0

def leerCSV(archivo, separador):
    with open(archivo) as file:
        datos = csv.reader(file, delimiter=separador)
        valores = [list(map(int, dato)) for dato in datos]

    return valores

def vector_binario(valores):
    datos = [list(map(escalar_rango, valor)) for valor in valores]
    datos_binarios = [list(map(convertir_binario, dato)) for dato in datos]

    return datos_binarios