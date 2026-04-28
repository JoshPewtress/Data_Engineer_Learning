from database import execute_command

def create_tables(conn):
    execute_command(conn, """
        CREATE TABLE IF NOT EXISTS pokemon(
        id INTEGER PRIMARY KEY,
        name TEXT UNIQUE,
        height INTEGER,
        weight INTEGER
        )
    """)
    
    execute_command(conn, """
        CREATE TABLE IF NOT EXISTS pokemon_types(
        id INTEGER PRIMARY KEY,
        pokemon_id INTEGER,
        pokemon_type TEXT,
        FOREIGN KEY (pokemon_id) REFERENCES pokemon(id)
        )
    """)

def clear_tables(conn):
    execute_command(conn, "DELETE FROM pokemon_types")
    execute_command(conn, "DELETE FROM pokemon")

def insert_pokemon(conn, data):
    return execute_command(conn, """
        INSERT INTO pokemon (name, height, weight)
        VALUES (:name, :height, :weight)
    """, {"name": data["name"], "height": data["height"], "weight": data["weight"]})

def insert_pokemon_types(conn, pokemon_id, data):
    for pokemon_type in data["types"]:
        execute_command(conn, """
        INSERT INTO pokemon_types (pokemon_id, pokemon_type)
        VALUES (:pokemon_id, :pokemon_type)
    """, {"pokemon_id": pokemon_id, "pokemon_type": pokemon_type})

def load(conn, data):
    for row in data:
        pokemon_id = insert_pokemon(conn, row)
        insert_pokemon_types(conn, pokemon_id, row)