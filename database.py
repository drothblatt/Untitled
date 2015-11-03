import pymongo
from pymongo import MongoClient
from time import time

# input: username, hash (hexstring) of user's password
# returns: true if the username is NOT in the database, and a user is created
# returns; false if the username has been taken
def newUser(username, passwordHash): # TESTED
    connection = MongoClient()
    db = connection['untitled']

    usernames = db.users.find({'username':username})
    userL = []
    for user in usernames:
        userL.append(user)
    if len(userL) == 0:
        db.users.insert({'username': username, 'password':passwordHash})
        return True
    else:
        return False

def checkUsers(): # TESTED
    connection = MongoClient()
    db = connection['untitled']

    current_users = db.users.find()
    for user in current_users:
        print user
        
# input: username-passwordHash pair
# output: true if the pair match, false if the pair does not

def authenticate(uName, passwordHash):  # TESTED
    connection = MongoClient()
    db = connection['untitled']

    username = db.users.find({'username':uName, 'password':passwordHash})
    userL = []
    for u in username:
        userL.append(u)
    if len(userL) == 0:
        return False
    else:
        return True


def getStory(storyID):
    connection = MongoClient()
    db = connection['untitled']

    #q = """SELECT stories.sentence
    #       FROM stories
    #       WHERE stories.id = ?
    #       ORDER BY time"""
    result = db.stories.find({'id':storyID}).sort(['time',pymongo.DESCENDING])  
    story = []
    for i in result:
        story.append(i.sentence)
    if len(story) == 0:
        return ""
    else:
        return story

    #TESTED: works

def addSentence(storyID, sentence, author):
    connection = MongoClient()
    db = connection['untitled']

    db.stories.insert({'storyID':storyID},{'sentence':sentence},{'author':author})
    #TESTED Works

# return a list of favorite story ids
#def getFavorites(username):
#    conn = sqlite3.connect("infos.db")
#    c = conn.cursor()
#
#    stories = []
#    q = """SELECT favorites.id
#           FROM favorites
#           WHERE favorites.username = '%s'""" % (username)
#    result = c.execute(q).fetchall()
#    return result

def changeFavorite(storyID, username):
    connection = MongoClient()
    db = connection['untitled']
    #q = """SELECT *
    #       FROM favorites
    #       WHERE favorites.username = ? AND favorites.id = ?
    #       """
    result = db.favorites.find({'username':username},{'id':storyID})
    #result = c.execute(q, (username, storyID)).fetchall()
# newly favorited
    if len(result) == 0:
        #q = """INSERT INTO favorites VALUES (?, ?)"""
        #c.execute(q, (storyID, username))
        db.favorites.insert({'id':storyID},{'username':username})
# removes favorite
    else:
        #q = """DELETE FROM favorites
        #       WHERE favorites.username = ? AND favorites.id = ?
        #    """
        #c.execute(q, (username, storyID))
        db.favorites.remove({'username':username},{'id':storyID})
    #conn.commit()

def getUniqueUsers(storyID):
    connection = MongoClient()
    db = connection['untitled']
    result = db.stories.find({'id':storyID})
    #q = """SELECT stories.author
    #       FROM stories
    #       WHERE stories.id = ?
    #       """
    #result = c.execute(q, (storyID,)).fetchall()
    result = set(result)
    result = list(result)
    return result


def getNumStories():
    connection = MongoClient()
    db = connection['untitled']
    result = db.stories.distinct('id')
    #q = """SELECT stories.id
    #       FROM stories
    #       """
    #result = c.execute(q).fetchall()
    length=len(set(result))
    return length;

def getStoryIDsByTime():
    connection = MongoClient()
    db = connection['untitled']
    
    result = db.stories.find().sort(['time',pymongo.DESCENDING])
    #q = """SELECT stories.id
    #       FROM stories
    #       ORDER BY stories.time DESC
    #       """
    #result = c.execute(q).fetchall()
# unique-ify the result, but keep the order
    uqList = []
    for el in result:
        if el[0] not in uqList:
            uqList.append(el[0])
    return uqList

def getFavorites(username):
    connection = MongoClient()
    db = connection['untitled']


    #stories = []
    #q = """SELECT favorites.id
    #       FROM favorites
    #       WHERE favorites.username = ?"""
    result = db.favorites.find({'username':username})
    #result = c.execute(q, (username,)).fetchall()
    return result

def getEditedFavorites(username):
    connection = MongoClient()
    db = connection['untitled']

    result = getStoryIDsByTime()

    stories = []
    #q = """SELECT favorites.id
    #       FROM favorites
    #       WHERE favorites.username = ?"""

    idList = db.favorites.find({'username':username})
    editedFaves = []
    for el in idList:
        lastEdit = getLastEditTime(el[0])
        #q = """SELECT stories.time
        #       FROM stories
        #       WHERE stories.author = ? AND stories.id = ?
        #       ORDER BY stories.time DESC"""
        #myLastEdit = c.execute(q, (username, el[0])).fetchall()
        myLastEdit = db.stories.find({'username':username},{'id':storyID}).sort(['time',pymongo.DESCENDING])
        if len(myLastEdit) > 0:
            myLastEdit = myLastEdit[0][0]
            if lastEdit > myLastEdit:
                editedFaves.append(el)
        else:
            editedFaves.append(el)
    return editedFaves
# input: author
# returns: a list of storyids that the author contributed to sorted in order of
# last time he edited them
def getStoriesByContributor(contributor):
    connection = MongoClient()
    db = connection['untitled']

    #q = """SELECT stories.id
    #       FROM stories
    #       WHERE author=?
    #       ORDER BY stories.time DESC
    #       """

    #result = c.execute(q, (contributor,)).fetchall()
    result = db.stories.find({'author':contributor}).sort(['time',pymongo.DESCENDING])
    uqList = []
    for el in result:
        uqList.append(el[0])
    return uqList

def getLastEditTime(storyID):
    connection = MongoClient()
    db = connection['untitled']

    #q = """SELECT stories.time
    #       FROM stories
    #       WHERE stories.id=?
    #       ORDER BY stories.time DESC"""

    #result = c.execute(q, (storyID,)).fetchall()
    result = db.stories.find({'id':storyID}).sort(['time',pymongo.DESCENDING])
    return result[0][0]

def getLastEditor(storyID):
    connection = MongoClient()
    db = connection['untitled']

    #q = """SELECT stories.author
    #       FROM stories
    #       WHERE stories.id=?
    #       ORDER BY stories.time DESC"""
    db.stories.find({'id':storyID})
    #result = c.execute(q, (storyID,)).fetchall()
    return result[0][0]


print newUser("pralowe","123456")
print "-----"
print checkUsers()
print "-----"
print authenticate("david_r", "hello123")
print "______"
print getStory(1)

"""
print newUser("yeech", "12345")
print authenticate("yeech", "12345")
#print authenticate("yeech2", "12345")
#print authenticate("yeech", "11111")
addSentence(1,"HI! This is a sentence!","yeech")
addSentence(2,"HI! This is a sentence in the second story","yeech")
addSentence(1,"HI! This is the second sentence in the first story","yeech")
addSentence(2,"HI! This is the second sentence in the second story","yeech")
addSentence(3,"HI! This is the first sentence in the third story","michael")
addSentence(2,"HI! This is the second sentence in the second story","yeech")
addSentence(1,"HI! This is the second sentence in the first story","yeech")
addSentence(3,"HI! This is the second sentence in the first story","yeech")
addSentence(3,"HI! This is the second sentence in the first story","yeech")
print getStory(1)
print getStory(2)
#addFavorite("yeech",2)
#getFavorites("yeech")
print getStoryIDsByTime()
"""
