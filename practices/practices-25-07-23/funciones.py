import validaciones


def deleted_partc_evet(dictionary,evt):
    if(validaciones.event_exists(dictionary,evt)):
        for keyDic,value in dictionary.items():
            if(keyDic == evt):
                idPart = int(input("Enter the id of theParticipant: "))
                if(validaciones.partc_exists(value['participants'])):
                    
                    value['participants'].remove()


def add_participants(dictionary,evt):
    
    if(validaciones.event_exists(dictionary,evt)):
        # print(evt)
        for keyDic,value in dictionary.items():
            if(keyDic == evt):
                idPart = int(input("Enter the id of theParticipant: "))
                if(validaciones.partc_exists(value['participants'])):
                    namePar = input("Enter the name of theParticipant: ")
                    agePart = input("Enter the age of the Participant: ")
                    positPar = input("Enter the position of the Participant: ")
                    payPart = input("Has the user already paid for his ticket? y/n: ").lower()
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
        print(dictionary[evt])
    else:
        print("The event not exists.")
def create_event(dictionary):
    nameEvt = input("Enter the name of the Event: ")
    if(not validaciones.event_exists(dictionary,nameEvt)):
        locationEvt = input("Enter the location of the Event: ")
        date_month = input("Enter the date of the Event: ")
        
        dictionary[nameEvt]={
            "location": locationEvt,
            "date_month": date_month,
            "participants": []
        }
        print(dictionary)
    else:
        print("El evento ya existe")
        
def operation_options(opc,dic):
    if(opc==1):
        create_event(dic)
    elif(opc==2):
        evento = input("Enter the event to add the participant: ")
        add_participants(dic,evento)
    elif(opc==3):
        evento = input("Enter the event to add the participant: ")
        deleted_partc_evet(dic)

def menu_text():
    print("""
╔═════ °❀•°✮°•❀°═════╗
    𝕄enu 𝔸genda
1.Crear Evento.
2.Añadir Empleado-Participante.
3.Quitar Participante.
4.Eliminar Evento.
5.Editar Evento.
6.Ver Eventos.
7.Salir

╚═════ °❀•°✮°•❀°═════╝       
        """)

