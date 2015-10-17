from flask import Flask, render_template, request, session, redirect, url_for, session
import time, hashlib, sqlite3
from functools import wraps
from database import *

app = Flask(__name__)


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "username" not in session:
            return redirect(url_for("login"))
        return f(*args, **kwargs)
    return decorated_function


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", s = session)



@app.route("/login", methods = ["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        username = request.form['username']
        password = request.form['password']
    
        m = hashlib.md5()
        m.update(password)
        passhash = m.hexdigest()

        if authenticate(username, passhash):

            session["username"] = username
            return redirect(url_for("home"))
        else:
            error = "Invalid username and password combo"
            return render_template("login.html", err = error) 


    
@app.route("/logout")
@login_required
def logout():
    del session["username"]
    return redirect(url_for('home'))


@app.route("/register", methods = ["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    else:
        username = request.form['username']
        password = request.form['password']

        m = hashlib.md5()
        m.update(password)
        passhash = m.hexdigest()
        if (newUser(username, passhash)):
            return redirect(url_for("login"))

        error = "Username already in use"
        return render_template("register.html", err = error)


@app.route("/browse")
def browseStatic():
    return redirect(url_for("browse", page = 1))

#doesn't do jack
@app.route("/browse/<int:page>")
def browse(page):
    d = {}
    numStories = getNumStories()
    if numStories % 10 == 0:
        d["numpages"] = numStories / 10
    else:
        d["numpages"] = (numStories / 10) + 1

    pg = page
    storyid = (pg - 1) * 10 
    l = []
    cat = []

    for x in range(storyid, storyid + 10):
        story = getStory(storyid)
        if story:
            cat[0] = story[0]
            cat[1] = story[1]
        l.append(cat)
    d["stories"] = l

    return render_template("browse.html", d = d, s = session)



@app.route("/browse/stories/<id>")
def browseStory(id):
    if id == "":
        return redirect(url_for("browse", page = 1))
    else:
        story = getStory(id)
        return render_template("browse.html", story = story, s = session)



@app.route("/create", methods = ["GET", "POST"])
@login_required
def create():
    if request.method == "GET":
        return render_template("create.html", s = session)
    else:
        title = request.form["title"]
        sentence = request.form["begin"]

        if not title or not sentence:
            error = "Please enter something before submitting"
            return render_template("create.html", err = error, s = session)
        else:
            storyid = getNumStories()
            author = session["username"]
            addSentence(storyid, title, author)
            addSentence(storyid, sentence, author)
            return redirect(url_for("browse", page = 1))
        
   
if __name__ == "__main__":
    app.debug = True
    app.secret_key = "potatoes"
    app.run(host = '0.0.0.0', port = 8000)
