
# ranking = {
#     "atletismo":{1:"1234123",2:"74782",3:"1234823",4:"77782"},
#     "ciclismo":{1:"1234587",2:"45785"},
#     "patinaje":{1:"4568123",2:"78923"}
# }

ranking = {}

def agregar_ranking(progr,id,pos):
    print("hola")
    ranking[progr][pos]=id
    print(ranking)
