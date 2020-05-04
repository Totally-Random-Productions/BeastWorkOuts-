from app import db, Student, Exercise, app
import csv

db.create_all(app=app)

with open("database.csv", mode="w") as database:
    account_writer = csv.writer(database, delimiter=",", quotechar='"')

    account_writer.writerow([studentId, email, password])

    db.session.commit()
    print("Student Database Initialized!")

with open("exerciseList.csv", newline="") as workouts:
    result = csv.DictReader(workouts)

    for line in result:
        #if line['Notes'] == '':
            #line['Notes'] = None
        #if line['Modifications'] == '':
            #line['Modifications'] = None

        workoutDetails = Exercise(exerciseName=line["exercise"], equipment=line["equipment "],
                                  exerciseType=line["exerciseType"], MajorMuscle=line["MajorMuscle"],
                                  MinorMuscle=line["MinorMuscle"], example=line["example"],
                                  notes=line["notes"], mods=line["modifications"])
        db.session.add(workoutDetails)
    db.session.commit()
    print("Workout Database Initialized!")
