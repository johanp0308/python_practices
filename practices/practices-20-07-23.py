# 1. Escribir una función que reciba un número entero positivo y devuelva su factorial.

# def fact(n):
#     if(n>1):
#         res = n * fact(n-1)
#     else:
#         res = 1
#     return res
# try:

#     num = int(input("Ingrese un numero: "))
#     print(f"Su factorial es de: {fact(num)}")

# except ValueError:
#     print("Ingrese un String")

# 2. Escribir una función que calcule el total de una factura tras aplicarle el IVA. La función debe recibir la cantidad 
# sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la factura. Si se invoca la función sin pasarle el porcentaje 
# de IVA, deberá aplicar un 21%.

# def iva_inc(valor=0, iva=0.21):
#     if(iva>0):
#         total = valor + (valor*iva)
#     elif(iva==0,21):
#         total = valor + (valor*iva)
#     else:
#         print("Valor no valido")
#     return total

# ent = float(input("Ingrese el valor: "))
# ivar = float(input("Ingrese el el iva: "))

# if(ivar==0):
#     print(f"El resultado del iva es de {iva_inc(ent)}")
# elif(ivar>0):
#     print(f"El resultado del iva es de {iva_inc(ent,ivar)}")

# 3. Escribir una función que calcule el área de un cuadrado y otra que calcule el volumen de un cubo usando la primera función.

# def cuadrado(x,y):
#     return x*y

# def cubo(cua,prof):
#     return cua*prof

# while(True):
#     try:
#         alto = float(input("Ingrese el alto: "))
#         anch = float(input("Ingrese el Ancho: "))
#         prof = float(input("Ingrese si Profundidad: "))
    
#         print(f"Su cuadrado es de: {cuadrado(alto,anch)}")
#         print(f"SU cubida es de {cubo(cuadrado(alto,anch),prof)}")
#         break
#     except ValueError:
#         print("Ingreso un valor Incorrecto")

# 4. Escribir una función que reciba una muestra de números en una lista y devuelva su media.

# def media_list(nums):
#     longit = len(nums)
#     mitad = int((longit-1)/2)
#     return nums[mitad]

# lista = [1,2,3,4,5,6]
# print(f"La mitad de la lista es {media_list(lista)}")

# 5. Escribir una función que reciba una muestra de números en una lista y devuelva otra lista con sus cuadrados.

def cuadrado_list(lista):
    listaCua = []
    for i in range(0,len(lista)):
        num = lista[i]
        num = num*num
        listaCua.append(num)
    return listaCua
    
listaa = [2,3,4]
print(cuadrado_list(listaa))

# Adicionalmente, puedes empezar a re organizar todos los ejercicios propuestos hasta el momento con funciones y excepciones!!