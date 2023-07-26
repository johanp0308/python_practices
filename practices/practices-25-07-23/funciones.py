import validaciones
from random import Random


def delet_evt(lista,evt):
    if(validaciones.event_exists(lista,evt)  and not validaciones.verif_evt_finished(lista,evt) ):
        for eleme in lista:
            if(eleme["name"] == evt):
                lista.remove(eleme)

def modif_evt(lista,evt):
    if(validaciones.event_exists(lista,evt) and not validaciones.verif_evt_finished(lista,evt)):
        for eleme in lista:
            if(eleme["name"] == evt):
                print("Modify \n-name-\nlocation. \ndate_month. \nExit.")
                opc_modf = input("Enter what you want to modify")
                modif = input("Ingrese la valor de la modificacion")
                if(opc_modf != 'participants'):
                    eleme[opc_modf]=modif

def deleted_partc_evet(dictionary,evt):
    if(validaciones.event_exists(dictionary,evt)):
        for keyDic,value in dictionary.items():
            if(keyDic == evt):
                idPart = int(input("Enter the id of theParticipant: "))
                if(validaciones.partc_exists(value['participants'])):
                    for elemento in value['participants']:
                        if(elemento['document']==idPart):
                            value['participants'].remove(elemento)
                            print(value['participants'])
                            break
                    else:
                        print("you finished deleting")
                else:
                    print("participant does not exist")


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
        
        dictionary.append({
            "identi": Random.randint(100,999),
            "name": nameEvt,
            "location": locationEvt,
            "date_month": date_month,
            "participants": [],
            "finished": False
        })

        print(dictionary)
    else:
        print("El evento ya existe")
        
def operation_options(opc,lista):
    if(opc==1):
        create_event(lista)
    elif(opc==2):
        evento = input("Enter the event to add the participant: ")
        add_participants(lista,evento)
    elif(opc==3):
        evento = input("Enter the event to add the participant: ")
        deleted_partc_evet(lista)

def operation_options_evt(opc,lista):
    if(opc == 1):
        event = input("Enter the name event please: ")
        modif_evt(opc,lista)
    elif(opc == 2):
        event = input("Enter the name event please: ")
        
    elif(opc == 3):
        event = input("Enter the name event please: ")


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

def menu_evt():
    print("""
    ╔═════ °❀•°✮°•❀°═════╗
        Menu Eventos.
    1. Modificar Evento.
    2. Eliminar Evento.
    3. Marcar Evento Realizado.
    4. 
    
    """)

