languages_a = ["Python", "JavaScript", "Java", "C++", "Ruby"]
languages_b = ["JavaScript", "Go", "Rust", "Python", "Swift"]

set_a = set(languages_a)
set_b = set(languages_b)

union = set_a | set_b
intersection = set_a & set_b
difference = set_a - set_b

print(f'Union:        {union}')
print(f'Intersection: {intersection}')
print(f'Difference:   {difference}')
