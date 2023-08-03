# Cree en un archivo json la información de países (al menos 10 países) con los siguientes datos:
#   Nombre
#   Población
#   Moneda
#   Continente
#   Área
# Cree un menú en python que lea la información del archivo json y se pueda consultar:
#   La información de todos los países
#   La información por país ingresando el nombre
#   El país con mayor población
#   El país con menor área
#   Imprimir continente y todos los países de cada uno
import json

def descargar(file_name):
    data = []
    with open(file_name) as file:
        data = json.load(file)
    return data