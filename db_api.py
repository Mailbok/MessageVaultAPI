from tinydb import TinyDB, Query

db = TinyDB('db.json')

"""In production this app would preferrably communicate with another db such as
   mongodb or couchbase  - TinyDB was used for prototyping purposes only"""

def persistMessage(password, message):
    currMessage = getMessage(password)

    if currMessage == 'Non-Existent':
        db.insert({'password':password, 'message': message})
        return 'Success'
    else:
        return 'Already Exists'
 

def getMessage(password):
    data = db.search(Query().password == password)
    if len(data) == 0:
        return 'Non-Existent'

    return data[0]['message']