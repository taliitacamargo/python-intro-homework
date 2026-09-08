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


def display_pokemon(pokemon):
    """Print one Pokemon's parsed data in a readable format."""
    print("---------------------------")
    print("Name:", pokemon["name"].title())
    print("Height:", pokemon["height"])
    print("Weight:", pokemon["weight"])
    print("Types:", ", ".join(pokemon["types"]))
    print("Stats:")
    for stat_name in pokemon["stats"]:
        print(" ", stat_name, ":", pokemon["stats"][stat_name])
    print("---------------------------")


def main():
    print("Welcome to the PokeDex CLI!")
    print("Type a Pokemon name to look it up, or type 'quit' to exit.")

    while True:
        name = input("\nPokemon name: ")

        if name.lower() == "quit":
            print("Goodbye!")
            break

        if name.strip() == "":
            print("Please type a Pokemon name.")
            continue

        data = fetch_pokemon(name)
        if data:
            pokemon = parse_pokemon(data)
            display_pokemon(pokemon)


if __name__ == "__main__":
    main()
