import os

import requests

API_KEY = os.environ.get("RESTCOUNTRIES_API_KEY")

url = "https://api.restcountries.com/countries/v5/region/Europe?response_fields=names.common,population"
response = requests.get(url, headers={"Authorization": f"Bearer {API_KEY}"})
countries = response.json()["data"]["objects"]

for item in countries[:10]:
    print(item["names"]["common"])
