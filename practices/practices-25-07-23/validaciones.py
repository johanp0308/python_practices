def event_exists(dic,evt):
  if(evt in dic):
    return True
  else:
    return False

def partc_exists(list,idpart):
  for dicio in list:
    if(dicio["document"] == idpart):
      return True
    else:
      return False