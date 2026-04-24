import sqlite3
import json

RAW_FILE_PATH = "data/raw/pokemon_data.json"
DB_PATH = "data/database/pokemon.db"

def read_from_json(file_path):
    with open(file_path, "r") as file:
        return json.load(file)

def create_tables(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS pokemon(
    id INTEGER PRIMARY KEY,
    name TEXT UNIQUE,
    height INTEGER,
    weight INTEGER
    )
    """)
    
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS pokemon_experience(
        id INTEGER PRIMARY KEY,
        pokemon_id INTEGER,
        base_experience INTEGER,
        FOREIGN KEY (pokemon_id) REFERENCES pokemon(id)
        )
        """)

def clear_tables(cursor):
    cursor.execute("DELETE FROM pokemon_experience")
    cursor.execute("DELETE FROM pokemon")

def insert_pokemon(cursor, row):
    cursor.execute("""
    INSERT INTO pokemon (name, height, weight)
    VALUES (?, ?, ?)
    """, (row["name"], row["height"], row["weight"]))
    
    pokemon_id = cursor.lastrowid

    cursor.execute("""
    INSERT INTO pokemon_experience(pokemon_id, base_experience)
    VALUES (?, ?)
    """, (pokemon_id, row["base_experience"]))

def load_pokemon_data(cursor, pokemon_data):
    for row in pokemon_data:
        insert_pokemon(cursor, row)

def get_high_experience_pokemon(cursor, min_exp):
    cursor.execute("""
    SELECT p.id, p.name, p.height, p.weight, pe.base_experience
    FROM pokemon p
    JOIN pokemon_experience pe ON pe.pokemon_id = p.id
    WHERE pe.base_experience > ?
    ORDER BY pe.base_experience DESC
    LIMIT 3
    """, (min_exp,))
    
    return cursor.fetchall()
    
def display_pokemon(rows):
    for row in rows:
        print(f"{row['name'].capitalize()} - {row['base_experience']}")

def main():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    create_tables(cursor)
    clear_tables(cursor)

    pokemon_data = read_from_json(RAW_FILE_PATH)
    load_pokemon_data(cursor, pokemon_data)

    high_experience_pokemon = get_high_experience_pokemon(cursor, 100)

    print("Top Pokémon by Base Experience:")
    display_pokemon(high_experience_pokemon)
    print()

    conn.commit()
    conn.close()

if __name__ == "__main__":
    main()