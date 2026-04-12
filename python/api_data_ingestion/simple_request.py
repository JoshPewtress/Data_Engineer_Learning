import requests

URL_NAME = "https://pokeapi.co/api/v2/pokemon/"

def get_pokemon_info(name):
    url = f"{URL_NAME}{name.lower()}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Invalid response: {response.status_code}")
        return None

def display_pokemon_info(pokemon):
    print(f"Name: {pokemon['name'].capitalize()}")
    print(f"Base Experience: {pokemon['base_experience']}")
    print(f"Height: {pokemon['height']}")
    print(f"Weight: {pokemon['weight']}")

def main():
    pokemon = "pikachu"
    pokemon_info = get_pokemon_info(pokemon)
    
    if pokemon_info:
        display_pokemon_info(pokemon_info)

if __name__ == "__main__":
    main()