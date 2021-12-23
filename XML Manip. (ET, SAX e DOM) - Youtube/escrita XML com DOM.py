from xml.dom.minidom import Document 
doc = Document()
#<pais>
brasil	    = doc.createElement('pais')

saopaulo	=	doc.createElement('estado')
minasgerais	=	doc.createElement('estado')

caconde	    =	doc.createElement('cidade')
muzambinho	=	doc.createElement('cidade')
guaxupe	    =	doc.createElement('cidade')

#setando atributos das tags 
brasil.setAttribute('nome', 'Brasil') 
saopaulo.setAttribute('nome', 'Sao Paulo') 
minasgerais.setAttribute('nome', 'Minas Gerais') 
caconde.setAttribute('nome', 'Caconde') 
muzambinho.setAttribute('nome', 'Muzambinho') 
guaxupe.setAttribute('nome', 'Guaxupe')

#	Define root como primeiro Child do documentor
#	tambem conhecido como raiz 
doc.appendChild(brasil)

brasil.appendChild(saopaulo) 
brasil.appendChild(minasgerais)

saopaulo.appendChild(caconde) 
minasgerais.appendChild(muzambinho) 
minasgerais.appendChild(guaxupe)

habitantes = doc.createElement('habitantes') 
muzambinho.appendChild(habitantes)

numerohabitantesmuzambinho  = doc.createTextNode('21.000')
habitantes.appendChild(numerohabitantesmuzambinho)

#Cria arquivo XML com indentagao de urn TAB e
#	fim de linha como indicador de nova linha 
doc.writexml(   open('pycursos.xml', 'w'),
                addindent= '	',
                newl= '\n' )

# print("Nome da primeira tag: ", str(doc.firstChild.tagName))
#                 
#destroi todos elementos criados para o doc doc .unlinkQ
doc.unlink()