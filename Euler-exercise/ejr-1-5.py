
# primos = []
# cont = 0
# i=2

# while True:
#     es_primo = True
#     for j in range(1,len(primos)):
#         if(i%primos[j] != 0):
#             es_primo = True
#             break
#         else:
#             es_primo = False
#     if(es_primo):
#         cont += 1
#         primos.append(i)
#         print(f"Numero: {cont} Primo: {i}")
#     i+=1
#     if(cont == 10001):
#         break


# Ejercicio euler 6

# sumaCu = 0
# sumaNa = 0
# for i in range(1,101):
#     sumaCu += (i*i)
#     sumaNa += i
# else:
#     sumaNa *= sumaNa

# print(sumaNa-sumaCu)

# Ejercicio euler 5
# num = []
# i = 1
# while True:
#     for j in range(2,21):
#         if(i%j!=0):
#             break
#     else:
#         num.append(i)
#     if(num!=[]):
#         break
#     i += 1
# print(num)




# Ejercicios euler 4 #######################
# res = 0
# mayor = 0
# for i in range(100,1001):
#     for j in range(100,1000):
#         res = i*j
#         if(str(res)== str(res)[::-1]):
#             # print(f"{i} X {j} = {i*j}")
#             # print(res)
#             if(res>mayor):
#                 mayor = res
# print(mayor)
############################################

#Ejercicio euler 3 ######## Completed
# var = 600851475143
# rango = 600851475143
# mayor = 0
# i = 2
# while True:
#     if(var%i == 0):
#         var /= i
#         mayor = i
#         print(i)
#     if(var==1):
#         break
#     i+=1
# print(mayor)
###########################



# Ejercicio euler 2.########## Completed
a,b = 0,1
suma = 0
while a<4000000:
    a,b = b,a+b
    if(a%2 == 0):
        suma += a

print(f"\n{suma}")
#############################