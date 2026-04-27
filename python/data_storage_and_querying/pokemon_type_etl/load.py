def create_tables(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS pokemon(
        id INTEGER PRIMARY KEY,
        name TEXT UNIQUE,
        height INTEGER,
        weight INTEGER
        )
        """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS pokemon_types(
        id INTEGER PRIMARY KEY,
        pokemon_id INTEGER,
        pokemon_type TEXT,
        FOREIGN KEY (pokemon_id) REFERENCES pokemon(id)
        )
        """)

def clear_tables(cursor):
    cursor.execute("DELETE FROM pokemon_types")
    cursor.execute("DELETE FROM pokemon")

def insert_pokemon(cursor, data):
    cursor.execute(
        """
        INSERT INTO pokemon (name, height, weight)
        VALUES (?, ?, ?)
        """, (data["name"], data["height"], data["weight"]))
    return cursor.lastrowid

def insert_pokemon_types(cursor, pokemon_id, data):
    for pokemon_type in data["types"]:
        cursor.execute(
        """
        INSERT INTO pokemon_types (pokemon_id, pokemon_type)
        VALUES (?, ?)
        """, (pokemon_id, pokemon_type))

def load(cursor, data):
    for row in data:
        pokemon_id = insert_pokemon(cursor, row)
        insert_pokemon_types(cursor, pokemon_id, row)