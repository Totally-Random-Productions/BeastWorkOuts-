from main import db, Student, Exercise, Routine, Selected, app
import csv

db.create_all(app=app)

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
