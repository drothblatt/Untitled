import sqlite3

conn = sqlite3.connect("infos.db")
c = conn.cursor()

# input: username, hash (hexstring) of user's password
# returns: true if the username is NOT in the database, and a user is created
# returns; false if the username has been taken
def newUser(username, passwordHash):
    q="""
    SELECT users.username
    FROM users
    """
    c.execute(q)
    usernames = c.fetchall()
    if len(usernames) == 0:
        q="INSERT INTO users VALUES ('%s','%s')" % (username, passwordHash)
        c.execute(q)
        conn.commit()
        return True
    else:
        return False

# input: username-passwordHash pair
# output: true if the pair match, false if the pair does not
def authenticate(uName, passwordHash):
    q="""
    SELECT users.username, users.password
    FROM users
    WHERE users.username = "%s" and users.password = "%s"
    """ % (uName, passwordHash)
    c.execute(q)
    result = c.fetchall() # turns the result of execute into a list
    if len(result) == 0:
        return False
    else:
        return True;

#print newUser("yeech", "12345")
#print authenticate("yeech", "12345")
#print authenticate("yeech2", "12345")
#print authenticate("yeech", "11111")
