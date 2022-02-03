#Lê RNA
rna = input("Digite o RNA:")

#Transforma em uma lista de Trincas
posicaoInicialTrinca = 0
trincas = list()
correspondencia = { 'UUU': 'Phe', 'CUU': 'Leu', 'UUA': 'Leu', 'AAG': 'Lisina', 'UCU': 'Ser', 
                    'UAU': 'Tyr', 'CAA': 'Gln'}
for n_trinca in range(1, (int(len(rna)/3)) + 1):
    trincas.append(rna[posicaoInicialTrinca : n_trinca * 3])
    posicaoInicialTrinca = n_trinca * 3

cadeiaAminoacidos = ''

for trinca in trincas:
    cadeiaAminoacidos += correspondencia[trinca] + '-'

cadeiaAminoacidos = cadeiaAminoacidos[: len(cadeiaAminoacidos) - 1]
print('Cadeia de Aminoácidos: ' + cadeiaAminoacidos)
