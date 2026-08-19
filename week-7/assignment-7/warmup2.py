import csv 

with open('../data/students.csv', 'r') as students:
    reader = csv.DictReader(students)

    for row in reader:
        print(f"{row['name']}: {row['score']}")

