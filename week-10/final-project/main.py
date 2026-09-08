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


if __name__ == "__main__":
    data = fetch_pokemon("pikachu")
    if data:
        print("Connected! Got data for:", data["name"])
