import sys

import requests

API_URL = "https://restcountries.com/v3.1/all?fields=name,capital,region,population"


def fetch_countries():
    try:
        response = requests.get(API_URL, timeout=10)
    except requests.exceptions.RequestException:
        print("Error: Could not reach the server. Check your connection and try again.")
        sys.exit(1)

    if response.status_code != 200:
        print(f"Error: Server responded with status code {response.status_code}.")
        sys.exit(1)

    data = response.json()

    countries = []
    for item in data:
        capital_list = item.get("capital")
        capital = capital_list[0] if capital_list else "N/A"
        countries.append(
            {
                "name": item["name"]["common"],
                "capital": capital,
                "region": item.get("region", "N/A"),
                "population": item.get("population", 0),
            }
        )
    return countries


def print_country(country):
    population = f"{country['population']:,}"
    print(
        f"{country['name']} — Capital: {country['capital']} "
        f"| Region: {country['region']} | Population: {population}"
    )


def get_population(country):
    return country["population"]


def search_by_name(countries):
    term = input("Search: ").strip().lower()
    matches = []
    for country in countries:
        if term in country["name"].lower():
            matches.append(country)

    if not matches:
        print("No countries found matching that search term.")
        return

    for country in matches:
        print_country(country)


def filter_by_region(countries):
    region = input("Region: ").strip().lower()
    matches = []
    for country in countries:
        if country["region"].lower() == region:
            matches.append(country)

    if not matches:
        print("No countries found in that region.")
        return

    matches.sort(key=get_population, reverse=True)
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
