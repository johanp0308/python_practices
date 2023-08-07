import validations
from BDempleados import empleados,cargar,descargar,cargar_csv
from datetime import datetime
empe = empleados

def register_empleado():
    empe = descargar("empe.json")
    name = input("Ingrese el nombre del Empleado: ").lower()
    ident = input("Ingrese la identificacion: ")
    cargo = input("Ingrese el cargo del empleado: ").lower()
    telefono = input("Ingrese el telefono del trabajador")    

    empe[ident]={
    "name":name,
    "cargo":cargo,
    "telefono":telefono,
    "isActive": True
    }
    cargar("empe.json",empe)
    return True

def list_emplea():
    empe = descargar("empe.json")
    for id,info in empe.items():
        if(info['isActive']==True):
            print(f"""
    =============================
    Id:       {id}
    Name:     {info['name']}
    Cargo:    {info['cargo']}
    Telefono: {info['telefono']}
            """)
    return True

def mod_emplea():
    try:
        empe = descargar("empe.json")
        iden = input("Ingrese la identificacion del empleado a modificar: ")
        if(validations.emple_exits(iden,empe)):
            name = input("Ingrese el nuevo nombre del empleado: ").lower()
            telefono = input("Ingrese el nuevo telefono: ")
            carg = input("Ingrese el nuevo cargo del emmpleado").lower()
            empe[iden]={"name":name,"cargo":carg,"telefono":telefono,"isActive":True}

            cargar("empe.json",empe)
    except Exception:
        print("Error")
    return True

def desp_empea():
    empe = descargar("empe.json")
    try:
        idn = input("Ingrese la DNI del empleado: ")
        if(validations.emple_exits(idn,empe)):
            empe[idn]['isActive']=False
        else:
            print("No se econtro el empleado!")
        cargar("empe.json",empe)
    except Exception:
        print("Error al despedir!!!!")
    return True
def regis_in_out():
    listValu = []
    idne = ""
    empe = descargar("empe.json")
    idne = input("Ingrese el DNI del empleado a registrar: ")
    if(validations.emple_exits(idne,empe)):
        listValu.append(int(idne))
        if(empe[idne]['isActive']==True):
            
            print("""
            ===================
            1. Entrada.
            2. Salida.
                """)
            try:
                opcion = int(input("Ingrese la Opcion: "))
                adve = "nada"
                if(opcion == 1 or opcion==2):
                    if(opcion == 1):
                        listValu.append("in")
                    else:
                        listValu.append("out")
                    time = datetime.today()
                    moment = time.strftime("%d-%m-%Y|%H:%M")
                    listValu.append(moment)
                    hora = time.hour
                    minuto = time.minute
                    if(opcion == 1):
                        if (hora>8):
                            adve = "llego Tarde"
                        elif(hora==8 and minuto>0):
                            adve = "llego Tarde"
                    else:
                        if hora < 6:
                            adve = "Se fue Temprano"
                    listValu.append(adve)
                    cargar_csv("in_out.csv",listValu)
                else:
                    print("Opcion no valida!!")
            except ValueError:
                print("Ingreso una letra mal")
        else:
            print("EL empleado esta despedido")
    else:
        print("No se encontro el empleado!")
    return True
