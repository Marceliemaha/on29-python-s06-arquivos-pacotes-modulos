from datetime import datetime

def today(opcao = "sem hora"):
    return   datetime.today().strftime('%d - %m - %y %H:%M:%S') if opcao == "hora" else datetime.today().strftime('%d - %m - %y')


    #return datetime.today().strftime('%d - %m - %y')