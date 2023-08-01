from ranking import ranking

rank = ranking

def descargar(file_name):
    if validate_file(file_name):       
        newDic = {}
        archivo = open(file_name, "r")
        lista = archivo.readlines()
        for line in lista:
            line = line.split("|")
            info = line[1].split("-")
            info.remove('\n')
            for ele in info:
                ele = ele.split(":")
                if(newDic.get(line[0],True)==True):
                    newDic[line[0]]={int(ele[0]):ele[1]}
                else:
                    newDic[line[0]][int(ele[0])]=ele[1]
                # ele.remove("\n")
        archivo.close()
        
        return newDic
    else:
        return {}

# KEy => Value


def cargar(file_name):
    if validate_file(file_name):            
        archivo = open(file_name, "w")
        for prog,ranked in rank.items():
            archivo.write(f"{prog}|")
            for pos,ide in ranked.items():
                archivo.write(f"{pos}:{ide}-")
            archivo.write("\n")
        archivo.close()

def validate_file(file_name):
    response = False
    try:
        with open(file_name, "r") as file:
            response = True
    except FileNotFoundError:
        with open(file_name, "x"):
            response = True
    except Exception:
        print("Error al manejar el archivo")
    return response 



