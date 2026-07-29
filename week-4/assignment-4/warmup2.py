student = {
    "name": "Camila",
    "grade": 10,
    "subjects": ["Math", "Science", "History"],
}

for key, value in student.items():
    print(f'{key}: {value}')

student["graduated"] = False

print(student)
