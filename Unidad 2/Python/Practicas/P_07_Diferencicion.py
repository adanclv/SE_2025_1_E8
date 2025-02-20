from procesamiento.carga_datos import cargar_data
from procesamiento.tratamiento import to_int, tratamiento_vacios, tratar_outliers
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import numpy as np
from matplotlib import pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

header, data = cargar_data('../Archivos/lecturaFoto.csv')
data = list(zip(*data)) #.T
data[0] = to_int(data[0])
data[1] = to_int(data[1])
data = tratamiento_vacios(list(map(list, zip(*data))))
data = tratar_outliers(data)

'''# resultado = adfuller([e[1] for e in data])
# print(f"p-valor serie original: {resultado[1]}")

# Primera diferenciación (d = 1)
datos_d1 = np.diff([e[1] for e in data])
# resultado_d1 = adfuller(datos_d1)
# print(f"p-valor con d=1: {resultado_d1[1]}")

# Graficamos las series
plt.figure(figsize=(16,4))
plt.subplot(1,2,1)
plt.plot([e[1] for e in data], marker='o')
plt.title("Serie original")

plt.subplot(1,2,2)
plt.plot(datos_d1, marker='o')
plt.title("Serie diferenciada (d=1)")

plt.show()

plt.figure(figsize=(12,5))

# Creacion de ejes
ax1 = plt.subplot(121)
ax2 = plt.subplot(122)

#De acuerdo con la libreria, se tiene que tomar en cuenta el tamano de la serie, en ese sentido, para este ejemplo
#se tiene el maximo de lags es 6:
#ValueError: Can only compute partial correlations for lags up to 50% of the sample size. The requested nlags 10 must be < 6.

# Grafica ACF (identifica q)
plot_acf(datos_d1, lags = 6, ax=ax1) #lags=10)

# Grafica PACF (identifica p)
plot_pacf(datos_d1, lags = 6, ax=ax2) #lags=10)


plt.show()'''
pS = [1, 2]
qS= [1, 2, 4, 6]

for p in pS:
    for q in qS:
        modelo = ARIMA([e[1] for e in data], order=(p,1,q))  # ARIMA(p,d,q)
        ajuste = modelo.fit()
        pronostico = ajuste.forecast(steps=1)  # Un paso adelante

        print("Pronóstico:", pronostico[0], 'p:', p, 'q:', q)