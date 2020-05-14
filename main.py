from flask import Flask, render_template, request, redirect, url_for, flash
from flask import Flask, render_template, request
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_jwt import JWT, jwt_required, current_identity
from datetime import timedelta

from flask_login import login_user, LoginManager, login_required
from models import db, Student, Exercise, Routine, Selected
from sqlalchemy.exc import IntegrityError

''' Begin boilerplate code '''


login_manager = LoginManager()
@login_manager.user_loader
def load_user(student_id):
    return Student.query.get(student_id)


def create_app():
    app = Flask(__name__, template_folder="templates")
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
    app.config['SECRET_KEY'] = "MYSECRET"
    login_manager.init_app(app)
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
        return student


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
            newUser = Student(studentId=userData["studentid"], email=userData["email"])  # to create a Student object
            newUser.set_password(userData['pass'])  # to set the password
            try:
                db.session.add(newUser)
                db.session.commit()
                return redirect(url_for('login'))
            except IntegrityError:
                db.session.rollback()
                return 'Username already exists'
        return 'Nothing submitted'
    return


@app.route("/login", methods=(['GET', 'POST']))
def login():
    if request.method == 'GET':
        return render_template('login.html')

    elif request.method == 'POST':
        userData = request.form.to_dict()
        print(userData)
        username = userData['studentid']
        password = userData['pass']
        student = Student.query.filter_by(studentId=username).first()
        if student and student.check_password(password):
            flash('Logged in successfully')
            login_user(student)
            return redirect(url_for('workouts'))
        if student is None:
            flash('You haven\'t registered yet')
            return redirect(url_for('signup'))
        flash('Invalid login')
        return redirect(url_for('login'))


@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for('login'))


@app.route("/workouts", methods=(['GET']))
@login_required
def workouts():
    asgs = Exercise.query.all()
    return render_template("workouts.html", exerciselist=asgs)


@app.route("/workouts", methods=(['GET']))
@login_required
def routine2():
    return redirect(url_for('routine'))


@app.route("/routine", methods=(['GET']))
@login_required
def routine():
    asgs = Exercise.query.all()
    return render_template("routine.html", exerciselist=asgs)
