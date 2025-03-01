from pmdarima import auto_arima

datos = [100, 200, 50, 700, 20, 30, 200, 300, 500, 1200, 600, 400, 0, 100, 120]
datos = datos * 3


modelo = auto_arima(datos, seasonal=False, trace=True)
print(modelo.summary())