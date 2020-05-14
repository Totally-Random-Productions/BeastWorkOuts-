from flask import Flask, render_template, request, redirect, url_for, flash
from flask import Flask, render_template, request
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_jwt import JWT, jwt_required, current_identity
from datetime import timedelta
from models import db, Student, Exercise, Routine, Selected
from sqlalchemy.exc import IntegrityError

''' Begin boilerplate code '''


def create_app():
    app = Flask(__name__, template_folder="templates")
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
    app.config['SECRET_KEY'] = "MYSECRET"
    app.config['JWT_EXPIRATION_DELTA'] = timedelta(days=7)
    app.config['JWT_EXPIRATION_DELTA'] = timedelta(days=7)
    db.init_app(app)
    return app


app = create_app()

app.app_context().push()
''' End Boilerplate Code '''

'''Set up JWT here '''


def authenticate(sId, password):
    student = Student.query.filter_by(studentId=sId).first()
    if student and student.check_password(password):
        return


# Payload is a dictionary which is passed to the function by Flask JWT
def identity(payload):
    return Student.query.get(payload['identity'])


jwt = JWT(app, authenticate, identity)

''' End JWT Setup '''


@app.route("/test")
def hello():
    return "Hello World!"


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/signup")
def signupPage():
    return render_template("signup.html")


@app.route("/signup", methods=(['POST']))
def signup():
    if request.method == 'POST':
        userData = request.form.to_dict()
        print(userData)
        if userData:
            newUser = Student(studentId=userData["studentid"], email="email")  # to create a Student object
            newUser.set_password(userData['pass'])  # to set the password
            try:
                db.session.add(newUser)
                db.session.commit()
                return redirect(url_for('workout'))
            except IntegrityError:
                db.session.rollback()
                return 'Username or Email already exists'
        return 200
    return


@app.route("/login", methods=(['GET', 'POST']))
def login():
    userData = request.form.to_dict()

    if request.method == 'GET':
        return render_template('login.html')

    elif request.method == 'POST':
        username = request.form['studentid']
        password = request.form['pass']
        userData = Student.query.filter_by(studentId=username, password=password).first()

    if userData is None:
        flash('Username or Password is invalid')
        return redirect(url_for('signup'))

    login_user(userData)
    flash('Logged in successfully')
    return redirect(url_for('workouts'))


@app.route("/workouts", methods=(['GET']))
def workouts():
    asgs = Exercise.query.all()
    return render_template("workouts.html", exerciselist=asgs)


@app.route("/workouts", methods=(['GET']))
def routine2():
    return redirect(url_for('routine'))


@app.route("/routine", methods=(['GET']))
def routine():
    asgs = Exercise.query.all()
    return render_template("routine.html", exerciselist=asgs)
