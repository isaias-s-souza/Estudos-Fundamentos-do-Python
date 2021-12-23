# 
# Exemplo de acesso a uma base de dados SQLite
#

import sqlite3

def manipulaDados(bancoDados, comando):
    conexao     = sqlite3.connect(bancoDados)
    cursor      = conexao.cursor()
    cursor.execute(comando)
    conexao.commit()
    conexao.close()      

def selecionaDados(bancoDados, comando):
    conexao     = sqlite3.connect(bancoDados)
    cursor      = conexao.cursor()
    cursor.execute(comando)
    linhas      = cursor.fetchall()
    for linha in linhas:
        print(linha)

def ManipulacaoDados():
    comandoInsert   = "INSERT INTO estados (nome_estado, sigla_estado, nome_capital)" \
                    + "values ('São Barto', 'SB', 'São Barto')"
    pathDB          = "C:\\Users\\isaiassouza\\Documents\\Estudos\\Python\\Descobrindo" \
                      "o Python - Linkedin\\Cap. 06\\BancoDeDados.db"
    comandoSelect   = "SELECT nome_estado, sigla_estado, nome_capital FROM estados"

    manipulaDados(pathDB, comandoInsert)
    selecionaDados(pathDB, comandoSelect)

ManipulacaoDados()



