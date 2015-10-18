from flask import Flask, render_template, request, session, redirect, url_for
import time, hashlib, sqlite3
from functools import wraps
from database import *
from datetime import timedelta

app = Flask(__name__)

#app.permanent_session_lifetime = timedelta(minutes = 20)



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
    #session.permanent = True
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
            error = "Invalid username and password combination"
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
            smsg = "You will be redirected to the log-in page in a moment."
            return render_template("register.html", success = smsg);

        error = "Username already in use"
        return render_template("register.html", err = error)


@app.route("/browse")
def browseStatic():
    return redirect(url_for("browse", page = 1))


@app.route("/browse/<int:page>")
def browse(page):
    numStories = getNumStories()
    if numStories % 10 == 0:
        totalPage = numStories / 10
    else:
        totalPage = (numStories / 10) + 1
    pg = page
    storyid = (pg - 1) * 10
    l = []
    cat = []
 
    for x in range(storyid, storyid + 10):
        story = getStory(x)
        if len(story) > 1:
            cat.append(x)
            cat.append(story[0])
            cat.append(story[1])
        else:
            break
        l.insert(0, cat)
        cat = []
        story = []

    return render_template("browse.html", current = page, pages = totalPage, stories = l, s = session)



@app.route("/browse/stories/<id>")
def browseStory(id):
    if not id:
        return redirect(url_for("browse", page = 1))
    else:
        id = int(id)
        story = getStory(id)
        authors = getUniqueUsers(id)
        d = {"title": story[0]}
        st = ""
        for x in range(1, len(story)):
            st += story[x]
        d["story"] = st
        d["authors"] = authors
        return render_template("browse.html", d = d, s = session, pages = 0, edit = True, id = id);

@app.route("/create", methods = ["GET", "POST"])
@login_required
def create():
    if request.method == "GET":
        return render_template("create.html", s = session)
    else:
        title = request.form["title"]
        sentence = request.form["begin"]

        title = title.replace("\'", "&#39;")
        title = title.replace("\"", "&quot;")

        sentence = sentence.replace("\'", "&#39;")
        sentence = sentence.replace("\"", "&quot;")

        if not title or not sentence:
            error = "Please enter something before submitting"
            return render_template("create.html", err = error, s = session)
        else:
            storyid = getNumStories()
            author = session["username"]
            addSentence(storyid, title, author)
            addSentence(storyid, sentence, author)
            return redirect(url_for("browse", page = 1))


@app.route("/edit/<int:id>")
@login_required
def edit(id):
    d = {}
    d["title"] = getStory(id)[0];
    d["story"] = "".join(getStory(id)[1:]);
    return render_template("edit.html", d = d)



@app.route("/edit/<int:id>", methods = ["GET", "POST"])
@login_required
def edit2(id):
    if request.method == "GET":
        return redirect(url_for("edit", id = 1))
    else:
        sentence = request.form["next"]
        sentence = sentence.replace("\'", "&#39;")
        sentence = sentence.replace("\"", "&quot;")

    if not sentence:
        error = "Please enter something before submitting"
        return render_template("edit.html", err = error, s = session)
    else:
        author = session["username"]
        addSentence(id, sentence, author)
        return redirect(url_for("browseStory", id = id))
# TODO


@app.route("/favorite")
@login_required
def favorite():
    storyid = request.form["storyid"]
    username = session["username"]
    addFavorite(storyid, username)
    #more to come


@app.route("/favorites")
@login_required
def favorites():
    username = session["username"]
    faves = getFavorites(username)
    return render_template("favorites.html", s = session, faves = faves)


if __name__ == "__main__":
    app.debug = True
    app.secret_key = "potatoes"
    app.run(host = '0.0.0.0', port = 8000)
