import csv
import os
from datetime import date

path = os.path.join('..', 'data', 'expenses.csv')

if not os.path.exists(path):
    print(f"Error: {path} not found.")
else:
    with open(path, 'r') as expenses:
        reader = csv.DictReader(expenses)
        rows = list(reader)

    for row in rows:
        row['amount'] = float(row['amount'])

    food_rows = [row for row in rows if row['category'] == 'Food']
    total = sum(row['amount'] for row in food_rows)
    today = date.today().strftime("%B %d, %Y")

    with open('food_report.txt', 'w') as report:
        report.write(f"Food Expense Report — generated {today}\n")
        for row in food_rows:
            report.write(f"{row['date']}: ${row['amount']:.2f}\n")
        report.write(f"Total: ${total:.2f}\n")
