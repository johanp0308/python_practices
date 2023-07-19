


# Ejercicios euler 4
res = 0
mayor = 0
for i in range(100,1001):
    for j in range(100,1000):
        res = i*j
        if(str(res)== str(res)[::-1]):
            # print(f"{i} X {j} = {i*j}")
            # print(res)
            if(res>mayor):
                mayor = res
print(mayor)

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
# a,b = 0,1
# suma = 0
# while a<4000000:
#     a,b = b,a+b
#     if(a%2 == 0):
#         suma += a

# print(f"\n{suma}")
#############################