# 3. (40 puntos) Cree un programa que dibuje una silla de nx10 donde n (número pedido al usuario) es el alto de la silla y siempre debe 
# ser impar y mayor o igual a 11. El asiento de la silla siempre debe estar la mitad de la altura. Por ejemplo si el número ingresado 
# es 11 la salida debería ser:

# *
# *
# *
# *
# *
# **********
# *              *
# *              *
# *              *
# *              *
# *              *

# while True:
#     try:
#         ingre = int(input("Ingrese algo:"))
#         if(ingre % 2 != 0 and ingre>=11):
#             mitad = ingre // 2
#             for i in range(0,ingre):
#                 if(i>mitad):
#                     print('*' + 8*' ' + '*')
#                     # print(10*" ")
#                 elif(i==(mitad)):
#                     print(10*"*")
#                 else:
#                     print("*")
#         break
#     except ValueError:
#         print("Ingreso algo mal, bruto")


import os

campus = {

"Sputnik": {"activity": "classes", "students access": True, "schedule": "6 am to 10 pm", "capacity": 35},

"Artemis": {"activity": "classes", "students access": True, "schedule": "6 am to 10 pm", "capacity": 30},

"Apollo": {"activity": "classes", "students access": True, "schedule": "6 am to 10 pm", "capacity": 30},

"Houston": {"activity": "teachers room", "students access": False, "schedule": "when teachers need", "capacity": 6},

"Review": {"activity": "skills review", "students access": True, "schedule": "24/7", "capacity": 100}

}

def menu_tex():
    print("::: 🧡 ━━━━━━━━━━━━━━ 🧡 :::")
    print("¡Bienvenido! \n A continuacion seleccione una opcion:")
    print("1.Mostrar espacios que tienen Acceso Los Campers. ")
    print("2.Mostrar espacios permitidos si el Camper NO se encuentra en horario de clases.")
    print("3.Mostrar espacios donde NO puede 3 el Camper.")
    print("4.Promedio De la capacidad de los espacios en clase.")
    print("**\n")
    

def operaciones_opc(opcion):
    
    if(opcion==1):
        
        for keyEspacio , dicEspacio in campus.items():
                     
            
            
            for keyAct , valor in dicEspacio.items():
                
                if(keyAct=="students access"):
                    
                    if(valor == True):
                        
                        print(f"Espacion Accesso {keyEspacio}")
    
def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def main():
    ejecucion =True
    while ejecucion:
        try:
            menu_tex()
            opc = int(input("Ingrese una opcion: "))
            if(opc>0 and opc<5):
                operaciones_opc(opc)
                
            clear()
        except ValueError:
            print("gono")
                
main()