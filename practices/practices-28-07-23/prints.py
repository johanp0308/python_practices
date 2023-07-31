

def print_parts(dic):
    print("     •—————————•°•✿•°•—————————•")
    for id,info in dic:
        print(f"ID:{id} | Name: {info['name']} | Age: {info['age']} | Residence: {info['residence']} | Program: {info['program']}")
    print("     •—————————•°•✿•°•—————————•")

def print_part(id,info):
    print(f"""
     •• <<────≪•◦⚜◦•≫────>> ••
     ID: {id}
     NAME: {info['name']}
     AGE: {info['age']}
     RESIDENCE: {info['residence']}
     PROGRAM: {info['program']}
     •• <<────≪•◦⚜◦•≫────>> ••
          """)
    

def list_par(dic):
    lista = []
    for id,info in dic.items():
        lista.append(f"{id}|{info['name']}|{info['age']}|{info['residence']}|{info['program']}\n")
    return lista

