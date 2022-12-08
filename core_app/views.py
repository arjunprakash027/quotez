from django.shortcuts import render,redirect
import json
import random
from pymongo import MongoClient
# Create your views here.
def home(request):
    f = open('core_app/sample.json')
    data = json.load(f)
    bookz = ["1"]
    boo = random.choice(bookz)
    quote_numbers = [i for i in range(len(data[boo]['quotes']))]
    quote_number = random.choice(quote_numbers)
    i = data[boo]['quotes'][quote_number]
    author = data[boo]['author']
    book = data[boo]['name']
    link = data[boo]['link']
    print(i)

    f.close()
    return render(request, 'home.html',context={'quotez':i,'author':author,'book':book,'link':link})

def stats(request):
    info = {}
    f = open('core_app/sample.json')
    data = json.load(f)
    bookz = ["1"]
    for boo in bookz:
        book = data[boo]['name']
        i = len(data[boo]['quotes'])
        info["{}".format(book)] = i
    f.close()
    return render(request,'stats.html',context={'information':info})

def mail(request):
    if request.method == 'POST':
        mail_collect = {}
        mailid = request.POST.get('mailid')
        print(mailid)
        db = get_database()
        collection_name = db["mail_subs"]
        print(collection_name)
        print(type(mailid))
        mail_collect['mail_id'] = mailid
        x = collection_name.insert_one(mail_collect)
        print(x.inserted_id)

        return render(request,'mail_letter.html',context={'mailid':mailid})
    return render(request,'mail_letter.html')
    

##non html interacting functions goes here

def get_database():
 
   # Provide the mongodb atlas url to connect python to mongodb using pymongo
   CONNECTION_STRING = "mongodb+srv://arjun:arjun1234@cluster0.seqkzq7.mongodb.net/?retryWrites=true&w=majority"
 
   # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
   client = MongoClient(CONNECTION_STRING)
 
   # Create the database for our example (we will use the same database throughout the tutorial
   return client['quotez']


