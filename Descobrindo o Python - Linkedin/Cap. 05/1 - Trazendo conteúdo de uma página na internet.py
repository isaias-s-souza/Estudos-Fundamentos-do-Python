# 
# Arquivo com exemplos para manipulação de dados na Internet
#

import urllib.request

#Conecta com determinado site
def ConectaInternet(site):
    
    objurl = urllib.request.urlopen(site)
    # print(objurl)
    #código HTTP 200 significa que conectou
    if objurl.getcode() == 200:
        dados = objurl.read()
        print(dados)

site = "http://www.google.com"
ConectaInternet(site)