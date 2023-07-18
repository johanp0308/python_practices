#numero primos gemelos 

limite = int(input("Ingrese el limite de la sucesion: "))
listaPri = []
i=2
cont=0
while i<limite:
    j=1
    while j<=i:
        if(i%j == 0):
            cont+=1
        j+=1
    if(cont==2):
        listaPri.append(i)
    i+=1
    cont = 0
print(listaPri[:])

i = 0
try:
    while i<len(listaPri):
        if(i != len(listaPri)):
            prime = listaPri[i+1]
        else:
            break
        segun = listaPri[i]
        if(prime-segun==2):
            print("({par1},{par2})".format(par1=listaPri[i],par2=listaPri[i+1]))
        i+=1
except:
    print("Termino el programa")
