REGEX_SENSORS_DATA = "^I[0-9]+-[0-9]+-[0-9]+-[0-9]+F$" # I123-42-12-412F

# Dispositivos
IDS_RELE = [1, 2, 3]
IDS_LDR = [4, 5, 6, 7] # [Central, rele1, rele2, rele3]

# Preferencias
MINIMO = 15
MAXIMO = 60
PROBLEMA = 'maximizacion'
PESO = 1
COSTO = 2

ALFA = 0.5
BETA = 0.5

# Algoritmo Genético (Hiperparámetros)
N_POP = 100
N_PARENTS = 50
PROBABILIDAD_MUTA = 5
ITERACIONES = 100