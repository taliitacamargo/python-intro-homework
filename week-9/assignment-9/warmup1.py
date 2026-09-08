import requests

response = requests.get("https://api.agify.io/?name=michael")

print(f"Status code: {response.status_code}")
print(f"Response: {response.json()}")
