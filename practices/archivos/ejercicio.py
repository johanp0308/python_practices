participantes = {
    "1234567890":{"name":"Juan Mariño", "age": 55, "area": "operations", "is paid": False},
    "1234567891":{"name":"Juan Mariño", "age": 56, "area": "operations", "is paid": False},
    "1234567892":{"name":"Juan Mariño", "age": 57, "area": "operations", "is paid": False}
}


def create_data(parti):
    data =  open("data.txt","w",encoding="utf-8")
    
    for key,value in parti.items():
        data.write(f"{key}-{value['name']}-{value['age']}-{value['area']}-{value['is paid']} \n")
    data.close()

def restruc_data():
    data = open("data.txt","r",encoding="utf-8")
    newDic = {}
    for i in range(3):
        dic = data.readline()
        dic = dic.split("-")
        newDic[int(dic[0])]={
            'name':dic[1],
            'age':dic[2],
            'area':dic[3],
            'is paid':bool(dic[4])
        }
    data.close()
    return newDic

create_data(participantes)
print(type(restruc_data()))
