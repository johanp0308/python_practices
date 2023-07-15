limite = int(input("Ingrese el limite de la sucesion: "))
listaPri = []
i=0
j=1
cont=0

lisPali = []

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



for i in range(0,len(listaPri)):
    num = listaPri[i]
    num = str(num)
    num = list(num)
    revr = listaPri[i]
    revr = str(revr)
    revr = list(revr)
    revr.reverse()
    
    if(num == revr):
        lisPali.append(num)

print(lisPali[:])
