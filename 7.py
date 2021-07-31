
import json
from argparse import ArgumentParser
import requests
import pymongo
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from bson import json_util, ObjectId
import couchdb

######## CouchDB connection #########

URL = 'http://sebas_admin:ng19960105@st11032014:5984/'
print(URL)

try:
    response = requests.get(URL)
    if response.status_code == 200:
        print('CouchDB connection: Success')
    if response.status_code == 401:
        print('CouchDB connection: failed', response.json())
except requests.ConnectionError as e:
    raise e

server=couchdb.Server(URL)


try:
    dbc=server.create('onlinecourses2') # creación de la bd en CouchDB
except:
    dbc=server['onlinecourses2']


########### MongoDB connection ########### 

SERVER = MongoClient('mongodb://localhost:27017')

try:
    SERVER.admin.command('ismaster')
    print('MongoDB connection: Success')
except ConnectionFailure as cf:
    print('MongoDB connection: failed', cf)
    

########### Running ###########

SKIPPED = []

''' Transferencia de archivos '''

db = 'mongotocouch1' # bd en MongoDb local

if db not in ('admin', 'local','config'):  
    cols = SERVER[db].list_collection_names()  
    for col in cols:
        for data in SERVER[db][col].find(): 
            try:
                doc = data
                del(doc["_rev"])
                dbc.save(doc)
            except TypeError as t:
                print('current document raised error: {}'.format(t))
                SKIPPED.append(data)  # creating list of skipped documents for later analysis
                continue    # continue to next document
            except Exception as e:
                raise e


# In[ ]:




