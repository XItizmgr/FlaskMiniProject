from flask import Flask, request,render_template,redirect,url_for

app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form.get("username")
        feedback = request.form.get("feedback")
        return redirect(url_for("thank",name=name,feedback=feedback))
    
    
    return render_template("home.html")

@app.route("/thank")
def thank_you():
    name = request.args.get("name")
    feedback = request.args.get("feedback")
    return render_template('thank.html', name=name, feedback=feedback)