import pymongo
import scenario
#creating a mongo my_client
#user_name='NkenAllassan'
#password='tonystarkbot'
#mongo_host='0.0.0.0'
#mongo_port='27017'
#mongo_database='stark'
my_client=pymongo.MongoClient("mongodb+srv://NkenAllassan:tonystarkbot@cluster0-4heam.mongodb.net/<dbname>?retryWrites=true&w=majority")
print('succesfully connected')
db=my_client.get_database('stark')
#print('database succesfully created')
people=db.people
#print('collection created')
#person_document={'_id':'allassan',

ret=scenario.book()                   # 'name':ret}

people.update_one({"_id":'painco'},{
"$set":ret
},upsert= True)
print('succesfully update')
