
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

a,b = 0,1
cont = 1
def fac(a,b):
    aux=a
    a=b
    b=aux+b
    return a
while cont<21:
    print(f"{cont} {fac(a,b)}")
    
    cont+=1


