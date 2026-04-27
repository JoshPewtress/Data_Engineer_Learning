import requests

from config import URL_PATH

def get_pokemon_input():
    user_input = input("Enter Pokémon names separated by commas: ")
    return [name.strip().lower() for name in user_input.split(',') if name.strip()]

def extract(pokemon_names):
    output = []

    for name in pokemon_names:
        name = name.strip().lower().replace(" ", "-")
        
        if not name:
            continue

        url = f"{URL_PATH}pokemon/{name}"
        response = requests.get(url)

        if response.status_code != 200:
            continue

        output.append(response.json())

    return output