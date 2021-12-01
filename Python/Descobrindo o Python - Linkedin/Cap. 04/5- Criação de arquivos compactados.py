#
# Exemplos de como trabalhar com arquivos
#
import os
from os import path
import shutil
from shutil import make_archive
from zipfile import ZipFile

#Compacta todos os arquivos de uma determinada pasta
def CriaZipModo1():
    shutil.make_archive("ArquivoCompactado", 
                        "zip", 
                        "C:\\Users\\Isaias Souza\Documents\\Estudos\\Python\\Descobrindo o Python - Linkedin\\Cap. 03")

# Executa Criação total
# CriaZipModo1()

# Compacta alguns arquivos listados
def CriaZipModo2(Arquivos, nomeZip):
    with ZipFile(nomeZip + ".zip", "w") as novoZip:
        for nomearq in Arquivos:
            novoZip.write(nomearq)

#Executa Compatação de determinados arquivos passados
arquivosquedevemsercompactados = [  "ArquivoAlterado.txt", 
                                    "NovoArquivo.txt",
                                    "ArquivoCompactado.zip"]
nomenovoarquivo = "Zip Com Arquivos Escolhidos"
# CriaZipModo2(arquivosquedevemsercompactados, nomenovoarquivo)

def DeletaArquivo():
    os.remove("Zip Com Arquivos Escolhidos.zip")

DeletaArquivo()

