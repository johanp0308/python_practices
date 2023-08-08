from datetime import datetime, delta

fechaActual = datetime.now()

fechaPasada = datetime(2002,5,29)

fecha = fechaActual - fechaPasada

ayios = fecha.days/365

print(fecha)

print(fecha.days)


print(ayios)


