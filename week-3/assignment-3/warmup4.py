number = int(input(f'enter a number: '))

if number > 0: 
    print(f'{number} is positive')
else: 
    print(f'{number} is negative')

if number % 2 == 0:
    print(f'{number} is even')
else:
    print(f'{number} is odd')