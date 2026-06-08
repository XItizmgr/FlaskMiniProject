from flask import Flask, request, Response, redirect, url_for, session


app = Flask(__name__)
app.secret_key = "key"


@app.route("/", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username == "admin" and password == "11":
            session["user"] = username
            return redirect(url_for("welcome"))
        else:
            return Response("ur not the admin")
    return """  
        <h2>Welcome to Login page <h2>
        <form method="POST">
       username: <input name="username" placeholder="Write ur name"></input>
        password :<input name="password" placeholder="Write ur password"></input>
        <input type="submit" value = "login">
        """


@app.route("/welcome")
def welcome():
    if "user" in session:
        return f'''
        <h2>Welocome {session["user"]}!</h2>
        <a href="{url_for("login")}">Logout</a>
        '''
    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))
