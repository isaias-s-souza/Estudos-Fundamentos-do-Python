# 
# Exemplo de processamento e parse de HTML
#
from html.parser import HTMLParser
import html
import urllib.request

#Cria classe para exibir informações personalizadas sobre 
# algum arquivo HTML

class meuParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Tag de abertura encontrada.")
        if attrs.__len__() > 0:
            for atributo in attrs:
                print("   Atributo encontrado: ", atributo[0], " = ", atributo[1])
        
    def handle_endtag(self, tag):
        print("Tag de fechamento encontrada.")

    def handle_comment(self, data):
        print("Comentário encontrado.")

    def handle_data(self, data):
        print("Valoes encontrados.")

        if data.isspace():
            print("O valor encontrado é um espaço")
        else:
            print("O valor encontrada é: ", data)

def meuObjeto():
    #Cria Parser
    meuparser   = meuParser()
    #Abre arquivo HTML da pasta
    arquivo     = open("C:\\Users\\Isaias Souza\\Documents\\Estudos\Python\\Descobrindo o Python - Linkedin\\Cap. 05\\exemplohtml.html")
    #Traz texto html para uma string
    dados       = arquivo.read()
    #Executa ações definidas pela classe meuParser() e 
    # ações padrões do HTMLParser() 
    meuparser.feed(dados)

# meuObjeto()

def leHTMLdaNet(site):
    parser = meuParser() 
    
    objurl = urllib.request.urlopen(site)
    # print(objurl)
    h = html.parser
    #código HTTP 200 significa que conectou
    if objurl.getcode() == 200:
        dados = h.escape(objurl.read())
        
        parser.feed(dados)

url = "https://www.kabum.com.br/login"
leHTMLdaNet(url)

