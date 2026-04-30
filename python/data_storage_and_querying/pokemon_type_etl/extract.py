import requests

from config import URL_PATH

def get_pokemon_input():
    while True:
        user_input = input("Enter Pokémon names separated by commas: ")
        pokemon_names = [name.strip().lower() for name in user_input.split(",") if name.strip()]
        
        if pokemon_names:
            return pokemon_names
        
        print("No valid Pokémon names entered.")

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