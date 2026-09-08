import requests

url = "https://thisurldoesnotexist.example.com"

try:
    response = requests.get(url, timeout=5)
    if response.status_code != 200:
        print(f"Error: Server responded with status code {response.status_code}.")
    else:
        print(response.json())
except requests.exceptions.RequestException:
    print("Error: Could not reach the server. Check your connection and try again.")
