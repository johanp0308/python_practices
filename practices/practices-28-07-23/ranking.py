
ranking = {
    "atletismo":{1:"1234123",2:"74782",3:"1234823",4:"77782"},
    "ciclismo":{1:"9865",2:"64984"},
    "patinaje":{1:"4568123",2:"78923"}
}



# ranking = {
#     "atletismo":{},
#     "ciclismo":{},
#     "patinaje":{}
# }

def agregar_ranking(progr,id,pos):
    ranking[progr][pos]=id
    print(ranking)

