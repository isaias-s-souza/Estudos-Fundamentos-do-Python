#
# Arquivo com exemplos de uso de calendários
#
import calendar

#criando um calendário no formato de texto
def CalendarioTexto():
    CalendarioTexto = calendar.TextCalendar(calendar.SUNDAY)
    txtCalendario   = CalendarioTexto.formatmonth(2021, 11)
    print(txtCalendario)

CalendarioTexto()

#criando um calendário no formato de texto
def CalendarioHTML():
    CalendarioHTML = calendar.HTMLCalendar(calendar.SUNDAY)
    htmlCalendario   = CalendarioHTML.formatmonth(2021, 11)
    print(htmlCalendario)

# CalendarioHTML()