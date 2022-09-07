from flask import Flask, request, render_template, redirect
from models.ApiModel import ApiModel
from typing import TypeVar

T = TypeVar("T")
app = Flask(__name__)


@app.get("/")
@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/signin", methods=["POST", "GET"])
def signInApi() -> T:
    """
    register the user in the database
    :return: None
    """
    if request.method == "POST":
        api = ApiModel()
        try:
            values = (
                request.form['name'],
                request.form['email'],
                request.form['password'],
                int(request.form['cpf'])
            )
        except ValueError as e:
            return render_template("register.html")
        else:
            print(values)
            if api.signIn(values):
                return redirect("/login", code=302)
            else:
                return render_template("register.html")
    return render_template("register.html")


if __name__ == '__main__':
    app.run()
