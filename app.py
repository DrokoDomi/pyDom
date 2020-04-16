from flask import Flask, redirect, url_for, render_template, request


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/name/", methods=["POST", "GET"])
def age():
    if request.method == "POST":
        user = request.form["nm"]
        return redirect(url_for("user", usr=user))
    else:
        return render_template("age.html")


@app.route("/name/<usr>/")
def user(usr):
    try:
        usr = int(usr)
    except Exception:
        namelenght = len(usr)
        capusr = usr.title()
        return f"<h1>Hello {capusr}!</h1> <br> Fun Fact: Dein Name hat {namelenght} Buchstaben!"
    else:
        alter = 2020 - usr
        return f"Du wirst/wurdest dieses Jahr {alter} Jahre alt!"

if __name__ == "__main__":
    app.run()
