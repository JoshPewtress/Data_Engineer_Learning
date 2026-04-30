from config import DEFAULT_POKEMON_INPUT, DEFAULT_TYPE_INPUT
from database import create_connection
from pokemon_repository import PokemonRepository
from extract import extract, get_pokemon_input
from transform import transform
from display import display_available_types, display_pokemon, get_type_input, is_stop_requested, log


def main(pokemon_input=None, type_input=None, interactive=False):
    conn = create_connection()
    repo = PokemonRepository(conn)
    
    repo.create_tables()
    repo.clear_tables()

    if not pokemon_input:
        pokemon_input = DEFAULT_POKEMON_INPUT

    if not type_input:
        type_input = DEFAULT_TYPE_INPUT

    if interactive:
        pokemon_input = get_pokemon_input()

    log("Extracting data...")
    raw_data = extract(pokemon_input)

    if not raw_data:
        log("Pipeline stopped: no valid Pokémon data.")
        conn.close()
        return

    log("Transforming data...")
    transformed = transform(raw_data)

    log("Loading data...")
    repo.load(transformed)

    pokemon_types = [row["pokemon_type"] for row in repo.get_available_types()]

    if interactive:
        stop_requested = False
        while not stop_requested:
            display_available_types(pokemon_types)
            type_input = get_type_input(pokemon_types)

            display_pokemon(repo.get_pokemon_type(type_input))
            stop_requested = is_stop_requested()
    else:
        display_pokemon(repo.get_pokemon_type(type_input))

    conn.commit()
    log("Pipeline complete.")
    conn.close()


if __name__ == "__main__":
    main(DEFAULT_POKEMON_INPUT, DEFAULT_TYPE_INPUT)