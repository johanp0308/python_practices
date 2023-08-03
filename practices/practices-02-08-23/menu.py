def opc_main(opc):
    if(opc==1):
            
    elif(opc==2):    
    elif(opc==3):    
    elif(opc==4):    
    elif(opc==5):    
    elif(opc==6):    

def menu_main():
    ejec = True
    while ejec:
        try:
            print("""
=========================
    Menu Paises
1. Todos los Paises.
2. Consultar Pais.
3. Pais Top poblacion.
4. Pais Area Menor.
5. Paises Por continente.
6. Salir
                  """)
            opc = int(input("Ingrese una opcion validad: "))
            ejec = opc_main(opc)
        except ValueError:
            print("Valor no numerico!")