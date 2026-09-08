import requests


def fetch_pokemon(name):
    """Get raw Pokemon data from the PokeAPI. Returns None if something goes wrong."""
    url = "https://pokeapi.co/api/v2/pokemon/" + name.lower()

    try:
        response = requests.get(url)
    except requests.exceptions.ConnectionError:
        print("Could not connect to the internet. Please check your connection.")
        return None

    if response.status_code != 200:
        print("Could not find a Pokemon named '" + name + "'.")
        return None

    return response.json()


def parse_pokemon(data):
    """Pull out the fields we care about from the raw API data into a simple dict."""
    types = []
    for type_entry in data.get("types", []):
        types.append(type_entry["type"]["name"])

    stats = {}
    for stat_entry in data.get("stats", []):
        stat_name = stat_entry["stat"]["name"]
        stat_value = stat_entry["base_stat"]
        stats[stat_name] = stat_value

    pokemon = {
        "name": data.get("name", "unknown"),
        "height": data.get("height"),
        "weight": data.get("weight"),
        "types": types,
        "stats": stats,
    }
    return pokemon


if __name__ == "__main__":
    data = fetch_pokemon("pikachu")
    if data:
        print(parse_pokemon(data))
