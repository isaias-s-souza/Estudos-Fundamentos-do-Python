import xml.etree.ElementTree as ET

#Abrindo arquivo
doc = ET.parse('pycursos.xml')

root = doc.getroot() # Recupera a tag principal

print(root.tag, root.attrib['nome']) # dicionário

#listar a galera 
for i in root:
    print(i.tag, i.attrib['nome'])

#itera todas tags cidades
for i in root.iter('cidade'):
    print(i.tag, i.attrib['nome'])


