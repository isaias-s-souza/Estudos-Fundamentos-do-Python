#
# Lendo arquivos com funções do Python
#
def leituraArquivo():
    arquivo = open("ArquivoCriado.txt", "r")

    if(arquivo.mode == "r"):
        conteudo = arquivo.read()
        print(conteudo)

    arquivo.close()

# leituraArquivo()

def leituraArquivoGrande():
    arquivo = open("ArquivoCriado.txt", "r")

    if(arquivo.mode == "r"):
        conteudoTotal = arquivo.readlines()

        for linha in conteudoTotal:
            print(linha)

    arquivo.close()

leituraArquivoGrande()
