def event_exists(dic,evt):
  if(evt in dic):
    return True
  else:
    return False

def partc_exists(lista,idpart):
  for dicio in lista:
    if(dicio["document"] == idpart):
      return True
    else:
      return False

def partc_pay(lista,idPart):
  for dicio in lista:
    if(dicio['contribution'] == True):
      return True
    else:
      return False

def verif_evt_finished(list,evt):
  for elem in list:
    if(elem['name']==evt):
      if(elem['finished'] == evt):
        return True
  return False