"""Part 2: Mini-Project - Country Explorer CLI"""

import os
import sys

import requests

API_URL = "https://api.restcountries.com/countries/v5"
API_KEY = os.environ.get("RESTCOUNTRIES_API_KEY")
PAGE_LIMIT = 100


def fetch_countries():
    headers = {"Authorization": f"Bearer {API_KEY}"}
    params = {
        "response_fields": "names.official,capitals,region,population",
        "limit": PAGE_LIMIT,
        "offset": 0,
    }

    objects = []
    try:
        while True:
            response = requests.get(API_URL, headers=headers, params=params, timeout=10)

            if response.status_code != 200:
                print(f"Error: Server responded with status code {response.status_code}.")
                sys.exit(1)

            payload = response.json()["data"]
            objects.extend(payload["objects"])

            if not payload["meta"]["more"]:
                break
            params["offset"] += PAGE_LIMIT
    except requests.exceptions.RequestException:
        print("Error: Could not reach the server. Check your connection and try again.")
        sys.exit(1)

    countries = []
    for obj in objects:
        capitals = obj.get("capitals") or []
        capital = capitals[0]["name"] if capitals else "N/A"
        countries.append(
            {
                "name": obj.get("names", {}).get("official", "N/A"),
                "capital": capital,
                "region": obj.get("region", "N/A"),
                "population": obj.get("population", 0),
            }
        )
    return countries


def print_country(country):
    population = f"{country['population']:,}"
    print(
        f"{country['name']} — Capital: {country['capital']} "
        f"| Region: {country['region']} | Population: {population}"
    )


def search_by_name(countries):
    term = input("Search: ").strip().lower()
    matches = [c for c in countries if term in c["name"].lower()]

    if not matches:
        print("No countries found matching that search term.")
        return

    for country in matches:
        print_country(country)


def filter_by_region(countries):
    region = input("Region: ").strip().lower()
    matches = [c for c in countries if c["region"].lower() == region]

    if not matches:
        print("No countries found in that region.")
        return

    matches.sort(key=lambda c: c["population"], reverse=True)
    for country in matches:
        print_country(country)


def main():
    countries = fetch_countries()

    while True:
        print("\n=== Country Explorer ===")
        print("1. Search by name")
        print("2. Filter by region")
        print("3. Quit")
        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            search_by_name(countries)
        elif choice == "2":
            filter_by_region(countries)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1, 2, or 3.")


if __name__ == "__main__":
    main()
