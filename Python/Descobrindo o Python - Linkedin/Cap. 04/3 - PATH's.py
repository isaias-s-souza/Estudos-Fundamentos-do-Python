#
# Arquivo com exemplos de como trabalhar com paths
#
from os import path
import time
import datetime as dt

def DadosDeDeterminadoArquivo(Arquivo):
    ArquivoExiste   = path.exists(Arquivo)
    EhDiretorio     = path.isdir(Arquivo)
    pathArquivo     = path.realpath(Arquivo)
    pathRelativo    = path.relpath(Arquivo)
    print(path.getctime(Arquivo))
    print(path.getmtime(Arquivo))
    dataCriacao     = dt.datetime.fromtimestamp(path.getctime(Arquivo))
    dataModificacao = dt.datetime.fromtimestamp(path.getmtime(Arquivo))

    print("O arquivo existe." if ArquivoExiste else "O Arquivo não existe")
    print("O caminho passado é um diretório." if EhDiretorio else "O caminho passado não é um diretório.")
    print("O caminho do arquivo é ", pathArquivo)
    print("O caminho relativo passado é", pathRelativo)


    if(ArquivoExiste):
        print("As datas de criação e ultima modificação do arquivo passado são respectivamente ", dataCriacao.strftime("%d/%m/%y"), " ", dataModificacao.strftime("%d/%m/%y"))

caminho = 'C:\\Users\\isaiassouza\\Documents\\Estudos\\Python\\Cap. 03\\5.1 - calendario gerado via python.html'
DadosDeDeterminadoArquivo(caminho)
