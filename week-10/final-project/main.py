import requests

from stats_chart import save_stats_chart


def fetch_pokemon(name):
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
    print("---------------------------")
    print("Name:", pokemon["name"].title())
    print("Height:", pokemon["height"])
    print("Weight:", pokemon["weight"])
    print("Types:", ", ".join(pokemon["types"]))
    print("Stats:")
    for stat_name in pokemon["stats"]:
        print(" ", stat_name, ":", pokemon["stats"][stat_name])
    print("---------------------------")


def run_compare():
    names_input = input("Enter 2 or more Pokemon names, separated by commas: ")
    names = [name.strip() for name in names_input.split(",") if name.strip()]

    if len(names) < 2:
        print("Please enter at least two Pokemon names to compare.")
        return

    pokemon_list = []
    for name in names:
        data = fetch_pokemon(name)
        if data:
            pokemon_list.append(parse_pokemon(data))

    if len(pokemon_list) < 2:
        print("Could not fetch enough valid Pokemon to build a chart.")
        return

    filepath = save_stats_chart(pokemon_list)
    print("Saved stat comparison chart to", filepath)


def main():
    print("Welcome to the PokeDex CLI!")
    print("Type a Pokemon name to look it up.")
    print("Type 'compare' to chart base stats across several Pokemon.")
    print("Type 'quit' to exit.")

    while True:
        name = input("\nPokemon name: ")

        if name.lower() == "quit":
            print("Goodbye!")
            break

        if name.lower() == "compare":
            run_compare()
            continue

        if name.strip() == "":
            print("Please type a Pokemon name.")
            continue

        data = fetch_pokemon(name)
        if data:
            pokemon = parse_pokemon(data)
            display_pokemon(pokemon)


if __name__ == "__main__":
    main()
