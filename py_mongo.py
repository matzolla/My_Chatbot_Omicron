import pymongo
#from utils import wit_response
#from wit import Wit
#import random
#i imported the wit service inorder to respond to the messages retrieve the intent and entities
#use de intent gotten to get response from our knowledge_base pymongo

#access_token="JFNNF2ZMZNSA2BAT3VVRYVFXSJPNWELC"
#client=Wit(access_token)
my_client=pymongo.MongoClient("mongodb://<NkenAllassan>:<tonystarkbot>@cluster0-shard-00-00-4heam.mongodb.net:27017,cluster0-shard-00-01-4heam.mongodb.net:27017,cluster0-shard-00-02-4heam.mongodb.net:27017/<dbname>?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")
mydb=my_client["mydatabase"]
my_col=mydb["responses"]
#a,b=wit_response(' j"ai la toux')

dict=[{"name":"salutation",
"answer":['bonjour je m''appel stark.Pensez-vous avoir le COVID-19? je suis là pour mener à bien cette investigation','coucou toi ! je m''appel stark.Pensez-vous avoir le COVID-19? je suis là pour mener à bien cette investigation',
'salut! je m''appel stark.Pensez-vous avoir le COVID-19? je suis là pour mener à bien cette investigation',
'hey je m''appel stark.Pensez-vous avoir le COVID-19? je suis là pour mener à bien cette investigation',
'hello je m''appel stark.Pensez-vous avoir le COVID-19? je suis là pour mener à bien cette investigation',
'holla je m''appel stark.Pensez-vous avoir le COVID-19? je suis là pour mener à bien cette investigation',
'bonjour à vous! je m''appel stark.Pensez-vous avoir le COVID-19? je suis là pour mener à bien cette investigation']},{"name": "toux",
"answer":['je comprend que vous ayez la toux','est-ce que vous avez aussi un mal de gorge','santez-vous que c''est une toux sèche?']}]
x=my_col.insert_many(dict)
#doc= my_col.find_one({"name":a[0]})
#print(random.choice(doc['answer']))


def knowledge_base(text):
    doc = my_col.find_one({"name":text})
    result= random.choice(doc['answer'])
    return result

#for i in range(len(a)):
    #print(knowledge_base(a[i]))
#print('the database has been created with the collection my_col the id of our record is')
#print(knowledge_base('bonjour'))
#print(x.inserted_id)
def book():
    ret={
    "name": "",
    "subname":"",
    "title": "",
    }
    return ret

{
"_id":ObjectId("54ce14c9dc4d5f15"),
"name":"bonjour comment aller vous?",
"answer":["bien et vous?","bien et toi?"]
}
