# Simulacro reto/examen/filtro:

# Nota: Cabe aclarar que según acuerdos previos esto no será considerado como nota pero si requiere que 
# se vea el compromiso. Por lo tanto, como es un simulacro se espera que se respeten las normas básicas 
# de una prueba de este tipo; tales como: no hablar con los compañeros, no usar internet para algo 
# diferente a classroom, no usar ningún otro tipo de dispositivo electrónico, preguntas que no sean 
# de interpretación, etc.

# 1. Dada la siguiente estructura de datos:


Empresas = {

"Empresa 1": [{"departamento": "Recursos Humanos", "empleados": 5}, {"departamento": "Contabilidad", "empleados": 4}, {"departamento": "Ventas", "empleados": 10}, {"departamento": "Operaciones", "empleados": 25}],

"Empresa 2": [{"departamento": "Recursos Humanos", "empleados": 10}, {"departamento": "Contabilidad", "empleados": 15}, {"departamento": "Ventas", "empleados": 25}, {"departamento": "Operaciones", "empleados": 41}],

"Empresa 3": [{"departamento": "Recursos Humanos", "empleados": 8}, {"departamento": "Contabilidad", "empleados": 20}, {"departamento": "Ventas", "empleados": 32}, {"departamento": "Operaciones", "empleados": 56}],

"Empresa 4": [{"departamento": "Recursos Humanos", "empleados": 5}, {"departamento": "Contabilidad", "empleados": 8}, {"departamento": "Ventas", "empleados": 15}, {"departamento": "Operaciones", "empleados": 29}],

"Empresa 5": [{"departamento": "Recursos Humanos", "empleados": 20}, {"departamento": "Contabilidad", "empleados": 35}, {"departamento": "Ventas", "empleados": 58}, {"departamento": "Operaciones", "empleados": 97}],

}

def menu():
    print("""
====================
    Menu de Empresas
1. Empresas que tienen más de 10 empleados en Recursos Humanos.
2. Promedio de empleados por departamento.
3. Empresas que tienen el doble o más del doble de 
   empleados en operaciones con respecto a ventas.
4. Empleados por departamento de cada empresa.
5. Salir.
    
    """)

def opciones_menu(opcion=0):
    
    if(opcion == 1):
        print("==== Empresas con mas de 10 empleados =====")
        for empr,deps in Empresas.items():
            for dep in deps:
                if(dep["departamento"] == "Recursos Humanos"):
                    if(dep["empleados"] >10):
                        print(f"Empresa {empr} tiene {dep['empleados']}")
    elif(opcion == 2):
        recur = 0
        opera = 0
        conta = 0
        venta = 0
        for deplist in Empresas.values():
            for dep in deplist:
                departa = dep['departamento']
                if(departa == "Recursos Humanos"):
                    recur += dep['empleados']
                elif(departa == "Contabilidad"):
                    conta += dep['empleados']
                elif(departa == "Ventas"):
                    venta += dep['empleados']
                elif(departa == "Operaciones"):
                    opera += dep['empleados']
                else:
                    print("Error")
        print(f"Recuros humanos: {recur/len(Empresas)}")
        print(f"Ventas: {venta/len(Empresas)}")
        print(f"Operaciones: {opera/len(Empresas)}")
        print(f"Contabilidad: {conta/len(Empresas)}")

    elif(opcion == 3):
        print("===== Empresas con mas del doble de empleados en ventas de operaciones =====")
        for empre,lista in Empresas.items():
            empleVen = 0
            empleOpr = 0
            for dicdep in lista:
                if(dicdep["departamento"]=="Ventas"):
                    empleVen = dicdep["empleados"]
                if(dicdep["departamento"]=="Operaciones"):
                    empleOpr = dicdep["empleados"]
            if(empleVen*2<=empleOpr):
                print(f"Empresa {empre} tiene en Operaciones: {empleOpr}")
    elif(opcion==4):
        newDic = {}
        for empre,listaDep in Empresas.items():
            for dicDep in listaDep:
                key = dicDep["departamento"]
                newDic[key] = []
        for dep,emprs in newDic.items():
            for empr,listadep in Empresas.items():
                for depDic in listadep:
                    depar = depDic["departamento"]
                    if(depar == dep):
                        aggEmpr = {
                            "Empresa" : empr,
                            "empleados": depDic["empleados"]
                        }
                        emprs.append(aggEmpr)
        print(newDic)

def main():
    ejecucion = True
    while ejecucion:
        try:
            menu()
            opc = int(input("Ingrese una opcion valida: "))
            
            if(opc == 5):
                ejecucion = False
            elif(opc >0):
                opciones_menu(opc)
            else:
                print("Opcion no en el rango")
        except ValueError:
                print("Error")
    

main()

# Crea un menú que se repita hasta que el usuario ingrese la opción de salida (a tu elección) y 
# utilice una función para cada opción válida. Las funcionalidades son:

#     Mostrar cuántas empresas tienen más de 10 empleados en Recursos Humanos
#     Mostrar el promedio de empleados por departamento (teniendo en cuenta todas las empresas para cada calculo)
#     Mostrar cuántas empresas tienen el doble o más del doble de empleados en operaciones con respecto a ventas
#     Mostrar una nueva estructura de datos reorganizada donde las llaves del diccionario principal no sea 
#       empresas sino por departamento.






# 2. Dado el siguiente ejercicio con su solución:

# Escribe un programa que genere los primeros 4 números perfectos. Un número perfecto es un número entero positivo que es igual a la suma de sus divisores propios positivos. Dicho de otra forma, un número perfecto es aquel que es amigo de sí mismo. Así, 6 es un número perfecto porque sus divisores propios positivos son 1, 2 y 3; y 6 = 1 + 2 + 3.

# numeros_perfectos_encontrados = []
# numero = 2

# while len(numeros_perfectos_encontrados) < 4:
#     suma_divisores = 0

#     for i in range(1, numero):
#         if numero % i == 0:
#             suma_divisores += i

#     if suma_divisores == numero:
#         numeros_perfectos_encontrados.append(numero)

#     numero += 1

# print("Los primeros 4 números perfectos son:")
# print(numeros_perfectos_encontrados)

    # Reestructura el ejercicio para que el calculo del número perfecto sea hecho con funciones
    # Una vez reestructurado el ejercicio, comenta línea por línea el funcionamiento del ejercicio. Recuerda que 
    # además de explicar la sentencia como código se debe explicar el propósito a nivel de la solución al problema 
    # propuesto.