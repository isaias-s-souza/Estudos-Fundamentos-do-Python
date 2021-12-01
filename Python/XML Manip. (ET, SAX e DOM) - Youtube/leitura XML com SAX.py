# SAX é uma biblioteca para manipular XML
# SAX é SOMENTE LEITURA
from xml.sax import make_parser
from xml.sax.handler import ContentHandler

#Declarando classe herdada de

class Leitura(ContentHandler):
    def __init__(self):
        ContentHandler.__init__(self)
        self.iden = ''

    #chamado quando encontra nova tag
    def startElement(self, tag, attr):
        self.iden += ' '

        print(self.iden, tag)

        for i in attr.items():
            print(self.iden + ' %s: %s' % i)
    
    def characters(self, txt):
        if txt.strip():
            print(self.iden, txt + "é caracter")
    
    def endElement(self, name):
        self.iden = self.iden[:-2]

p = make_parser()

p.setContentHandler(Leitura())

p.parse('CADOC 3040 Exemplo.xml')