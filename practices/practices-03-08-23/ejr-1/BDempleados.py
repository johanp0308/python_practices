import json
import validations
import csv
empleados={}

def cargar(file_name,data):
    try:
        with open(file_name,"w") as file:
            json.dump(data,file)
    except FileNotFoundError:
        return False
    except Exception:
        return False

def descargar(file_name):
    try:
        with open(file_name,"r") as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(FileNotFoundError)
        return {}
    except Exception:
        print(Exception)
        return {}


def cargar_csv(file_name,data):
    try:
        if(validations.if_not_exits(file_name)):
            with open(file_name,"a",newline="",encoding="UTF-8") as file:
                mod = csv.writer(file)
                mod.writerow(data)
    except Exception:
        print("Error cargando el CSV")

def descargar_csv(file_name):
    try:
        if(validations.if_not_exits(file_name)):
            listass = []
            with open(file_name,"r") as file:
                title = ['dni','type','time','advetencia']
                data = csv.DictReader(file,fieldnames=title)
                for line in data:
                    listass.append(line)
                print(listass)

    except Exception:
        print("Error descagando")
        