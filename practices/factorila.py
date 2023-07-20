# import math
# from turtle import *
# def hearta(k):
#     return 15*math.sin(k)**3
# def heartb(k):
#     return 12*math.cos(k)-5*\
#             math.cos(2*k)-2*\
#             math.cos(3*k)-\
#             math.cos(4*k)
# speed(1000)
# bgcolor("black")
# for i in range(6000):
#     goto(hearta(i)*20,heartb(i)*20)
#     for j in range(5):
#         color("red")
#     goto(0,0)
# done()

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

#####################################3

# a,b = 0,1
# cont = 1
# def fac(a,b):
#     aux=a
#     a=b
#     b=aux+b
#     return a
# while cont<21:
#     print(f"{cont} {fac(a,b)}")
    
#     cont+=1


