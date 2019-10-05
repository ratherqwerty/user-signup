from flask import Flask, request, redirect, render_template
import os

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/")
def index():
    return render_template("index.html")

def not_valid(field):
    if len(field) < 3 or len(field) > 20 or field.find(" ") != -1:
        return True
    else:
        return False

@app.route("/", methods=["POST"])
def validate():

    username = request.form["username"]
    password1 = request.form["password1"]
    password2 = request.form["password2"]
    email = request.form["email"]

    username_error = ""
    password_error = ""
    email_error = ""

    if not_valid(username):
        username_error = "That is not a valid username"
    
    if not_valid(password1) or not_valid(password2):
        password_error = "That is not a valid password"
        password1 = ""
        password2 = ""
    elif password1 != password2:
        password_error = "Passwords must match"
        password1 = ""
        password2 = ""

    if len(email) == 0:
        email_error = email_error
    elif email.find("@") == -1 or email.find(".") == -1 or len(email) > 20 or len(email) < 3:
        email_error = "That is not a valid email"
       
    if not len(username_error) >=1 and not len(password_error) >= 1 and not len(email_error) >= 1:
        return redirect("/welcome?username={0}".format(username))
    else:
        return render_template("index.html", username_error=username_error, password_error=password_error, email_error=email_error,
        username=username, email=email)

@app.route("/welcome")
def render_welcome():
    #username = request.form["username"]
    username = request.args.get("username")
    #return render_template("welcome.html", username = username)
    return "<h1>Welcome, {0}!</h1>".format(username)



app.run()