import os

print(os.getcwd())

path = os.path.join('..', 'data', 'expenses.csv')
print(os.path.exists(path))
print(path)
