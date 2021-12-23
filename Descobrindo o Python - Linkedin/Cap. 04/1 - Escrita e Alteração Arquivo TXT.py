#
# Escrevendo arquivos com funções do Python
#

def EscreveArquivo():
    arquivo = open("ArquivoCriado.txt", "w+")

    arquivo.write("Linha escrita pela funcao 'EscreveArquivo' \r\n")

    arquivo.close()

#EscreveArquivo()


def AlteraArquivo():
    arquivo = open("ArquivoCriado.txt", "a+")

    arquivo.write("Linha escrita pela funcao 'AlteraArquivo' \r\n")

    arquivo.close()

AlteraArquivo()