from flask import Flask, render_template, request
from flask_jwt import JWT, jwt_required, current_identity
from datetime import timedelta
from models import db, Student, Exercise
from sqlalchemy.exc import IntegrityError

''' Begin boilerplate code '''


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
    app.config['SECRET_KEY'] = "MYSECRET"
    app.config['JWT_EXPIRATION_DELTA'] = timedelta(days=7)
    app.config['JWT_EXPIRATION_DELTA'] = timedelta(days=7)
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
    '''userData = request.get_json()  # has to userData from the db to compare
    newUser = Student(userID=userData['Student ID'], email=userData(['Email']))  # to create a Student object
    newUser.set_password(userData['password'])  # to set the password
    try:
        db.session.add(newUser)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return 'Username or Email already exists'

    return render_template("workouts.html")'''
    if request.method == 'POST':
        userData = request.form.to_dict()
        print(userData)
        if userData:
            newUser = Student(studentId=userData['studentid'], email="email")  # to create a Student object
            newUser.set_password(userData['password'])  # to set the password
            try:
                db.session.add(newUser)
                db.session.commit()
            except IntegrityError:
                db.session.rollback()
                return 'Username or Email already exists'
        return 200
    return


@app.route("/login", methods=(['GET', 'POST'])) #this is temporary
def login():
    if request.method == 'GET':
        return render_template('login.html')

    username = request.form['Student ID']

    password = request.form['password']

    registered_user = User.query.filter_by(username=username, password=password).first()

    if registered_user is None:
        flash('Username or Password is invalid')

        return render_template('signup.html')

    login_user(registered_user)

    flash('Logged in successfully')

    return render_template("workouts.html")


@app.route("/workouts", methods=(['GET']))
def workouts():
    asgs = Exercise.query.all()
    return render_template("workouts.html", exerciselist=asgs)


@app.route("/routine", methods=(['GET']))
def routine():
    asgs = Exercise.query.all()
    return render_template("routine.html", exerciselist=asgs)