from django.shortcuts import render
import json
import random
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
    return render(request,'mail_letter.html')
