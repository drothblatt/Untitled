from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)

userinfo = {"user": "password", "foo": "bar"}

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")



@app.route("/login", methods = ["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        username = request.form['username']
        password = request.form['password']

        if username in userinfo:
            if userinfo[username] == password
                session[username] = True
                return redirect(url_for("home"))
            error = "Invalid username and password combo"
            return render_template("login.html", error = error)
        else:
            return redirect(url_for("register"))
"""
        //if username is in database:
            //if username/password combo valid:
                session[username] = True
                return redirect(url_for("home"))
            error = "Invalid username and password combo"
            //return render_template("login.html", error = error) error = 
            
        //else:
            //return redirect(url_for("register"))
"""

    
@app.route("/logout")
def logout():
    session[username] = False
    return redirect(url_for('home'))


@app.route("/register", methods = ["GET", "POST"])
def register():
     if request.method == "GET":
        return render_template("register.html")
    else:
        username = request.form['username']
        password = request.form['password']

        if username in userinfo:
            error = "Username already in use"
            return render_template("register.html", error = error)
        else:
            userinfo[username] = password;
            return redirect(url_for("login"))

"""
        //if username in database:
            error = "Username already in use"
            return render_template("register.html", error = error)
        else:
            //add user to database
            return redirect(url_for("login"))
"""



        
   
if __name__ == "__main__":
    app.debug = True
    app.secret_key = "potatoes"
    app.run(host = '0.0.0.0', port = 8000)
