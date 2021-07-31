import couchdb
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json


###API ########################
ckey = "SFFA6Wtru67DFk8Ym52BJFS8V"
csecret = "pHLuUWB9ZeskGr52Bln0ovyULmO63wHFHvuEC7jbNmDgCmqAuC"
atoken = "867193866017001472-SRD8xUVikasVg5xmhN0JkbDjVlls9aB"
asecret = "gpPmApPSIwzKqaspdJpdVdZscU1jUsIjLCp7uV0GIOHZ0"
#####################################

class listener(StreamListener):
    
    def on_data(self, data):
        dictTweet = json.loads(data)
        try:
            dictTweet["_id"] = str(dictTweet['id'])
            doc = db.save(dictTweet)
            print ("SAVED" + str(doc) +"=>" + str(data))
        except:
            print ("Already exists")
            pass
        return True
    
    def on_error(self, status):
        print (status)
        
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())

'''========couchdb'=========='''
server = couchdb.Server('http://sebas_admin:ng19960105@st11032014:5984/')  
try:
    db = server.create('juegosOlimpicos2')
except:
    db = server['juegosOlimpicos2']
    
'''===============LOCATIONS=============='''    

#twitterStream.filter(locations=[40.71427,-74.00597])  
twitterStream.filter(track=['juegosOlimpicos', 'ecuador'])