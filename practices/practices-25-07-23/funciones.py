import validaciones
import impresiones
import random

def mark_evt(lista,idEvt):
    pass
def deuda_evt(lista,idEvt):
    deuda = 0
    for dicEle in lista:
        if(dicEle['identi'] == idEvt):
            for elemento in dicEle['participants']:
                if(elemento['contribution']== True):
                    deuda += 50000
    print("╔════════════════════════════╗")
    print(f"  La deuda es de: {deuda}")
    print("╚════════════════════════════╝")

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

def deleted_partc_evet(lista,evt,iden):
    if(validaciones.event_exists(lista,evt,iden)):
        for dicel in lista:
            if(dicel['identi'] == iden and dicel['name']==evt):
                idPart = int(input("Enter the id of theParticipant: "))
                if(validaciones.partc_exists(dicel['participants'],idPart)):
                    for elemento in dicel['participants']:
                        if(elemento['document']==idPart and elemento['contribution']!=True):
                            dicel['participants'].remove(elemento)
                            print(dicel['participants'])
                            break
                    else:
                        print("you finished deleting")
                else:
                    print("participant does not exist")

def add_participants(lista,evt,iden):
    
    if(validaciones.event_exists(lista,evt,iden)):
        for dicEvt in lista:
            print(dicEvt['finished'])
            if(dicEvt['identi']==iden and dicEvt['finished']!=True):
                idPart = int(input("Enter the id of theParticipant: "))
                if(not validaciones.partc_exists(dicEvt['participants'],idPart)):
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
                    dicEvt["participants"].append({
                        "document": idPart,
                        "name":namePar,
                        "age":agePart,
                        "position":positPar,
                        "contribution":pay
                    })
                    print(dicEvt["participants"])
                    break
        else:
            print("this event does not exist or event finished")
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

        impresiones.impr_evts(lista)
    else:
        print("El evento ya existe")
        
def operation_options(opc,lista):
    if(opc==1):
        create_event(lista)
    elif(opc==2):
        idEvt = int(input("Enter the id of the event to add Participants: "))
        evento = input("Enter the event to add the participant: ")
        add_participants(lista,evento,idEvt)
    elif(opc==3):
        evento = input("Enter the event to deleted the participant: ")
        ident = int(input("Enter the id of the particpant to deleted: "))
        deleted_partc_evet(lista,evento,ident)
    elif(opc==4):
        ident = int(input("Enter the id of the event to delete: "))
        event = input("Enter the name of the event to delete: ")
        delet_evt(lista,event,ident)
    elif(opc == 5):
        impr_evts(lista)
        ident = int(input("Enter the id of the event to modify: "))
        event = input("Enter the name event please: ")
        modif_evt(lista,event,ident)
    elif(opc == 6):
        ident = int(input("Enter the id of the event to Consult: "))
        impresiones.imprimi_evt(lista,ident)
    elif(opc == 7):
        ident = int(input("Enter the id of the participant to Consult: "))
        event = int(input("Enter the id of the event to consult"))
        impresiones.imprimi_part(lista,event,ident)
    elif(opc == 8):
        idEvt = int(input("Enter the id of the event to consult: "))
        impresiones.imp_evt_part(lista,idEvt)
    elif(opc == 9):
        idEvt = int(input("Enter the id of the event to consult: "))
        deuda_evt(lista,idEvt)
    elif(opc == 10):
        idEvt = int(input("Enter the id of the event to consult: "))
        impresiones.impr_part_noPay(lista,idEvt)
    elif(opc == 11):
        pass
    elif(opc == 12):
        inte = input("Are you sure you want to go out? y/n: ").lower()
        aser = True if inte == "y" else False
        if(aser):
            return False
        elif(aser==False):
            print("He has not escaped execution")
        else:
            print(f"\033[1;30;41mThe error has occurred\033[0m")
    
    return True



def menu_text():
    print(f"""\033[3;30;41m
╔═════ °❀•°✮°•❀°═════╗
        𝕄enu 𝔸genda
1.  Create Event.
2.  Add Employee-Participant.
3.  Remove Participant.
4.  Delete Event.
5.  Edit Event.
6.  View Event Information.
7.  View Participant Information.
8.  View Event Participants.
9.  View event debt
10. List of participants who have not paid
11. Mark Event as Finished.
12. Exit

╚═════ °❀•°✮°•❀°═════╝       
        \033[0m""")


