import validaciones
import random


def delet_evt(lista,evt,iden):
    if(validaciones.event_exists(lista,evt,iden)  and not validaciones.verif_evt_finished(lista,evt) ):
        for eleme in lista:
            if(eleme["name"] == evt and eleme['identi']==iden):
                lista.remove(eleme)
                break
        else:
            print("Participant not found")
    else:
        print("Event not found or Finished")      

def modif_evt(lista,evt,iden):
    if(validaciones.event_exists(lista,evt,iden) and not validaciones.verif_evt_finished(lista,iden)):
        for eleme in lista:
            if(eleme["name"] == evt):
                print("Modify \n-name\n-location. \n-date_month. \n-Exit.")
                opc_modf = input("Enter what you want to modify: ")
                modif = input("Enter the value of the modification: ")
                if(opc_modf != 'participants' and opc_modf != 'identi'):
                    if(validaciones.verif_attri_exist(lista,opc_modf)):
                        eleme[opc_modf]=modif
                    else:
                        print("that attribute does not exist")
                else:
                    print("Ese elemento no se puede modificar directamente")
    else:
        print("Event not found or Finished")
    print(lista)                 

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


def add_participants(lista,evt):
    
    if(validaciones.event_exists(lista,evt)):
        for dicEvt in lista:
            if(dicEvt['name'] == evt):
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
def create_event(lista):
    nameEvt = input("Enter the name of the Event: ")
    if(not validaciones.event_exists(lista,nameEvt)):
        locationEvt = input("Enter the location of the Event: ")
        date_month = input("Enter the date of the Event: ")
        
        lista.append({
            "identi": random.randint(100,999),
            "name": nameEvt,
            "location": locationEvt,
            "date_month": date_month,
            "participants": [],
            "finished": False
        })

        print(lista)
    else:
        print("El evento ya existe")
        
def operation_options(opc,lista):
    if(opc==1):
        create_event(lista)
    elif(opc==2):
        idEvt = int(input("Enter the id of the event to add Participants "))
        evento = input("Enter the event to add the participant: ")
        add_participants(lista,evento)
    elif(opc==3):
        evento = input("Enter the event to add the participant: ")
        deleted_partc_evet(lista)
    elif(opc==4):
        ident = int(input("Enter the id of the event to delete"))
        event = input("Enter the name of the event to delete")
        delet_evt(lista,event,ident)
    elif(opc == 5):
        ident = int(input("Enter the id of the event to delete"))
        event = input("Enter the name event please: ")
        modif_evt(lista,event,ident)
    elif(opc == 6):
        event = input("Enter the name event please: ")
    elif(opc == 7):
        return False
    
    return True
        

def operation_options_evt(opc,lista):
    if(opc == 1):
        pass
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
    pass

