import prints
import valid_part

particpantes = {
    "123412":{"name": "Hola","age": 23,"residence":"santander","program": "Atletismo"},
    "1234123":{"name": "Hola","age": 23,"residence":"santander","program": "Atletismo"},
    "1234456":{"name": "Hola","age": 23,"residence":"santander","program": "Atletismo"},
    "1235648":{"name": "Hola","age": 23,"residence":"santander","program": "Atletismo"}
}


def opc_pro(opci):
    if(opci==1):
        return "Atletismo"
    elif(opci==2):
        return "Ciclismo"
    elif(opci==3):
        return "Patinaje"
    return "None"

def create():
    ejec = True
    while ejec:
        try:
            id = input("Enter the participant's document: ")
            if(valid_part.part_exists(id,particpantes)):
                nombre = input("Enter the name of the Participant: ")
                age = int(input("Enter the age of the Participant: "))
                if(age>=18):
                    residence = input("In which department you reside?").lower()
                    if(residence == "santander"):
                        print("""
        •—————————•°•✿•°•—————————•
            Choose any program               
        1. Altetismo.
        2. Ciclismo.
        3. Patinaje.                  
        4. Cancel.   
                            """)
                        opc = int(input("Enter any option: "))
                        print("        •—————————•°•✿•°•—————————•")
                        if(opc>0 and opc<4):
                            prog = opc_pro(opc)
                            particpantes[id]={
                                "name": nombre,
                                "age": age,
                                "residence":residence,
                                "program": prog
                            }
                            prints.print_part(id,particpantes)
                            ejec=False
                        else:
                            print("registration canceled")
                            break
                    else:
                        print("The participant must be from Santander")
                elif(age<18 and age>0):
                    print("Sorry, you are not of legal age")
                else:
                    print("Sorry, Age cannot be negative")
            else:
                print("Sorry no participant found")
        except ValueError:
            print("Error Non-numeric value")

def eliminar():
    ejec = True
    while ejec:
        try:
            id = input("Enter the participant's document: ")
            print(valid_part.part_exists(id,particpantes))
            if(valid_part.part_exists(id,particpantes)):
                print("You deleted this participant")
                prints.print_part(id,particpantes[id])
                particpantes.pop(id)
                ejec = False
            else:
                print("Sorry no participant found")
        except ValueError:
            print("Error Non-numeric value")
            
def see_all():
    print("        •—————————•°•✿•°•—————————•")    
    for id,info in particpantes.items():
        prints.print_part(id,info)