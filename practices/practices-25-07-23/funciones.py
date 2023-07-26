



def add_participants(dictionary,evt):
    for keyDic,value in dictionary.items():
        if(keyDic == evt):
            idPart = input("Enter the id of theParticipant: ")
            namePar = input("Enter the name of theParticipant: ")
            agePart = input("Enter the age of the Participant: ")
            positPar = input("Enter the position of the Participant: ")
            payPart = input("Has the user already paid for his ticket? y/n").lower()
            if(payPart=='y'):
                pay = True
            elif(payPart=='n'):
                pay = False
            else:
                print("Error estableciendo booleano")
                
            value["participants"].append({
                "document": idPart,
                "name":namePar,
                "age":agePart,
                "position":positPar,
                "contribution":pay
            })
            
            print(value["participants"])
        else:
            print("this event does not exist")

def create_event(dictionary):
    nameEvt = input("Enter the name of the Event: ")
    locationEvt = input("Enter the location of the Event: ")
    date_month = input("Enter the date of the Event: ")
    
    dictionary[nameEvt]={
        "location": locationEvt,
        "date_month": date_month,
        "participants": []
    }
    print(dictionary)
    
def operation_options(opc,dic):
    if(opc==1):
        create_event(dic)
    if(opc==2):
        evento = input("Enter the event to add the participant: ")
        add_participants(dic,evento)
        
def menu_text():
    print("""
╔═════ °❀•°✮°•❀°═════╗
    𝕄enu 𝔸genda
1.Crear Evento.
2.Añadir Empleado-Participante.
3.Quitar Participante.
4.Eliminar Evento.
5.Editar Evento.
6.Ver Validaciones.
7.Salir

╚═════ °❀•°✮°•❀°═════╝       
         """)
    
