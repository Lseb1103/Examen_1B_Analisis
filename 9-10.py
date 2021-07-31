import json
import csv
import pymongo
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure



####### MongoDB Atlas connection ######

CLIENT = pymongo.MongoClient("mongodb+srv://luiSeb:st11032014@cluster0.f1ltd.mongodb.net/admin?retryWrites=true&w=majority")

try:
    CLIENT.admin.command('ismaster')
    print('MongoDB Atlas connection: Success')
except ConnectionFailure as cf:
    print('MongoDB Atlas connection: failed', cf)


SKIPPED = []


###### Runninng ######

db = "mongo_to_mongoat1"

cols = CLIENT[db].list_collection_names() 
doc = csv.writer(open("datos1.csv", "w"))
for col in cols:
    for data in CLIENT[db][col].find():
        #document = json.dumps(data)
        #doc1 = open(document, "w", encoding = "utf-8")
        #document = json.loads(doc1)
        mydict = {k: unicode(v).encode("utf-8") for k,v in data.items()}
        for key, val in mydict.items():
            try:
                doc.writerow([key, val])
            except TypeError as t:
                print('current document raised error: {}'.format(t))
                SKIPPED.append(documents)  # creating list of skipped documents for later analysis
                continue    # continue to next document
            except Exception as e:
                raise e


# In[ ]:




