"""Warmup 2: Access Specific JSON Fields"""

import requests

response = requests.get("https://api.agify.io/?name=michael")
data = response.json()

print(f"Name: {data.get('name')}")
print(f"Predicted age: {data.get('age')}")
print(f"Birthday: {data.get('birthday', 'Not available')}")
