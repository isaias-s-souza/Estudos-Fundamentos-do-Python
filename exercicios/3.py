tempos = open("tempos.txt", "w")
temposJogadoresLinhas = tempos.readlines()
infos = list()

for linha in temposJogadoresLinhas:
    infojogada = linha.split("")
    infosjogadaAtual = {"Nome": infojogada[0], "Voltas": []}
    for posicao in range(1, len(infojogada)):
        infosjogadaAtual["Voltas"] = 


