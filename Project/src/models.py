from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

# Model for Student
class Student(db.Model, UserMixin,):
    id = db.Column(db.Integer, primary_key=True)
    studentId = db.Column(db.Integer, nullable=False, unique=True )
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def toDict(self):
        return {
            "id": self.id,
            "Student Id": self.studentId,
            "Email": self.email,
            "password": self.password
        }

    # hashes the password parameter and stores it in the object
    def set_password(self, password):
        self.password = generate_password_hash(password, method='sha256')

    # Returns true if the parameter is equal to the object's password property
    def check_password(self, password):
        return check_password_hash(self.password, password)

    # To String method
    def _repr_(self):
        return '<Student Id {}>'.format(self.studentID)


# Model for exercise link
class Exercise(db.Model):
    exerciseID = db.Column(db.Integer, primary_key=True)
    exerciseName = db.Column(db.String(120), nullable=False)
    equipment = db.Column(db.String(120), nullable=False)
    exerciseType = db.Column(db.String(120), nullable=False)
    majorMuscle = db.Column(db.String(120), nullable=False)
    minorMuscle = db.Column(db.String(120), nullable=False)
    example = db.Column(db.String(200), nullable=False)
    notes = db.Column(db.String(120), nullable=False)
    mods = db.Column(db.String(120), nullable=False)

    def toDict(self):
        return {
            "id": self.exerciseID,
            "Exercise": self.exerciseName,
            "Equipment": self.equipment,
            "Exercise Type": self.exerciseType,
            "Major Muscle ": self.majorMuscle,
            "Minor Muscle": self.minorMuscle,
            "Example": self.example,
            "Notes": self.notes,
            "Modifications": self.mods
        }


class Routine(db.Model):
    routineID = db.Column(db.Integer, primary_key=True)
    routineName = db.Column(db.String(50), nullable=False)
    userid = db.Column(db.Integer, db.ForeignKey('student.id'))

    def toDict(self):
        return {
            "Routine ID": self.routineID,
            "Routine Name": self.routineName,
        }


class Selected(db.Model):
    selectedID = db.Column(db.Integer, primary_key=True)
    rid = db.Column(db.Integer, db.ForeignKey('routine.routineID'))
    reps = db.Column(db.Integer, nullable=False)
    sets = db.Column(db.Integer, nullable=False)
    eid = db.Column(db.Integer, db.ForeignKey('exercise.exerciseID'))
    exercise = db.relationship('Exercise')

    def toDict(self):
        return {
            "Exercise": self.exercise.toDict(),
            "Reps": self.reps,
            "Sets": self.sets
        }
