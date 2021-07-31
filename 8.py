import json
from argparse import ArgumentParser
import requests
import pymongo
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from bson import json_util, ObjectId
import couchdb


####### MongoDB connection ######

SERVER = pymongo.MongoClient("mongodb://localhost:27017")

try:
    SERVER.admin.command('ismaster')
    print('MongoDB connection: Success')
except ConnectionFailure as cf:
    print('MongoDB connection: failed', cf)


####### MongoDB Atlas connection ######

CLIENT = pymongo.MongoClient("mongodb+srv://luiSeb:st11032014@cluster0.f1ltd.mongodb.net/admin?retryWrites=true&w=majority")

try:
    CLIENT.admin.command('ismaster')
    print('MongoDB Atlas connection: Success')
except ConnectionFailure as cf:
    print('MongoDB Atlas connection: failed', cf)

try:
    mydb = CLIENT["mongo_to_mongoat1"] #creación de la bd en MongoDB Atlas
    mycol = mydb["onlinecourses"]      #creación de la colección en la bd
except:
    dblist = CLIENT.list_database_names()
    if "mongo_to_mongoat1" in dblist:
        print("The database exists.")
        
SKIPPED = []


###### Runninng ######

db = 'mongotocouch1' #base de datos en MongoDB local

'''Intercambio de archivos'''

if db not in ('admin', 'local','config'): 
    cols = SERVER[db].list_collection_names()  
    for col in cols:
        print('Querying documents from collection {} in database {}'.format(col, db))
        for data in SERVER[db][col].find():  
            try:
                print(data)
                data["_id"] = str(data["id"])
                mycol.insert_one(data)
            
            except TypeError as t:
                print('current document raised error: {}'.format(t))
                SKIPPED.append(documents)  # creating list of skipped documents for later analysis
                continue    # continue to next document
            except Exception as e:
                raise e


# In[ ]:




