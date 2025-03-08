from load_data import cargar_data
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

import warnings
warnings.simplefilter("ignore")

semana = 1
data = cargar_data(f'../Archivos/lecturaFotoS{semana}_tratada.csv')

d = 1
p_values = [[1], [1, 2], [1], [10]]
q_values = [[1, 2, 3, 4], [1, 2, 4, 6], [1], [10]]


best_aic = 999999  ##EN EL AIC, mientras mas bajo, mejor
best_model = None
best_order = None

for p in p_values[semana - 1]:
    for q in q_values[semana - 1]:
        try:
            model = ARIMA(data, order=(p, d, q)).fit()
            aic = model.aic
            print("Parametros-> p: ",p, "   d: ", d, "  q: ", q, "      AIC:", aic)

            if aic < best_aic:
                best_aic = aic
                best_model = model
                best_order = (p, d, q)
        except:
            print("Parametros-> p: ", p, "   d: ", d, "  q: ", q, "  COMBINACION NO VALIDA")


print(f"\nMejor modelo: ARIMA{best_order} con AIC = {best_aic}")

# Mejor modelo vs Datos Reales
plt.figure(figsize=(10, 5))
plt.plot(data, label="Datos reales", color = "blue")
plt.plot(best_model.fittedvalues, label="Datos de ARIMA", linestyle="dashed", color = "green")
plt.legend()
plt.show()

# ARIMA (p, d, q)
# Semana 1 - ARIMA(1, 1, 1)
# Semana 2 - ARIMA(1, 1, 1)
# Semana 3 - ARIMA(1, 1, 1)
# Semana 4 - ARIMA(10, 1, 10)
