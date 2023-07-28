participantes = {
    "1234567890":{"name":"Juan Mariño", "age": 55, "area": "operations", "is paid": False},
    "1234567891":{"name":"Juan Mariño", "age": 56, "area": "operations", "is paid": False},
    "1234567892":{"name":"Juan Mariño", "age": 57, "area": "operations", "is paid": False}
}


def create_data(parti):
    data =  open("data.txt","w",encoding="utf-8")
    
    for key,value in parti.items():
        data.write(f"{key}-{value['name']}-{value['age']}-{value['area']}-{value['is paid']}[")
    data.close()

def restruc_data():
    data = open("data.txt","r",encoding="utf-8")
    newDic = {}
    dic = data.readline()
    dic = dic.split("[")
    dic.remove("")
    for ele in dic:
        resr = ele.split("-")
        print(resr[0])
        newDic[int(resr[0])]={
            "name":resr[1],
            "age":resr[2],
            "area":resr[3],
            "is pad":resr[4]
        }
    data.close()
    return newDic

create_data(participantes)
print(restruc_data())
