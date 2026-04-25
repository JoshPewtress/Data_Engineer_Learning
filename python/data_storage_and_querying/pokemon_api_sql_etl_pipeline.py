import sqlite3
import requests

DB_PATH = "data/database/pokemon.db"
URL_PATH = "https://pokeapi.co/api/v2/"

def create_tables(cursor):
    cursor.execute(create_pokemon_table_sql())
    cursor.execute(create_pokemon_types_table_sql())

def clear_tables(cursor):
    cursor.execute("DELETE FROM pokemon_types")
    cursor.execute("DELETE FROM pokemon")

def create_pokemon_table_sql():
    return """
        CREATE TABLE IF NOT EXISTS pokemon(
        id INTEGER PRIMARY KEY,
        name TEXT UNIQUE,
        height INTEGER,
        weight INTEGER
        )
        """

def create_pokemon_types_table_sql():
    return """
        CREATE TABLE IF NOT EXISTS pokemon_types(
        id INTEGER PRIMARY KEY,
        pokemon_id INTEGER,
        pokemon_type TEXT,
        FOREIGN KEY (pokemon_id) REFERENCES pokemon(id)
        )
        """

def insert_pokemon(cursor, data):
    cursor.execute("""
                INSERT INTO pokemon (name, height, weight)
                VALUES (?, ?, ?)""", 
                (data["name"], data["height"], data["weight"]))
    return cursor.lastrowid

def insert_pokemon_types(cursor, pokemon_id, data):
    for pokemon_type in data["types"]:
        cursor.execute("""
                INSERT INTO pokemon_types (pokemon_id, pokemon_type)
                VALUES (?, ?)""",
                (pokemon_id, pokemon_type))

def get_pokemon_input():
    user_input = input("Enter Pokémon names separated by commas: ")
    return [name.strip().lower() for name in user_input.split(",") if name.strip()]

def get_available_types(cursor):
    cursor.execute("""
                   SELECT DISTINCT pokemon_type
                   FROM pokemon_types
                   ORDER BY pokemon_type ASC
                   """)
    return cursor.fetchall()

def display_available_types(rows):
    print()
    print("Available Pokémon types:")
    for row in rows:
        print(f"- {row['pokemon_type']}")
    print()

def get_type_input():
    return input("Enter Pokémon type to search for: ").strip().lower()

def get_pokemon_type(cursor, pokemon_type):
    print("Querying data...")
    cursor.execute("""
                   SELECT p.name, pt.pokemon_type
                   FROM pokemon p
                   JOIN pokemon_types pt ON pt.pokemon_id = p.id
                   WHERE pt.pokemon_type = :pokemon_type
                   ORDER BY p.name ASC
                   """, {'pokemon_type': pokemon_type})
    return cursor.fetchall()

def display_pokemon(fetched_data, pokemon_type):
    print()
    print(f"{pokemon_type.capitalize()}-type Pokémon:")

    if not fetched_data:
        print("No Pokémon found for this type.")
        return

    for row in fetched_data:
        print(f"{row['name'].capitalize()} — {row['pokemon_type']}")

def is_stop_requested():
    while True:
        user_input = input("Search by type again (Y/N): ").strip().lower()
        if user_input == "y":
            return False
        elif user_input == "n":
            return True
        else:
            print("Please enter 'Y' or 'N'.")

def extract(pokemon_names):
    raw_data = []
    print("Extracting data...")

    for name in pokemon_names:
        name = name.strip().lower()
        if not name:
            continue

        url = f"{URL_PATH}pokemon/{name}"
        response = requests.get(url)
        if response.status_code != 200:
            continue
        raw_data.append(response.json())
    
    return raw_data
    
def transform(raw_data):
    transformed_data = []
    print("Transforming data...")

    for row in raw_data:
        transformed_data.append({
            "name": row["name"],
            "height": row["height"],
            "weight": row["weight"],
            "types": [typ["type"]["name"] for typ in row["types"]]
        })
    
    return transformed_data

def load(cursor, transformed_data):
    print("Loading data...")
    for pokemon in transformed_data:
        pokemon_id = insert_pokemon(cursor, pokemon)
        insert_pokemon_types(cursor, pokemon_id, pokemon)

def main():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    create_tables(cursor)
    clear_tables(cursor)

    pokemon_input = get_pokemon_input()
    if not pokemon_input:
        print("No valid Pokémon names entered.")
        conn.close()
        return
    
    raw_data = extract(pokemon_input)
    if not raw_data:
        print("No valid Pokémon data retrieved from API.")
        conn.close()
        return
    
    transformed_data = transform(raw_data)
    load(cursor, transformed_data)

    available_types = get_available_types(cursor)
    stop_requested = False
    while not stop_requested:
        display_available_types(available_types)
        type_input = get_type_input()
        if not type_input:
            print("No Pokémon type entered.")
            conn.close()
            return

        fetched_data = get_pokemon_type(cursor, type_input)
        display_pokemon(fetched_data, type_input)
        print()
        stop_requested = is_stop_requested()

    conn.commit()
    print("Pipeline complete.")
    conn.close()

if __name__ == "__main__":
    main()