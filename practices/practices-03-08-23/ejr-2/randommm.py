import random


aletoria = random.randint(50,59) # Numero aletorio con rango


lista = [2,3,4,5,6,8,7]

random.shuffle(lista) # Batidora de listas

a = random.choice(lista) # Escoje algo en una lista aleatoriamente

b = int(random.random()*100) # Aletoria entre 0 1
print(b)