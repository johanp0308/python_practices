#numero primos gemelos 

limite = int(input("Ingrese el limite de la sucesion: "))
listaPri = []
i=0
j=1
cont=0
while i<limite:
    j=1
    while j<=i:
        if(i%2 != 0):
            if( i%j == 0):
                cont+=1
        elif(i==2):
            listaPri.append(i)
            break
        j+=1
    
    if(cont==2):
        if(i%3 != 0 and i!=3):
            listaPri.append(i)
        elif(i==3):
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

