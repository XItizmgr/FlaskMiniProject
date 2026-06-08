from flask import Flask , render_template , request 
app =Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/submit",methods=['POST'])
def submit():
    username = request.form.get("username")
    password = request.form.get("password")
    
    valid_user = {
        "ram":"123",
        "admin":11
    }
    if username in valid_user and password == valid_user[username]:
        return render_template("welcome.html", name=username)
    else:
        return render_template("invalid.html")