students = [
    {"name": "Jazmine", "score": 88, "subject": "Python"},
    {"name": "Luis",    "score": 74, "subject": "Data"},
    {"name": "Sara",    "score": 91, "subject": "Python"},
    {"name": "Marcus",  "score": 68, "subject": "Web"},
    {"name": "Priya",   "score": 95, "subject": "Data"},
    {"name": "Devon",   "score": 72, "subject": "Python"},
    {"name": "Mia",     "score": 83, "subject": "Web"},
    {"name": "Eli",     "score": 79, "subject": "Data"},
]

top_name = students[0]["name"]
top_score = students[0]["score"]

for student in students:
    if student["score"] > top_score:
        top_score = student["score"]
        top_name = student["name"]

total_score = 0
for student in students:
    total_score += student["score"]
class_average = total_score / len(students)

subjects_offered = set()
for student in students:
    subjects_offered.add(student["subject"])

high_scorers = []
for student in students:
    if student["score"] > 75:
        high_scorers.append(student["name"])

print(f'Top scorer:       {top_name} ({top_score})')
print(f'Class average:    {round(class_average, 1)}')
print(f'Subjects offered: {subjects_offered}')
print(f'High scorers:     {high_scorers}')
