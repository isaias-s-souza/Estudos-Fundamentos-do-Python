import requests

cep = requests.get("https://viacep.com.br/ws/37890000/json/")
if cep.status_code == 200:
    cep = cep.json()
    for info in cep.keys():
        print("{} : {}".format(info, cep[info]))
        

