from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()


# Model for Student
class Student(db.Model):
    studentId = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def toDict(self):
        return {
            "Student Id": self.studentId,
            "Email": self.email,
            "Password": self.password
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
    exerciseId = db.Column(db.Integer, primary_key=True)
    exerciseName = db.Column(db.String(120), nullable=False)
    equipment = db.Column(db.String(120), nullable=False)
    exerciseType = db.Column(db.String(120), nullable=False)
    majorMuscle = db.Column(db.String(120), nullable=False)
    minorMuscle = db.Column(db.String(120), nullable=True)
    example = db.Column(db.String(200), nullable=True)
    notes = db.Column(db.String(120), nullable=True)
    mods = db.Column(db.String(120), nullable=True)

    def toDict(self):
        return {
            "id": self.exerciseId,
            "Exercise": self.exerciseName,
            "Equipment": self.equipment,
            "Exercise Type": self.exerciseType,
            "Major Muscle ": self.majorMuscle,
            "Minor Muscle": self.minorMuscle,
            "Example": self.example,
            "Notes": self.notes,
            "Modifications": self.mods
        }


#Workouts Routine Model

'''
class WorkoutRoutine(db.Model):
    workout1 = db.Column(db.String(120), nullable=False)
    workout2 = db.Column(db.String(120), nullable=False)
    workout3 = db.Column(db.String(120), nullable=False)
    workout4 = db.Column(db.String(120), nullable=False)
    workout5 = db.Column(db.String(120), nullable=False)
    workout6 = db.Column(db.String(120), nullable=False)

    def toDict(self):
        return {
            "Workout 1": self.workout1,
            "Workout 2": self.workout2,
            "Workout 3": self.workout3,
            "Workout 4": self.workout4,
            "Workout 5": self.workout5,
            "Workout 6": self.workout6,
        }


'''