from flask import Flask, render_template, request, session, redirect, url_for, session
import time, hashlib

app = Flask(__name__)

userinfo = {"user": "password", "foo": "bar"}


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", s = session)



@app.route("/login", methods = ["GET", "POST"])
def login():
    if "username" in session:
        return redirect(url_for("home"))
    if request.method == "GET":
        return render_template("login.html")
    else:
        username = request.form['username']
        password = request.form['password']

        if username in userinfo:
            if userinfo[username] == password:
                session["username"] = username
                return redirect(url_for("home"))
        error = "Invalid username and password combo"
        return render_template("login.html", err = error)
        
    
"""
        m = hashlib.md5()
        m.update(password)
        passhash = m.hexdigest()
        #if username is in database:
            if authenticate(username, passhash):
            
                session["username"] = username
                return redirect(url_for("home"))
            error = "Invalid username and password combo"
            //return render_template("login.html", err = error) 
            
"""

    
@app.route("/logout")
def logout():
    if "username" in session:
        del session["username"] 
    return redirect(url_for('home'))


@app.route("/register", methods = ["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    else:
        username = request.form['username']
        password = request.form['password']

        # hard coded for testing
        if username in userinfo:
            error = "Username already in use"
            return render_template("register.html", err = error)
        else:
            userinfo[username] = password;
            return redirect(url_for("login"))

# using database functions
"""
        m = hashlib.md5()
        m.update(password)
        passhash = m.hexdigest()
        if (newUser(username, passhash)):
            return redirect(url_for("login"))

        error = "Username already in use"
        return render_template("register.html", err = error)

"""




        
   
if __name__ == "__main__":
    app.debug = True
    app.secret_key = "potatoes"
    app.run(host = '0.0.0.0', port = 8000)
