from flask import Flask, render_template

app = Flask(__name__)


@app.route("/test")
def hello():
    return "Hello World!"


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/signup")
def signup():
    return render_template("signup.html")


@app.route("/workouts")
def workouts():
    return render_template("workouts.html")

