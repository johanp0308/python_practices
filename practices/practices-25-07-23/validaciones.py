def event_exists(list,evt,iden=0):
  for elem in list:
    if(elem['identi']==iden or elem['name']==evt):
      return True
  return False
      

def partc_exists(lista,idpart):
  for dicio in lista:
    if(dicio["document"] == idpart):
      return True
  return False

def partc_pay(lista,idPart):
  for dicio in lista:
    if(dicio['contribution'] == True):
      return True
  return False

def verif_evt_finished(list,ident):
  for elem in list:
    if(elem['identi']==ident):
      if(elem['finished'] == True):
        return True
  return False

def verif_attri_exist(lista,att):
  for ele in lista:
    if(att in ele):
      return True
  return False