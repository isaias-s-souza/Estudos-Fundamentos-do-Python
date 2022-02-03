numerosRomanos = \
{
    'Centena'   : {
                    '0':'', '1': 'C', '2': 'CC', '3': 'CCC', '4': 'CD', '5': 'D', '6': 'DC', '7': 'DCC', 
                    '8': 'DCCC', '9': 'CM'
                  },
    'Dezena'    : {
                    '0':'', '1': 'I', '2': 'II', '3': 'III', '4': 'IV', '5': 'V', '6': 'VI', '7': 'VII', 
                    '8': 'VIII', '9': 'IX'
                  },
    'Unidade'   : {
                    '0':'', '1': 'X', '2': 'XX', '3': 'XXX', '4': 'XL', '5': 'L', '6': 'LX', '7': 'LXX', 
                    '8': 'LXXX', '9': 'XC'
                  }
}

numeroDecimal = input('Digite um número: ')

# É Centena
if len(numeroDecimal) == 3:
    numeroRomano =  numerosRomanos['Centena'][str(numeroDecimal[0])] + \
                    numerosRomanos['Dezena'][str(numeroDecimal[1])] + \
                    numerosRomanos['Unidade'][str(numeroDecimal[2])]
# É Dezena
elif len(numeroDecimal) == 2:
    numeroRomano =  numerosRomanos['Dezena'][str(numeroDecimal[0])] + \
                    numerosRomanos['Unidade'][str(numeroDecimal[1])]
# É Unidade
else:
    numeroRomano =  numerosRomanos['Unidade'][str(numeroDecimal[0])]  

print('Número Romano: ' + numeroRomano)