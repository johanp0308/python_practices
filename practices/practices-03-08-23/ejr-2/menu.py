import parqueadero

def opc_adPlac(opc):
    if(opc == 1):
        pass
    elif(opc == 2):
        pass
    elif(opc == 3):
        pass
    elif(opc == 4):
        pass
    elif(opc == 5):
        return False
def menu_placas():
    ejec = True
    while ejec:
        try:
            print("""
    ===========================
        Entradas y Salidas
    1. Registrar Entrada.
    3. Marcar Salida.
    4. Pagar Deuda.
    5. Salir.
                  
                  """)
            opc = int(input("Ingrese una opcion Valida:"))
            ejec = opc_adPlac(opc)
        except ValueError:
            print("Opcion no Valida!!!")

def opc_main(opc):
    if(opc == 1):
        pass
    elif(opc==2):
        pass
    elif(opc==3):
        pass
    elif(opc==4):
        pass
    elif(opc==5):
        pass
    elif(opc==6):
        val = input("Estas seguro de que queires salir y/n: ")
        if(val == 'y'):
            return False
    return True

def menu_main():
    try:
        ejec = True
        while ejec:
            print("""
===========================
    Menu Parqueadero
1. Administrar Salidas y Entradas.
3. Historico de Vehiculos.
4. Dinero Reacaudado.
5. Vehiculos Parqueados.
                """)
            opc = int(input("Ingrese una opcion:"))
            ejec = opc_main(opc)
    except ValueError:
        print("Opcion no Valida!!!")
        