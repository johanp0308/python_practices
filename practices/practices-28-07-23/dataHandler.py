from ranking import ranking

rank = ranking

def cargar(file_name):
    if validate_file(file_name):       
        archivo = open(file_name, "r")
        lista = archivo.readlines()    
        archivo.close()
        part = {}
        
        return part
    else:
        return {}

def guardar(file_name):
    if validate_file(file_name):            
        archivo = open(file_name, "w")
        for prog,ranked in rank:
          archivo.write(f"{prog}|")
          for pos,id in ranked.items():
            archivo.write(":".join([pos,id]))
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