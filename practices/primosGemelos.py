# La linea pide al usuario el limite de primos
limite_superior = int(input("Ingrese el límite superior del rango de búsqueda: "))

"""
Aqui se inicializa el for que su recorredor sera @(num)
el for arranca en 2 y llegara a al @(limite_superior)

"""
for num in range(2, limite_superior): 
    # num en su posicion inicial se incrementa en 2: (agarra dos valores por delante)
    if num + 2 <= limite_superior: # Se valida para que no se pase del limite al incrementarlo 
        es_primo_actual = True # Crea un variable booleana que sera el primer primo encontrado
        es_primo_siguiente = True # Cre una segunda que sera gemelo del primer valor

#       Este for es par el primier primo que encuentra
        for i in range(2, num): 
            if num % i == 0: # Esta linea encuentra el numero divisble por num de los i recorrido
                es_primo_actual = False # Cuando encuentra el primer divisor vuelve la variable es_primo_actual a false
                break #rompe el bucle indicando que no es un primo
# Al romper el bucle segun el enunciado su siguiente con dos numeros de diferencia tambien debe ser primo
        for j in range(2, (num + 2)): # Este for inicia de igual forma pero este termina num+2 => osea este es el gemelo que debe encontrar
            if (num + 2) % j == 0: # Esta linea compara pero en la posicion de num con su diferencia de primo de 2 y verifica el divisor de la posicion 
                es_primo_siguiente = False #Esta linea
                break # Rompe el bucle para que no siga indicando que no es un primo
        
# Teniendo encuenta que un primo solo es divisible por 1 y por el mismo al encontrar otro
# divisor entre 2 y num-1 significa que el numero no es primo
# Por eso solo imprimira si ambas validaciones son True
        if es_primo_actual and es_primo_siguiente: # este If usa un and para que obligaotoriamente ambas sean true
            
            # Aqui se usa un tipo de formato para imprimir donde antes del String se pone una f esta indica que
            # Por medio de los corchetes se puede agregar varibles al string sin necesidad de concatenar
            print(f"({num}, {num + 2}) son números primos gemelos.") 