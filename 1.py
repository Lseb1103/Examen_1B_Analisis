import couchdb
frimport couchdb
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
    db = server.create('juegosOlimpicos')
except:
    db = server['juegosOlimpicos']
    
'''===============LOCATIONS=============='''    

#twitterStream.filter(locations=[-92.21,-5.02,-75.19,1.88])  
twitterStream.filter(track=['juegosOlimpicos', 'ecuador'])

#twitterStream.filter(locations=[-84.64,-20.2,-68.65,-0.04])  
twitterStream.filter(track=['juegosOlimpicos', 'peru'])

#twitterStream.filter(locations=[-82.12,-4.23,-66.85,16.06])  
twitterStream.filter(track=['juegosOlimpicos', 'ecuador'])