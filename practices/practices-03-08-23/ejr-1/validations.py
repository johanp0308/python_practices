
def emple_exits(idne,emp):
    for key in emp:
        if idne==key:
            return True
    return False

def if_not_exits(file_name):
    try:
        with open(file_name,"r") as file:
            return True
    except FileNotFoundError:
        with open(file_name,"x") as fiel:
            return True
    except Exception:
        return False