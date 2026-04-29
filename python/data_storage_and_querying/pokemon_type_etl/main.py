from database import create_connection
from pokemon_repository import PokemonRepository
from extract import extract, get_pokemon_input
from transform import transform
from display import display_available_types, display_pokemon, get_type_input, is_stop_requested


def main():
    conn = create_connection()
    repo = PokemonRepository(conn)

    pokemon_input = get_pokemon_input()
    if not pokemon_input:
        print("No valid Pokémon names entered.")
        conn.close()
        return

    print("Extracting data...")
    raw = extract(pokemon_input)
    if not raw:
        print("No valid Pokémon data found.")
        conn.close()
        return

    print("Transforming data...")
    transformed = transform(raw)

    repo.create_tables()
    repo.clear_tables()

    print("Loading data...")
    repo.load(transformed)

    pokemon_types = repo.get_available_types()

    stop_requested = False
    while not stop_requested:
        display_available_types(pokemon_types)

        type_input = get_type_input()
        if not type_input:
            print("No Pokémon type entered.")
            conn.close()
            return

        fetched_data = repo.get_pokemon_type(type_input)
        display_pokemon(fetched_data, type_input)
        print()
        stop_requested = is_stop_requested()

    conn.commit()
    print("Pipeline complete.")
    conn.close()

if __name__ == "__main__":
    main()