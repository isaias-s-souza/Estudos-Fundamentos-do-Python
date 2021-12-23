listacoisas = ['tesoura', 'alicate', 'chave', 'limao']
listaEnumerada = list(enumerate(listacoisas))
print(listaEnumerada) # [(0, 'tesoura'), (1, 'alicate'), (2, 'chave'), (3, 'limao')]


#Equivalente a...
listacoisas     = ['tesoura', 'alicate', 'chave', 'limao']
listaposicoes   = [0, 1, 2, 3]
listaEnumerada  = list(zip(listaposicoes, listacoisas)) # [(0, 'tesoura'), (1, 'alicate'), (2, 'chave'), (3, 'limao')]
print(listaEnumerada)