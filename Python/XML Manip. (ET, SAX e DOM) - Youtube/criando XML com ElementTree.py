import xml.etree.ElementTree as ET

root        = ET.Element('pycursos')
gtk         = ET.SubElement(root, 'pyGTK')
django      = ET.SubElement(gtk, 'Django')
django.text = 'Django'

arq = ET.ElementTree(root)

#mostra o que temos na memória
# ET.dump(root)

#persiste um xml
arq.write('pycursos_final.xml')

