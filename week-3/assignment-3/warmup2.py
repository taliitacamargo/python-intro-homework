age = int(input(f'Enter your age: '))

if 0 <= age <= 12: 
    print("You are a child")
elif 13 <= age <= 17:
    print("You are a teen")
elif 18 <= age <= 64:
    print("You are an adult")
else:
    print("You are a senior")
