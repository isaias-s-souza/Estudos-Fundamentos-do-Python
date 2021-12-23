#
# Arquivo de exemplo para uso da classe timedeltas
#
import datetime
from datetime import timedelta

def deltaTempo():
    periodo_experiencia = timedelta(days = 90)
    print(periodo_experiencia)

    primeiro_dia = datetime.datetime(2021, 9, 8)
    print("Fim periodo de experiencia:", primeiro_dia + periodo_experiencia)

deltaTempo()