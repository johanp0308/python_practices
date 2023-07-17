

fruti = {'platano':0.1,'21d21':212,'asdqw':22}

fruti['platano']= 2.60

# print(fruti['platano'])

fruti['melon'] =3

# print(fruti)

######### Functions ########################

def homework_task(name, lenguage):
    print("Hola mundo, desde una funcion: ")
    print("Declare a variable in python")
    print("Hello! {namep} this is a function in {lenguages}".format(namep=name,lenguages=lenguage))
    
# print("Start")
# homework_task(lenguage="Python",name="Pachon")
# print("End")

def path(v,t):
    return v*t

S = path(43,34)
print(S)

##################################

# Asi se puede manejar multiples Excepciones en el codigo

try:
    innt = int(input("Ingrese un entero"))
    numero = 30
    prce = numero/innt
    print(innt)    
except ValueError:
    print("You value  is not an integer")
except ZeroDivisionError:
    print("You cannot divide by zero")