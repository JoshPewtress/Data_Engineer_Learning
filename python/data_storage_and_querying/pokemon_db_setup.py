import sqlite3
import json

FILE_PATH = "data/raw/pokemon_data.json"

def read_json_file(file_path):
    with open(file_path, "r") as file:
        return json.load(file)
    
def insert_data_into_rows(pokemon_data, cursor):
    for pokemon in pokemon_data:
        name = pokemon["name"]
        height = pokemon["height"]
        weight = pokemon["weight"]
        base_experience = pokemon["base_experience"]

        cursor.execute("""
        INSERT INTO pokemon (name, height, weight, base_experience)
        VALUES (?, ?, ?, ?)
        """, (name, height, weight, base_experience))

def preview_pokemon(cursor):
    cursor.execute("SELECT * FROM pokemon")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

def main():
    conn = sqlite3.connect("data/pokemon.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS pokemon (
        id INTEGER PRIMARY KEY,
        name TEXT UNIQUE,
        height INTEGER,
        weight INTEGER,
        base_experience INTEGER
    )
    """)

    pokemon_data = read_json_file(FILE_PATH)
    insert_data_into_rows(pokemon_data, cursor)
    preview_pokemon(cursor)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    main()