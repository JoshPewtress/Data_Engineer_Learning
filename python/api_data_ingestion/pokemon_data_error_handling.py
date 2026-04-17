import requests

URL_NAME = "https://pokeapi.co/api/v2/"
POKEMON_LIST = ["pikachu", "ChAriZaRd", "invalidmon", " "]

def get_pokemon_data(name):
    name = name.strip().lower()

    if name:
        url = f"{URL_NAME}pokemon/{name}"
        response = requests.get(url)
        
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Skipping '{name}', no record was found.")
            return None
    else:
        print(f"Skipping '{name}', blank entry.")
        return None

def transform_pokemon_data(pokemon_list):
    output = []

    for item in pokemon_list:
        pokemon = get_pokemon_data(item)
        
        if pokemon:
            poke_id = pokemon["id"]
            name = pokemon["name"]
            weight = pokemon["weight"]

            output.append({
                "id": poke_id,
                "name": name,
                "weight": weight
            })
        
    return output
            

def main():
    pokemon_data = transform_pokemon_data(POKEMON_LIST)

    if pokemon_data:
        print(pokemon_data)

if __name__ == "__main__":
    main()