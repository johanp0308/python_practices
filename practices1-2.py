limite = int(input("Ingrese el limite de la sucesion: "))
listaPri = []
i=0
j=1
cont=0

lisPali = []

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
    

# print(listaPri[:])

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
