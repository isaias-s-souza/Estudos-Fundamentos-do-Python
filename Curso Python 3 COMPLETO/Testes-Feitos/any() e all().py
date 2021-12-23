listaComTodosItensVerdadeiros   = [True, True, True, True, True, True, True, True, True, True]
listaComAlgumItemVerdadeiro     = [False, False, True, False, False, False, False, False, False]

EstaListaTemTodosItensVerdadeiros   = all(listaComTodosItensVerdadeiros)
EstaListaTemAoMenosUmItemVerdadeiro = any(listaComAlgumItemVerdadeiro)

print(EstaListaTemAoMenosUmItemVerdadeiro)
print(EstaListaTemTodosItensVerdadeiros)