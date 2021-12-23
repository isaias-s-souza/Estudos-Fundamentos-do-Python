# 
# Exemplo de acesso a uma base de dados SQLite
#
import pymongo
from pymongo import MongoClient

def manipulaDadosMongoDB():
    cliente = pymongo.MongoClient('mongodb+srv://sa:DcIZay@cluster0.zwb6v.mongodb.net/myFirstDatabase?retryWrites=true"&"w=majority')
    db      = cliente.conheca_python

    for i in range(1, 10):
        objDit = {'codigo' : i} 
        db.conheca_mongodb.insert_one(objDit)

    db.conheca_mongodb.update_one({'codigo' : 2}, {'$set' : {'atributo' : 780}})
    db.conheca_mongodb.deleta_one({'codigo' : 1})

    resultadoConsulta = db.conheca_mongodb.find({})

    for doc in resultadoConsulta:
        print(doc)

manipulaDadosMongoDB()

    

