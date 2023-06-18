students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name":name , "house": house}
        students.append(student)

for students in sorted(students):
    print(f"{students['name']} is in {students['house']}")