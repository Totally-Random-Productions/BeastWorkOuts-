from flask import Flask, render_template
#from flask_jwt import JWT, jwt_required, current_identity
from datetime import timedelta
<<<<<<< HEAD:Project/src/main.py
from models import db, Student
=======

from models import db, Student, Exercise

>>>>>>> AM_Branch:Project/src/app.py

''' Begin boilerplate code '''


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
    app.config['SECRET_KEY'] = "MYSECRET"
<<<<<<< HEAD:Project/src/main.py
    app.config['JWT_EXPIRATION_DELTA'] = timedelta(days = 7)
=======
    app.config['JWT_EXPIRATION_DELTA'] = timedelta(days=7)
>>>>>>> AM_Branch:Project/src/app.py
    db.init_app(app)
    return app


app = create_app()

app.app_context().push()
# db.create_all(app=app)
''' End Boilerplate Code '''

'''Set up JWT here '''


def authenticate(sId, password):
    student = Student.query.filter_by(studentId=sId).first()
    if student and student.check_password(password):
        return


# Payload is a dictionary which is passed to the function by Flask JWT
def identity(payload):
<<<<<<< HEAD:Project/src/main.py
    return Student.query.get(payload['identity'])

=======
    # return Student.query.get(payload['identity'])
    return
>>>>>>> AM_Branch:Project/src/app.py


# jwt = JWT(app, authenticate, identity)


''' End JWT Setup '''


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
