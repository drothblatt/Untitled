from pymongo import MongoClient
import random
import time

"""THIS FILE IS USED TO CREATE THE BACKEND OF THE PROJECT, IT CREATES THE
DATABASE FILE AND CREATES ITS TABLES. ALL FUNCTIONS REGARDING CHANGING THE
DATABASE IS LOCATED AT database.py"""

connection = MongoClient()

db = connection['untitled']

#db.drop_collection("users")
#db.drop_collection("stories")
#db.drop_collection("comments")
#Creates database for users, posts and comments

if ("users" not in db.collection_names()):
    db.create_collection("users")
    
if ("stories" not in db.collection_names()):
    db.create_collection("stories")
        
if ("favorites" not in db.collection_names()):
    db.create_collection("favorites")


q = int(time.time())
db.users.insert({'username': "Guest", 'password': "Guest"})
db.stories.insert({'id': 1, 'sentence': "Heyyo guys, it's a test" ,
                   'author': "Guest", 'time':q})
db.favorites.insert({'id':-1},{'username':"Guest"})

results = db.users.find({'username': "Guest"})
for r in results:
    print r
results = db.stories.find({'author': "Guest"})
for r in results:
    print r
    



"""
COLLECTIONS 
users: username, password
stories: id, sentence, author, time
comments: favorites, id, username
"""

#db.createCollection('users', { 'username': <text>,
#                              'password': <text> } )


#q = "CREATE TABLE %s (%s)" # format string for creating tables,
                           # first formatter = name
                           # second formatter = arguments

#c.execute(q % ("users", "username TEXT, password TEXT")) # NOTE: hex string will do fine for hash

#c.execute(q % ("stories", "id INTEGER, sentence TEXT, author TEXT, time INTEGER"))

#c.execute(q % ("favorites", "id INTEGER, username TEXT"))



#conn.commit()
