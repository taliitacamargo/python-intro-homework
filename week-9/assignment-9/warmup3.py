import requests

url = "https://restcountries.com/v3.1/region/europe?fields=name,population"
response = requests.get(url)
countries = response.json()

for item in countries[:10]:
    print(item["name"]["common"])
