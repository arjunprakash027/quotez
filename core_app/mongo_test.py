from pymongo import MongoClient
def get_database():
 
   # Provide the mongodb atlas url to connect python to mongodb using pymongo
   CONNECTION_STRING = "mongodb+srv://arjun:password@cluster0.seqkzq7.mongodb.net/?retryWrites=true&w=majority"
 
   # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
   client = MongoClient(CONNECTION_STRING)
 
   # Create the database for our example (we will use the same database throughout the tutorial
   return client['quotez']
  
# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":   
   mail = {}
   # Get the database
   dbname = get_database()
   #print(dbname)
   collection_name = dbname["mail_subs"]
   #print(collection_name)
#    mail['mail_id'] = 'sushmeekarthick2003@gmail.com'
#    x = collection_name.insert_one(mail)
#    print(x.inserted_id)

    #accesss mail addresses from database
#    mailList = []
#    y = list(dbname.mail_subs.find())
#    for i in y:
#     mailList.append(i['mail_id'])
#    print(mailList)
