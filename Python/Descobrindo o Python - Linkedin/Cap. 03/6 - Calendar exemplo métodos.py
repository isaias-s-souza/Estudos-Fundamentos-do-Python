#
# Arquivo com exemplos de uso de calendários
#
import calendar
def ImprimeMes():
    print("___Meses no ano___")
    for mes in calendar.month_name:
        print(mes)
    
    print("\n")

    print("___Dias na semana___")
    for dia in calendar.day_name:
        print(dia)

ImprimeMes()