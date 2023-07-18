# Ejercicios Python (listas y tuplas) para review. Dejados a partir de tema visto en clase (14 de julio 2023):

# 1. Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, 
# Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado 
# en cada asignatura, y después las muestre por pantalla con el mensaje En <asignatura> has 
# sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y <nota> cada 
# una de las correspondientes notas introducidas por el usuario.

# lisAsig = []
# lisNota = []

# ejecutar = True

# while(ejecutar):
#     print("""
# =============================
#     Colegio nuevo mundo
#     1. Agregar Asignatura.
#     2. Ver notas.          
#     3. Salir.\n""")
#     opc = int(input("Ingrese Una Opcion : "))
#     if(opc == 1):
#         asig = input("  Ingrese el nombre de la Asignatura: ")
#         nota = float(input("  Ingrese la nota: "))
#         if(len(lisAsig) == 0):
#             lisAsig.append(asig)
#             lisNota.append(nota)
#             print(lisAsig[:])            
#             print(lisNota[:])
#         else:
#             for i in range(0,len(lisAsig)):
#                 if(asig == lisAsig[i]):
#                     print(asig == lisAsig[i])
#                     print("La asignatura escrita ya existe")
#                 else:
#                     lisAsig.append(asig)
#                     lisNota.append(nota)
#                     # print(lisAsig[:])            
#                     # print(lisNota[:])
#                     break
#     elif(opc == 2):
#         if(len(lisAsig) == 0):
#             print("La lista de asignaturas esta vacia")
#         else:
#             print("== Lista de Asignaturas ==")
#             for i in range(0,len(lisAsig)):
#                 print("=> {asig} => {nota}".format(asig=lisAsig[i],nota=lisNota[i]))
#     elif(opc == 3):
#         ejecutar=False

# 2. Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por 
# pantalla en orden inverso separados por comas.


# numList = [1,2,3,4,5,6,7,8,9,10]
# print(numList[:])
# numList.reverse()

# for i in numList:
#     if(i == numList[-1]):
#         print(i)
#     else:
#         print(i,end=",")
    
# print(*numList,sep=",",end="")  # Version que no sirve

# print(str(numList)[1:-1])

# 3. Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, 
# Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha 
# sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. Al 
# final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.

# Nota:: Considerando que sea de 0.0 a 5.0

# asig = ["Matematicas","Fisica", "Quimica", "Historia", "Lengua"]
# nota = []
# for i in range(0,len(asig)):
#     asignatura = asig[i]
#     canNo = float(input(f"Ingrese su nota de {asignatura}: "))
#     nota.append(canNo)
# print("========================")
# print("Lista de Notas a repetir")
# for i in range(0,len(asignatura)-1):
#     if(nota[i]<3.0):
#         print(' {asignatur} => {note}'.format(asignatur=asig[i], note=nota[i]))

# 4. Escribir un programa que almacene el abecedario en una lista, elimine de la lista 
# las letras que ocupen posiciones múltiplos de 3, y muestre por pantalla la lista resultante.

# abecedario = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
# litAbc = []
# for i in range(0,len(abecedario)):
#     if(i%3!=0):
#         litAbc.append(abecedario[i])

# println(str(litAbc)[1:-1])
        
# 5. Escribir un programa que pida al usuario una palabra y muestre por pantalla si
# es un palíndromo.

# palabra = input("Ingrese un palabra: ")
# palabrareve = palabra
# palabrareve = list(palabrareve)
# palabra = list(palabra)
# palabrareve.reverse()
# if(palabrareve == palabra):
#     print("La palabra es un palindromo:")
#     print(*palabrareve, sep="")


    

# 6. Escribir un programa que pida al usuario una palabra y muestre por pantalla el 
# número de veces que contiene cada vocal.

# palbra2 = input("Ingrese un palabra: ")

# a = palbra2.count("a")
# e = palbra2.count("e")
# i = palbra2.count("i")
# o = palbra2.count("o")
# u = palbra2.count("u")

# print(f'A => {a}, E => {e}, I => {i}, O => {o}, U => {u}')

# 7. Escribir un programa que pregunte por una muestra de números, separados por
# comas, los guarde en una lista y muestre por pantalla su promedio.

nums = input("Ingrese la lista de numeros: ")
lista = nums.split(',')
# lista = list(lista)
# lista.remove(',')
suma = 0
cant = len(lista)
for i in range(0,len(lista)):
    numero = int(lista[i])
    suma += numero

promedio = suma / cant
print(f'Su promedio es de {promedio}')
