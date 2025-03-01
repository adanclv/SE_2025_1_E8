import numpy as np
import matplotlib.pyplot as plt
from load_data import cargar_data

from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

semana = 4
data = cargar_data(f'../Archivos/lecturaFotoS{semana}_tratada.csv')

data = np.diff(data)

plt.figure(figsize=(12,5))

# Creacion de ejes
ax1 = plt.subplot(121)
ax2 = plt.subplot(122)

#De acuerdo con la libreria, se tiene que tomar en cuenta el tamano de la serie, en ese sentido, para este ejemplo
#se tiene el maximo de lags es 6:
#ValueError: Can only compute partial correlations for lags up to 50% of the sample size. The requested nlags 10 must be < 6.

# Grafica ACF (identifica q)
plot_acf(data, lags = 10, ax=ax1) #lags=10)

# Grafica PACF (identifica p)
plot_pacf(data, lags = 10, ax=ax2) #lags=10)


plt.show()

# Semana 1 - p = 1 / q = 1, 2, 3, 4
# Semana 2 - p = 1, 2 / q = 1, 2, 4, 6
# Semana 3 - p = 1 / q = 1
# Semana 4 - p = 10 / q = 10