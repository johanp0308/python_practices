def menu_text():
    print("""
===================
    Calculadora 
1. Suma.
2. Resta.
3. Multiplicacion.
4. Potencia.
0. Salir.""")

def calc_(opera,x,y):
    return (opera(x,y))

def suma_(x=0,y=0):
    return x+y
def rest_(x=0,y=0):
    return x-y
def mult_(x=0,y=0):
    return x*y
def pot_(x=0,y=0):
    return x**y

def Opc_exec(operacion):
    x = int(input("Ingrese el primer numero: "))
    y = int(input("Ingrese el segundo: "))

    if(operacion==1):
        return calc_(suma_,x,y)
    elif(operacion==2):
        return calc_(rest_,x,y)
    elif(operacion==3):
        return calc_(mult_,x,y)
    elif(operacion==4):
        return calc_(pot_,x,y)

def _main():
    while True:
        menu_text()
        op = int(input("Ingrese una Opcion: "))
        if(op==0):
            break
        elif(op>0 and op<5):
            print(f"Su resultado es de {Opc_exec(op)}")
        else:
            print("Ingrese una opcion Valida")

_main()