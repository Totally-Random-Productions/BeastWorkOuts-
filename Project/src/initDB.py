from main import db, Student, Exercise, Routine, app
import csv

db.create_all(app=app);

'''
with open("database.csv", mode="w") as database:
  account_writer = csv.writer(database, delimiter=",", quotechar='"')

  account_writer.writerow ([studentId, email, password])

  db.session.commit()
  print("Database Initialzed!")
'''
'''
with open("exerciseList.csv", newline="") as workouts:
    result = csv.DictReader(workouts)

    for line in result:

        workoutDetails = Exercise(exerciseName=line["exercise"], equipment=line["equipment "],
                                  exerciseType=line["exerciseType"], MajorMuscle=line["MajorMuscle"],
                                  MinorMuscle=line["MinorMuscle"], example=line["example"],
                                  notes=line["notes"], mods=line["modifications"])

        db.session.add(workoutDetails)
    db.session.commit()
    print("Database Initialised!")
'''
with open('exerciseList.csv') as workouts:
    readCSV = csv.reader(workouts, delimiter=',')
    itercsv = iter(readCSV)
    next(itercsv)
    for row in itercsv:
        # Removes the name of the image and leaves url only
        start = "("
        end = ")"
        example = row[5]
        url = example[example.find(start) + len(start):example.rfind(end)]
        # print(url)

        # print(row) For testing, remove when cleaning
        workoutDetails = Exercise(exerciseName=row[0], equipment=row[1],
                                  exerciseType=row[2], majorMuscle=row[3],
                                  minorMuscle=row[4], example=url,
                                  notes=row[6], mods=row[7])

        db.session.add(workoutDetails)
    db.session.commit()
    print("Database Initialised!")
