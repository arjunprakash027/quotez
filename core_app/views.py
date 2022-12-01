from django.shortcuts import render
import json
# Create your views here.
def home(request):
    f = open('core_app/sample.json')
    data = json.load(f)
    i = data['books']['quotes'][0]
    author = data['books']['author']
    book = data['books']['name']
    print(i)
    f.close()
    return render(request, 'home.html',context={'quotez':i,'author':author,'book':book})