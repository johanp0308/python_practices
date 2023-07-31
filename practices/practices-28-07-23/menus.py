import part_program

def menu_participantes():
    exePart = True
    while exePart:
        try:
            print("""
    •—————————•°•✿•°•—————————•
        Participants Menu      
    1. Add Participants.
    2. Delete Participantes.
    3. See all.

            """)
            opc = int(input("    Ingrese una Opcion: "))
            print("    •—————————•°•✿•°•—————————•")
            exePart = part_maneja(opc)
        except ValueError:
            print("Error! Enter a non-numeric value")
def part_maneja(opc):
    if(opc==1):
        part_program.create()
    elif(opc==2):
        part_program.eliminar()
    elif(opc==3):
        part_program.see_all()
def manejador(opcion):

    if(opcion==1):
        menu_participantes()
    elif(opcion==2):
        pass
    elif(opcion==3):
        fer = input("Do you want to go out? y/n: ")
        if(fer == 'y'):
            return False
    return True

def main_menu():
    ejecucion = True
    while ejecucion:
        try:
            print("""
•——————•°•✿•°•——————•
    Main Menu
1. Particpants.
2. Ranking.
3. Salir.
•——————•°•✿•°•——————•    
                """)
            opc = int(input("Entwer a option: "))
            ejecucion = manejador(opc)
        except ValueError:
            print("Error! Enter a non-numeric value")
