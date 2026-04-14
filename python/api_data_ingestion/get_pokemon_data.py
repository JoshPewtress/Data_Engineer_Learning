import requests

URL_NAME = "https://pokeapi.co/api/v2/"

def get_pokemon_data(name):
    url = f"{URL_NAME}pokemon/{name}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Invalid request: {response.status_code}")
        return None

def transform_pokemon_data(pokemon):
    return {
        "name": pokemon["name"],
        "base_experience": pokemon["base_experience"],
        "height": pokemon["height"],
        "weight": pokemon["weight"]
    }

def main():
    pokemon_name = input("Enter a Pokemon name: ").strip().lower()

    if pokemon_name:
        pokemon_data = get_pokemon_data(pokemon_name)

        if pokemon_data:
            pokemon_dictionary = transform_pokemon_data(pokemon_data)
            print(pokemon_dictionary)

if __name__ == "__main__":
    main()