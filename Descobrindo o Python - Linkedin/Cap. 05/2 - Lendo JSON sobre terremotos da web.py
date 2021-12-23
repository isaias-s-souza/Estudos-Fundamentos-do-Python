# 
# Exemplo de como processar dados provenientes de um JSON
#

import urllib.request  
import json

def ManipulaJSON():
    #site que retorna um json com informações de terremotos ocorridos no estados unidos
    endereco =      "https://earthquake.usgs.gov/earthquakes/" \
                +   "feed/v1.0/summary/all_hour.geojson"

    webUrl = urllib.request.urlopen(endereco)

    if(webUrl.getcode() == 200):
        dados = webUrl.read()
        #cria dicionário a partir dos dados trazidos da url q ja esta em JSON 
        oJSON = json.loads(dados)

        #pega o conteúdo da chave count que está dentro da chave metadata 
        contagem = oJSON["metadata"]["count"]
        print("Contagem de terremotos: " + str(contagem))

        for local in oJSON["features"]:
            if local["properties"]["place"] == "21 km ESE of Honaunau-Napoopoo, Hawaii":
                print(">**<**>**<Encontrado registro especial >**<**>**<")
            else:
                print(local["properties"]["place"])

ManipulaJSON()


