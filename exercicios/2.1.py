numerosRomanos = \
[
    {'0':'', '1': 'C', '2': 'CC', '3': 'CCC', '4': 'CD', '5': 'D', '6': 'DC', '7': 'DCC', '8': 'DCCC', '9': 'CM'},
    {'0':'', '1': 'X', '2': 'XX', '3': 'XXX', '4': 'XL', '5': 'L', '6': 'LX', '7': 'LXX', '8': 'LXXX', '9': 'XC'},
    {'0':'', '1': 'I', '2': 'II', '3': 'III', '4': 'IV', '5': 'V', '6': 'VI', '7': 'VII', '8': 'VIII', '9': 'IX'}
]

numeroDecimal = input('Digite um número: ')
numeroRomano = ''

contadorAlgarismo = 0
for algarismo in numeroDecimal:
    numeroRomano += numerosRomanos[len(numeroDecimal) - 3 + contadorAlgarismo][algarismo]
    contadorAlgarismo += 1

print('Número Romano: ' + numeroRomano)