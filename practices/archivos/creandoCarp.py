import os
from datetime import date as dt


def getDate():
  today = dt.today()
  fecha = f"{today.day}-{today.month}-{today.year}"
  return fecha

def creat_dir(fecha):
  os.system(f"touch practices/practices-{fecha}.py")
  archivo = open(f"practices/practices-{fecha}.py", "w")
  archivo.write("""
def hola():
  print("Hola mundo")

hola()""")
  archivo.close()
  os.system(f"python3 practices/practices-{fecha}.py")
print(getDate())
creat_dir(getDate())


