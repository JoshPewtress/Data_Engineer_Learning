def display_available_types(types):
    print()
    print("Available Pokémon types:")
    for t in types:
        print(f"- {t}")
    print()

def display_pokemon(fetched_data):
    print()

    if not fetched_data:
        print("No Pokémon found for this type.")
        return
    
    pokemon_type = fetched_data[0]["pokemon_type"]
    print(f"{pokemon_type.capitalize()}-type Pokémon:")
    
    for row in fetched_data:
        print(f"{row['name'].capitalize()} - {pokemon_type}")

    print()

def get_type_input(pokemon_types):
    while True:
        type_input = input("Enter a Pokémon type: ").strip().lower()
        
        if type_input in pokemon_types:
            return type_input
        
        print(f"'{type_input}' is not a valid type. Please choose from the list above.")

def is_stop_requested():
    while True:
        user_input = input("Search by type again (Y/N): ").strip().lower()
        if user_input == "y":
            return False
        elif user_input == "n":
            return True
        else:
            print("Please enter 'Y' or 'N'.")

def log(message):
    print(f"[PIPELINE] {message}")