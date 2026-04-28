from database import execute_query

def get_available_types(conn):
    return execute_query(conn, """
        SELECT DISTINCT pokemon_type
        FROM pokemon_types
        ORDER BY pokemon_type ASC
    """)

def get_pokemon_type(conn, type_input):
    return execute_query(conn, """
        SELECT p.name, pt.pokemon_type
        FROM pokemon p
        JOIN pokemon_types pt ON pt.pokemon_id = p.id
        WHERE pt.pokemon_type = :pokemon_type
        ORDER BY p.name ASC
    """, {'pokemon_type': type_input.lower()})