from database import execute_command, execute_insert, execute_query

class PokemonRepository:

    def __init__(self, conn):
        self.conn = conn

    def create_tables(self):
        execute_command(self.conn, """
            CREATE TABLE IF NOT EXISTS pokemon (
            id INTEGER PRIMARY KEY,
            name TEXT UNIQUE,
            height INTEGER,
            weight INTEGER
            )
        """)

        execute_command(self.conn, """
            CREATE TABLE IF NOT EXISTS pokemon_types (
            id INTEGER PRIMARY KEY,
            pokemon_id INTEGER,
            pokemon_type TEXT,
            FOREIGN KEY (pokemon_id) REFERENCES pokemon(id)
            )
        """)

    def clear_tables(self):
        execute_command(self.conn, "DELETE FROM pokemon_types")
        execute_command(self.conn, "DELETE FROM pokemon")

    def load(self, data):
        for row in data:
            pokemon_id = self.insert_pokemon(row)
            self.insert_pokemon_types(pokemon_id, row)

    def insert_pokemon(self, data):
        return execute_insert(self.conn, """
            INSERT INTO pokemon (name, height, weight)
            VALUES (:name, :height, :weight)
        """, {'name': data["name"], 'height': data["height"], 'weight': data["weight"]})

    def insert_pokemon_types(self, pokemon_id, data):
        for pokemon_type in data["types"]:
            execute_command(self.conn, """
                INSERT INTO pokemon_types (pokemon_id, pokemon_type)
                VALUES (:pokemon_id, :pokemon_type)
            """, {'pokemon_id': pokemon_id, 'pokemon_type': pokemon_type})

    def get_available_types(self):
        return execute_query(self.conn, """
            SELECT DISTINCT pokemon_type
            FROM pokemon_types
            ORDER BY pokemon_type ASC
        """)

    def get_pokemon_type(self, type_input):
        return execute_query(self.conn, """
            SELECT p.name, pt.pokemon_type
            FROM pokemon p
            JOIN pokemon_types pt ON pt.pokemon_id = p.id
            WHERE pt.pokemon_type = :pokemon_type
            ORDER BY p.name ASC
        """, {'pokemon_type': type_input.lower()})
