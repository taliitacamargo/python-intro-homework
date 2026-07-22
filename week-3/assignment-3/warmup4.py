number = int(input(f'enter a number: '))

if number > 0: 
    print(f'{number} is positive')
elif number < 0:
    print(f'{number} is negative')
else: 
    print(f'{number} is zero')

if number % 2 == 0:
    print(f'{number} is even')
else:
    print(f'{number} is odd')