def display_available_types(rows):
    print()
    print("Available Pokémon types:")
    for row in rows:
        print(f"- {row['pokemon_type']}")
    print()

def display_pokemon(fetched_data, pokemon_type):
    print()
    print(f"{pokemon_type.capitalize()}-type Pokémon:")

    if not fetched_data:
        print("No Pokémon found for this type.")
        return
    
    for row in fetched_data:
        print(f"{row['name'].capitalize()} - {row['pokemon_type']}")

def get_type_input():
    type_input = input("Enter a Pokémon type: ")
    return type_input.strip().lower()

def is_stop_requested():
    while True:
        user_input = input("Search by type again (Y/N): ").strip().lower()
        if user_input == "y":
            return False
        elif user_input == "n":
            return True
        else:
            print("Please enter 'Y' or 'N'.")
