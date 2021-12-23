import requests as rq

id_cidade = "3456412"
key = "06a73c8e768505502cdcb96028b39fae"

url   = "https://api.openweathermap.org/data/2.5/weather?id=" + id_cidade + "&appid=" + key
dados = rq.get(url)
dados = dados.json()

print("Metereologia em Muzambinho (" + str(dados['id']) + ")")
print("Situacao: " + str(dados['weather'][0]["main"]))
print("Temperatura: " + str(round(dados['main']["temp"] - 273, 2)))
print("Sensacao Termica: " + str(round(dados['main']["feels_like"] - 273, 2)))
print("Umidade: " + str(dados['main']["humidity"]) + "%")