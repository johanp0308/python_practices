import empleados

def opc_main(opc):
    if(opc==6):
        return False
    Opc_menu={
        1:empleados.register_empleado,
        2:empleados.list_emplea,
        3:empleados.mod_emplea,
        4:empleados.desp_empea,
        5:empleados.regis_in_out
    }
    for key,func in Opc_menu.items():
        if(key==opc):
            return func()

def main_menu():
    ejec = True
    while ejec:
        try:
            print("""
==============================
    Menu Principal
1. Registro empleado.
2. Listar Empleados.
3. Modificar Empleados.
4. Despedir Empleado.
5. Registrar Entrada y Salida.
6. Salir
            """)
            opc = int(input("Ingrese una opcion valida: "))
            if(opc>0 and opc <=6):
                ejec = opc_main(opc)
            else:
                print("Opcion no Valida")
        except ValueError:
            print("Error!!!")