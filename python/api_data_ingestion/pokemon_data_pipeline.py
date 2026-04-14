import requests
import json

URL_NAME = "https://pokeapi.co/api/v2/"
POKEMON_LIST = ["pikachu", "charizard", "bulbasaur"]

def get_pokemon_data(name):
    url = f"{URL_NAME}pokemon/{name.lower()}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Invalid request: {response.status_code}")
        return None

def transform_pokemon_data(pokemon_list):
    output = {}

    for pokemon in pokemon_list:
        pokemon_data = get_pokemon_data(pokemon)

        if pokemon_data:
            output[pokemon_data["name"].capitalize()] = {
                "height": pokemon_data["height"],
                "weight": pokemon_data["weight"],
                "base_experience": pokemon_data["base_experience"]
            }
        else:
            continue

    return output

def create_json_file(file_name, data):
    with open(file_name, "w") as file:
        json.dump(data, file, indent=4)
        print(f"'{file_name}' was created.")

def main():
    pokemon_dictionary = transform_pokemon_data(POKEMON_LIST)
    create_json_file("data/raw/pokemon_data.json", pokemon_dictionary)

if __name__ == "__main__":
    main()