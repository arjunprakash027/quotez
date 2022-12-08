import json
from mongo_connect import get_database

dictionary = {
    'books':{
        'name': 'atomic habits',
        'author': 'James clear',
        'link':'https://jamesclear.com/atomic-habits',
        'quotes':['Breakthrough moments are often the result of many previous actions which build up the potential required to unleash a major change',
        'habits often appear to make no difference untill you create a critical threshholdf and unlock a new level of performance',
        ]
    },
}
 
# Serializing json
json_object = json.dumps(dictionary, indent=4)
 
# Writing to sample.json
with open("core_app/sample2.json", "w") as outfile:
    outfile.write(json_object)
print(get_database())