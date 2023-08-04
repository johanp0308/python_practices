from data import descargar

def print_paises():
    datos = descargar("paises.json")
    for dic in datos:
        print(f"""
        ===============
            Pais
    Nombre: {dic['pais']}
    Poblacion: {dic['poblacion']}
    Continente:{dic['moneda']}
    Area: {dic['area']}
    =======================
            """)

def cons_pais():
    datos = descargar("paises.json")
    try:
        print("""
    =====================
        Consulta Pais
            """)
        pais = input("Ingrese el pais a consultar: ")
        for dic in datos:
            if(dic['pais']==pais):
                print(f"""
        ===============
            Pais
    Nombre: {dic['pais']}
    Poblacion: {dic['poblacion']}
    Continente:{dic['moneda']}
    Area: {dic['area']}
    =======================
                """)
                
    except Exception:
        print("Erro en la consulta")

def top_poblacion():
    datos = descargar("paises.json")
    mayor = 0
    pais = {}
    for dic in datos:
        if(dic['poblacion']>mayor):
            mayor = dic['poblacion']
            pais = dic['pais']
    print(f"El pais con mas poblacion es: {pais} con un total de {mayor} de habitantes")

def area_menor():
    datos = descargar("paises.json")
    dici = datos[0]
    pais = dici['pais']
    menor = dici['area']
    for dic in datos:
        for i in range(0,len(datos)):
            dic = datos[i]
            if(dic['area'] < menor):
                menor = dic['area']
                pais = dic['pais']
    print(f"El pais con menos area es: {pais} con un total de {menor} de metros cuadrados")
    
def print_cont():
    datos = descargar("paises.json")
    continente = input("Ingrese el contienente: ")
    print(f"< Paises del Conitinente: {continente.capitalize()}>")
    for dic in datos:
        if(continente == dic['continente']):
            print(f"""
    ======================
    Pais:       {dic['pais'].capitalize()}
    Poblacion:  {dic['poblacion']}
    Moneda:     {dic['moneda']}
    Area:       {dic['area']}
                  """)