age = int(input(f'Enter your age: '))

if 0 <= age <= 12: 
    category = "Child"
elif 13 <= age <= 17:
    category = "Teen"
elif 18 <= age <= 64:
    category = "Adult"
else:
    category = "Senior"

print(f'You are a {category}')
