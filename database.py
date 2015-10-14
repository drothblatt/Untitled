import sqlite3

conn = sqlite3.connect("infos.db")
c = conn.cursor()

# input: username
# returns: hash of the user's password (hex string, as it is in the database)
def getUserPassword(username):
# TODO for michael

# input: username, hash (hexstring) of user's password
# returns: true if the username is NOT in the database, and a user is created
# returns; false if the username has been taken
def newUser(username, passwordHash):
# TODO for michael
