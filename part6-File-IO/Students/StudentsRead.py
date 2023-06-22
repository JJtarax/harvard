import csv #docs.python.org/3/library/csv.html

students = []

with open("students.csv") as file:
    reader = csv.reader(file)
    for row in csv.DictReader(file):
        students.append({"name": row['name'], "house": row['house'], "home": row['home']})

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} of {student['house']} is from {student['home']}")