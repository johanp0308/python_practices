# 1. Escribir un programa que guarde en una variable el diccionario 
# {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por 
# una divisa y muestre su símbolo o un mensaje de aviso si la 
# divisa no está en el diccionario.

# currency = {"Euro":'€',"Dollar":'$',"Yen":'¥'}
# badge = input("Enter a Currency: ")

# if('No encontrado'==currency.get(badge,'No encontrado')):
#     print("No encontrado :C")
# else:
#     print(currency[badge])

# 2. Escribir un programa que pregunte al usuario su nombre, 
# edad, dirección y teléfono y lo guarde en un diccionario. 
# Después debe mostrar por pantalla el mensaje <nombre> tiene 
# <edad> años, vive en <dirección> y su número de teléfono 
# es <teléfono>.

# user_data = {
#     "name":"",
#     "age":0,
#     "address":"",
#     "telephone":0
# }

# for keys in user_data.keys():
#     dato = input(f"Enter you {keys}: ")
#     user_data[keys]=dato

# print(user_data)

# 3. Escribir un programa que guarde en un diccionario los 
# precios de las verduras de la tabla, pregunte al usuario por 
# una verdura, un número de kilos y muestre por pantalla el 
# precio a pagar. Si la fruta no está en el diccionario debe 
# mostrar un mensaje informando de ello.

# Verdura               Precio (Kg)
# Brócoli                2500 COP
# Pimentón               1250 COP
# Arveja                 3500 COP

# vegetables = {
#     "Brocoli": 2500,
#     "Pimenton": 1250,
#     "Arveja": 3500
# }

# vege = input("Enter you vegetable: ")
# for key in vegetables.keys():
#     if(vege == key):
#         kg = int(input("Enter to numbre of kilos to carry: "))
#         print(f"El precio de {key} es de {vegetables[vege]*kg}")

# print("No existe ese vegetal en la base de datos")

# 4. Escribir un programa que cree un diccionario vacío y 
# lo vaya llenado con información sobre una persona (por 
# ejemplo nombre, edad, sexo, teléfono, correo 
# electrónico, etc.) que se le pida al usuario. Cada 
# vez que se añada un nuevo dato debe imprimirse el 
# contenido del diccionario.

# user_data = {}
# execution = True
# while execution:
#     execute = (input("Do you want to enter a user data? y/n: ")).upper()
#     if(execute=="Y"):
#         keyIn = input("Enter what type of user data it is: ")
#         value = input(f"Enter the data of {keyIn}: ")

#         if keyIn in user_data:
#             user_data[keyIn]=value
#         else:
#             user_data[keyIn]=value
#             print(user_data)
#     elif(execute=="N"):
#         execution=False
#     else:
#         print("Wrong Option")

# 5. Escribir un programa que cree un diccionario simulando una cesta de la compra. El programa debe 
# preguntar el artículo y su precio y añadir el par 
# al diccionario, hasta que el usuario decida terminar. 
# Después se debe mostrar por pantalla la lista de la 
# compra y el coste total

# trolley = {}
# execution = True
# total = 0
# while execution:
#     exist = False
#     execute = (input("Do you want to buy something? y/n: ")).upper()
#     if(execute=="Y"):
#         keyIn = input("What is your article called? : ")
#         value = input(f"What does this {keyIn} cost? : ")
#         exist=True if "does not exist"!=trolley.get(keyIn,"does not exist") else False

#         if(exist):
#             trolley[keyIn]=value
#             print("This article has already been introduced")
#         else:
#             trolley[keyIn]=value
#     elif(execute=="N"):
#         for value in trolley.values():
#             total += int(value)
#         execution=False
#     else:
#         print("Wrong Option")

# print("===== Total =====")
# for key, value in trolley.items():
#     print(f"{key} ==> {value}")

# print(f"His total is : {total}")

# 6. Escribir un programa que gestione las facturas 
# pendientes de cobro de una empresa. Las facturas 
# se almacenarán en un diccionario donde la clave de 
# cada factura será el número de factura y el valor 
# el coste de la factura. El programa debe preguntar 
# al usuario si quiere añadir una nueva factura, pagar 
# una existente o terminar. Si desea añadir una nueva 
# factura se preguntará por el número de factura y su 
# coste y se añadirá al diccionario. Si se desea pagar
# una factura se preguntará por el número de factura 
# y se eliminará del diccionario. Después de cada 
# operación el programa debe mostrar por pantalla la 
# cantidad cobrada hasta el momento y la cantidad pendiente de cobro.

# fact = {}
# ejecucion = True
# pagado = 0
# debe = 0
# while ejecucion:
#     print("""
# ===========================
#     Sistema de Facturas
# 1. Agregar Factura.
# 2. Pagar Factura.
# 3. Ver lo que eh pagado.
# 4. Ver lo que debo.
# 5. Ver facturas.
# 6. Salir.
# ===========================     
# """)
#     opc = int(input("Ingrese Una Opcion Valida: "))
#     if(opc==1):
#         numRef = int(input("Ingrese el numero de referencia de la factura: "))
#         valor = float(input("Ingrese el valor de la factura: "))
#         fact[numRef]=valor
#         debe += valor
#     elif(opc==2):
#         numRef = int(input("Ingrese el numero de referencia de la factura a pagar: "))
#         if(numRef in fact):
#             print(f"Su valor a pagar es de: {fact[numRef]}")
#         debe -= fact[numRef]
#         pagado += fact.pop(numRef)
#     elif(opc==3):
#         print(f"El valor que usted ah pagado es de: {pagado}")
#     elif(opc==4):
#         print(f"El valor que usted debe es de: {debe}")
#     elif(opc==5):
#         for key,value in fact:
#             print(f"Ref:{key} valor:{value}")
#     elif(opc==6):
#         ejecucion=False
#     else:
#         print("Opcion Invalida")
# print("Termino el programa")

# 7. Escribir un programa que permita gestionar la 
# base de datos de clientes de una empresa. Los 
# clientes se guardarán en un diccionario en el que 
# la clave de cada cliente será su NIF, y el valor 
# será otro diccionario con los datos del cliente 
# (nombre, dirección, teléfono, correo, preferente), 
# donde preferente tendrá el valor True si se 
# trata de un cliente preferente. El programa debe 
# preguntar al usuario por una opción del siguiente 
# menú: (1) Añadir cliente, (2) Eliminar cliente, 
# (3) Mostrar cliente, (4) Listar todos los 
# clientes, (5) Listar clientes preferentes, (6) 
# Terminar. En función de la opción elegida el 
# programa tendrá que hacer lo siguiente:Preguntar 
# los datos del cliente, crear un diccionario con 
# los datos y añadirlo a la base de datos.Preguntar 
# por el NIF del cliente y eliminar sus datos de 
# la base de datos.Preguntar por el NIF del cliente 
# y mostrar sus datos.Mostrar lista de todos los 
# clientes de la base datos con su NIF y nombre.
# Mostrar la lista de clientes preferentes de la 
# base de datos con su NIF y nombre.Terminar el programa.
#·------------------------------------------------------------
empresa = {}
ejecucion = True

while ejecucion:
    print("""
===========================
    Sistema de Facturas
1. Agregar Cliente.
2. Elminar Cliente.
3. Mostrar Cliente.
4. Listar Clientes.
5. Listar Clientes Preferentes.
6. Salir.
===========================     
""")
    opc = int(input("Ingrese Una Opcion Valida: "))
    if(opc==1):
        cliente = {}
        nif = input("Ingrese el numero de NiF del Cliente: ")
        cliente["nombre"] = input("Ingrese el Nombre del Cliente: ")
        cliente["direccion"] = input("Escriba la direccion de residencia: ")
        cliente["telefono"] = input("Digite el numero de telefono: ")
        cliente["correo"] = input("Escriba el correo del cliente: ")
        cliente["prefe"] =True if (input("El cliente es preferente: y/n: ").upper()) == 'Y' else False
        empresa[nif]=cliente
        
    elif(opc==2):
        nif = input("Ingrese el nif del cliente al eliminar: ")
        eliminado = empresa.pop(nif,"No enconcontrado")
        if(eliminado!="No encontrado"):
            print("Cliente eliminado")
    elif(opc==3):
        nif = input("Ingrese el nif del cliente a mostrar: ")
        clienteCons = empresa.get(nif,"Cliente no encontrado")
        if(clienteCons != "Cliente no encontrado"):
            print(f"""
==== Datos Cliente ====
Nombre : {clienteCons["nombre"]}
Direccion: {clienteCons["direccion"]}
Telefono:  {clienteCons["telefono"]}
correo: {clienteCons["correo"]}
Cliente preferente: {"Si" if clienteCons["prefe"]=='Y' else "No"}
=======================
                """)
    elif(opc==4):
        print("****** Lista de Cliente ******")
        for Nif,Cli in empresa:
            print(f"""
== Cliente {Nif} ==
Nombre : {Cli["nombre"]}
Direccion: {Cli["direccion"]}
Telefono:  {Cli["telefono"]}
correo: {Cli["correo"]}
Cliente preferente: {"Si" if clienteCons["prefe"]=='Y' else "No"}
-------------------
                """)
    elif(opc==5):
        for nife,Clie in empresa:
            if(Clie["prefe"]=='Y'):
                print(f"""
== Cliente {Nif} ==
Nombre : {Cli["nombre"]}
Direccion: {Cli["direccion"]}
Telefono:  {Cli["telefono"]}
correo: {Cli["correo"]}
Cliente preferente: {"Si" if clienteCons["prefe"]=='Y' else "No"}
-------------------
                """)
    elif(opc==6):
        ejecucion=False
    else:
        print("Opcion Invalida")
print("Termino el programa")
