#Solicita el limite de Primos palindromos buscar
limite = int(input("Ingrese un número límite para el rango de búsqueda: "))

# Inicializa una lista donde almacenara los primos palindromos encontrados
numeros_palindromicos = []

# El For arranca en 10 ya que los numero de una cifra no cuenta como palindromos
# Desde 10 hasta el limite pueto por el usuario
for num in range(10, limite):
    es_primo = True  #Crea un variable booleana para indicar que es primo
    
    # La idea de este For es que no encuentre mas divisores entre el rango 1 pero no en 1 hasta el numero-1 dado 
    for i in range(2, num): # Su for arranca desde 2 hasta num-1
        if num % i == 0: # Si encuentra que un numero es divisor en el rango significa que no es primo
            es_primo = False # Esto saltara a False cuando haya un no primo
            break # Rompe el bucle si encuentra el no primo y pasa al siguiente
        

    # aqui al encontrar el primo compara primero el numero convertido a string luego el mismo string invertido con [::-1]
    if es_primo and str(num) == str(num)[::-1]:
        numeros_palindromicos.append(num) # Aqui agrega el num a la lista


print("Números primos palindrómicos encontrados:") # Imprime un mensaje de titulo
for num in numeros_palindromicos: #Crea for que recorrera la lista
    print(num) #Imprime cada elemento de la lista