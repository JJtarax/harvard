import csv #docs.python.org/3/library/csv.html

students = []

with open("students.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        students.append({"name": row[0], "house": row[1], "home": row[2]})

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} of {student['house']} is from {student['home']}")