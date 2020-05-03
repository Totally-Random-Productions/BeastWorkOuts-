from app import db, Student, Exercise
import csv

db.create_all(app=app);

'''
with open("database.csv", mode="w") as database:
  account_writer = csv.writer(database, delimiter=",", quotechar='"')

  account_writer.writerow ([studentId, email, password])

  db.session.commit()
  print("Database Initialzed!")
'''

with open("exerciseList.csv", newline="") as workouts:
  result = csv.DictReader(workouts)

  for line in result:

    workoutDetails = Exercise(exerciseName=line["exercise"], equipment =line["equipment "],
    exerciseType=line["exerciseType"], MajorMuscle=line["MajorMuscle"],
    MinorMuscle=line["MinorMuscle"], example=line["example"],
    notes=line["notes"], mods=line["modifications"])

    db.session.add(workoutDetails)
  db.session.commit()
  print("Database Initialzed!")