#
# Exemplos de como trabalhar com arquivos
#
import os
from os import path
import shutil #High-level file operations

def copiaArquivo():
    if path.exists("ArquivoCriado.txt"):
        pathAtual   = path.realpath("ArquivoCriado.txt") # caminho inteiro real
        novoPath    = pathAtual + ".bkp"
        shutil.copy(pathAtual, novoPath)

        #Copia também todas as permissões do arquivo
        shutil.copystat(pathAtual, novoPath)

# copiaArquivo()

def renomearArquivo():
    if path.exists("ArquivoCriado.txt.bkp"):
        # Renomeia(OldName, NewName)
        os.rename("ArquivoCriado.txt.bkp", "ArquivoAlterado.txt")

renomearArquivo()
