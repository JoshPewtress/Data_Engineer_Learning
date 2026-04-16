import json

FILE_NAME = "data/raw/pokemon_data.json"

def read_json_file(file_name):
    with open(file_name, "r") as file:
        return json.load(file)
    
def filter_by_base_experience(pokemon, min_exp):
    filtered = []

    for key, value in pokemon.items():
        if value["base_experience"] > min_exp:
            height = value["height"]
            weight = value["weight"]
            base_experience = value["base_experience"]

            filtered.append({
                "name": key,
                "height": height,
                "weight": weight,
                "base_experience": base_experience
            })
        
    return {
        "high_experience": filtered,
        "count": len(filtered)
    }

def main():
    pokemon = read_json_file(FILE_NAME)
    filtered_pokemon = filter_by_base_experience(pokemon, 100)
    
    print(filtered_pokemon)

if __name__ == "__main__":
    main()