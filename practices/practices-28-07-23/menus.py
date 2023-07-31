import part_program
import ranking
import valid_part

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
    4. Cancel

            """)
            opc = int(input("    Ingrese una Opcion: "))
            print("    •—————————•°•✿•°•—————————•")
            exePart = part_maneja(opc)
        except ValueError:
            print("Error! Enter a non-numeric value")
            
def opc_progr(opc):
    while True:
        try:
            if(opc==4):
                return False
            id = input("Enter the participant's document: ")
            if(valid_part.part_exists(id)):
                posicion = int(input("Enter the participant's ranking in numbers: "))
                if(opc== 1):
                    ranking.agregar_ranking("atletismo",id,posicion)
                    break
                elif(opc==2):
                    ranking.agregar_ranking("ciclismo",id,posicion)
                    break
                elif(opc==3):
                    ranking.agregar_ranking("patinaje",id,posicion)
                    break
            else:
                print("Sorry no participant found")
        except Exception:
            print("Error! Enter a non-numeric value")
    return True
        
def menu_ranked():
    exec = True
    while exec:
        try:
            print("""
    •—————————•°•✿•°•—————————•
        Rankings Menu     
    1. Atletismo.
    2. Ciclismo.
    3. Patinaje.
    4. Cancel.

            """)
            opc = int(input("Enter any option"))
            print("    •—————————•°•✿•°•—————————•")
            exec = opc_progr(opc)
        except:
            print("Error Non-numeric value")

# Manejador de opciones de Participantes
def part_maneja(opc):
    if(opc==1):
        part_program.create()
    elif(opc==2):
        part_program.eliminar()
    elif(opc==3):
        part_program.see_all()

# Manejador de opciones prinicipal
def manejador(opcion):

    if(opcion==1):
        menu_participantes()
    elif(opcion==2):
        menu_ranked()
    elif(opcion==3):
        fer = input("Do you want to go out? y/n: ")
        if(fer == 'y'):
            return False
    return True

# Menu Principal
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
