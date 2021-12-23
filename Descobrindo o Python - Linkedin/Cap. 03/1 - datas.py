#
# Arquivo com exemplos de manipulação de  datas
#
from datetime import date, datetime
#from datetime import time
#from datetime import datetime

def ManipulaDataHora():
    #Trazendo data de hoje
    hoje = date.today()
    print("Hoje é: " , hoje)

    #trazendo partes da data de hoje
    print("Partes da data: ", hoje.day, hoje.month, hoje.year)
    
    # Trazendo dia da semana pelo dia da semana (começa no 0)
    dias = ["seg", "ter", "qua", "qui", "sex", "sab", "dom",]
    print("Nome abreviado do dia da semana:", dias[hoje.weekday()])
    
    # Trazendo data e hora atual
    data = datetime.now()
    print("Data e Hora: ", data)

    # Trazendo somente hora de um dado datetime
    tempo = datetime.time(data)
    print("Hora atual: ", tempo)

ManipulaDataHora()
