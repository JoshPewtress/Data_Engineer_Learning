import requests
import json

URL_NAME = "https://pokeapi.co/api/v2/"
RAW_FILE_PATH = "data/raw/pokemon_data.json"
SUMMARY_FILE_PATH = "data/outputs/pokemon_summary.json"

def get_user_input():
    pokemon_input = []

    user_input = input("Enter Pokémon names separated by ',': ").split(",")
    
    for split_input in user_input:
        pokemon_input.append(split_input.strip())

    return pokemon_input

def write_json_file(file_name, data):
    with open(file_name, "w") as file:
        json.dump(data, file, indent=4)
        print(f"'{file_name}' was created.")

def get_pokemon_data(name):
    name = name.strip().lower()

    if name:
        url = f"{URL_NAME}pokemon/{name}"
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()
        else:
            print(f"{name} not found. Status code {response.status_code}")
            return None
    else:
        print(f"'{name}' was invalid and skipped.")
        return None

def collect_pokemon_data(pokemon_list):
    output = []

    for item in pokemon_list:
        pokemon_data = get_pokemon_data(item)

        if pokemon_data:
            name, height, weight, base_experience = extract_pokemon_fields(pokemon_data)

            output.append(build_pokemon_record(name, height, weight, base_experience))
        else:
            continue
    
    return output

def filter_by_base_experience(pokemon_list, min_exp):
    passing = []
    failing = []

    for pokemon in pokemon_list:
        name, height, weight, base_experience = extract_pokemon_fields(pokemon)

        if base_experience > min_exp:
            passing.append(build_pokemon_record(name, height, weight, base_experience))
        else:
            failing.append(build_pokemon_record(name, height, weight, base_experience))
    
    return passing, failing

def extract_pokemon_fields(pokemon):
    name = pokemon["name"]
    height = pokemon["height"]
    weight = pokemon["weight"]
    base_experience = pokemon["base_experience"]

    return name, height, weight, base_experience

def build_pokemon_record(name, height, weight, base_experience):
    return {
        "name": name,
        "height": height,
        "weight": weight,
        "base_experience": base_experience
    }

def build_pokemon_summary(good_data, bad_data):
    return {
        "high_experience": good_data,
        "low_experience": bad_data,
        "high_experience_count": len(good_data),
        "low_experience_count": len(bad_data)
    }
    
def main():
    pokemon_input = get_user_input()
    
    pokemon_data = collect_pokemon_data(pokemon_input)
        
    if pokemon_data:
        write_json_file(RAW_FILE_PATH, pokemon_data)
        good_data, bad_data = filter_by_base_experience(pokemon_data, 100)
        pokemon_summary = build_pokemon_summary(good_data, bad_data)
        write_json_file(SUMMARY_FILE_PATH, pokemon_summary)
        
if __name__ == "__main__":
    main()