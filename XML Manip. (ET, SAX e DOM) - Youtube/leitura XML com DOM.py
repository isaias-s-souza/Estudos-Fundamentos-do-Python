
# coding:utf-8
from xml.dom.minidom import parse
#abriu
doc = parse('CADOC 3040 Exemplo.xml')

xml = doc.documentElement

if xml.hasAttribute('nome'):
	print("Pais: %s" % xml.getAttribute('nome'))

estados = xml.getElementsByTagName('estado')

for info in estados:
    print('*'*10 + 'REG' + '*' * 10)
    if info.hasAttribute('nome'):
        print("Estado: %s" % info.getAttribute('nome'))

        cidades = info.getElementsByTagName('cidade')
        for c_info in cidades:
            if c_info.hasAttribute('nome'):
                print("Cidade: %s" % c_info.getAttribute('nome'))
                
                habitantes = c_info.getElementsByTagName('habitantes')

                if len(habitantes) > 0:
                    print("Populacao de: %s %s hab" % (c_info.getAttribute('nome'),
                                                       habitantes[0].childNodes[0].data ))

                    #Alterar valores
                    habitantes[0].firstChild.nodeValue = 19000
                    print(doc.toxml())