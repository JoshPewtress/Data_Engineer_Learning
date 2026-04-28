from database import create_connection
from extract import extract, get_pokemon_input
from transform import transform
from load import create_tables, clear_tables, load
from query import get_available_types, get_pokemon_type
from display import display_available_types, display_pokemon, get_type_input, is_stop_requested


def main():
    conn = create_connection()

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

    create_tables(conn)
    clear_tables(conn)

    print("Loading data...")
    load(conn, transformed)

    pokemon_types = get_available_types(conn)

    stop_requested = False
    while not stop_requested:
        display_available_types(pokemon_types)

        type_input = get_type_input()
        if not type_input:
            print("No Pokémon type entered.")
            conn.close()
            return
        
        fetched_data = get_pokemon_type(conn, type_input)
        display_pokemon(fetched_data, type_input)
        print()
        stop_requested = is_stop_requested()

    conn.commit()
    print("Pipeline complete.")
    conn.close()

if __name__ == "__main__":
    main()