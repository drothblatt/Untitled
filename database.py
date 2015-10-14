import sqlite3

conn = sqlite3.connect("infos.db")
c = conn.cursor()

# input: username
# returns: hash of the user's password (hex string, as it is in the database)
def getUserPassword(username):
    q="""
        SELECT user.password
        FROM user
        WHERE people.username=username
    """
    result  = c.execute(q)
    print result

# input: username, hash (hexstring) of user's password
# returns: true if the username is NOT in the database, and a user is created
# returns; false if the username has been taken
def newUser(username, passwordHash):
    q="""
    SELECT user.username
    FROM user
    """
    usernames=c.execute(q)
    if (username in usernames):
        return False
    else:
        q="""
            insert into user values (username,passwordHash);
            """
            #I don't know how to make this work using the parameters given. Help Plox.
        c.execute(q)

def authenticate(username, passwordHash)
    q="""
    SELECT user.username, user.passwordHash
    FROM user
    WHERE user.username = username and user.passwordHash = passwordHash
    """
    result = c.execute(q)
    if (result= ""):
        return False
    else:
        return True;
