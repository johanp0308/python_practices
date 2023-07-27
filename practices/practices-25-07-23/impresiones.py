
def imprimi_evt(lista,iden):
  for dic in lista:
    if(dic['identi']==iden):
      print(f"Event: {dic['identi']} | Name: {dic['name']} | Location: {dic['location']} | Date: {dic['date_month']} Participants {len(dic['participants'])}")

def imprimi_part(lista,idEv,idPAr):
  for dic in lista:
    if(dic['identi']==idEv):
      for dicPar in dic['participants']:
        if(dicPar['document']==idPar):
          print(f"Participant: {dicPar['document']} | Name: {dicPar['name']} | Age: {dicPar['age']} | Position: {dicPar['position']} | Contribution: {True if dicPar['contribution']==True else False}")

def imp_evt_part(lista,idEv):
  print("◈ ━━━━ ◈ Participants ◈ ━━━━ ◈")
  for dicD in lista:
    if(dicD['identi']==idEv):
      for dicPar in dicD['participants']:
        print(f"Participant: {dicPar['document']} | Name: {dicPar['name']} | Age: {dicPar['age']} | Position: {dicPar['position']} | Contribution: {True if dicPar['contribution']==True else False}")
  print("◈ ━━━━━━━━━━━━━━━━━━━━━━━━━━ ◈")

def impr_evts(lista):
  print("◈ ━━━━ ◈ Participants ◈ ━━━━ ◈")
  for dicD in lista:
    for dicPar in dicD['participants']:
      print(f"Participant: {dicPar['document']} | Name: {dicPar['name']} | Age: {dicPar['age']} | Position: {dicPar['position']} | Contribution: {True if dicPar['contribution']==True else False}")
  print("◈ ━━━━━━━━━━━━━━━━━━━━━━━━━━ ◈")

def impr_part_noPay(lista):
  print("◈ ━━━━ ◈ Participants ◈ ━━━━ ◈")
  for dicEle in lista:
    if(dicEle['contribution'] == True):
      print(f"Id: {dicPar['document']} | Name: {dicPar['name']} | Age: {dicPar['age']} | Position: {dicPar['position']} | Contribution: {True if dicPar['contribution']==True else False}")
  print("◈ ━━━━━━━━━━━━━━━━━━━━━━━━━━ ◈")


