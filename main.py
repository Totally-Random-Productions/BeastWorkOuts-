import json
from flask import Flask, request
from flask_jwt import JWT, jwt_required, current_identity
from sqlalchemy.exc import IntegrityError
from datetime import timedelta 

from models import db, Student

''' Begin boilerplate code '''
def create_app():
  app = Flask(__name__)
  app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
  app.config['SECRET_KEY'] = "MYSECRET"
  app.config['JWT_EXPIRATION_DELTA'] = timedelta(days = 7) 
  db.init_app(app)
  return app

app = create_app()

app.app_context().push()
db.create_all(app=app)
''' End Boilerplate Code '''

''' Set up JWT here '''
def authenticate(sId, password):
  #search for the specified user
  student = Student.query.filter_by(studentId=sId).first()
  #if user is found and password matches
  if student and student.check_password(password):
    return student

#Payload is a dictionary which is passed to the function by Flask JWT
def identity(payload):
  return Student.query.get(payload['identity'])

jwt = JWT(app, authenticate, identity)

''' End JWT Setup '''
