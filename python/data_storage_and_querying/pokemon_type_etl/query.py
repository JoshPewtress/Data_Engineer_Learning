def get_available_types(cursor):
    cursor.execute(
        """
        SELECT DISTINCT pokemon_type
        FROM pokemon_types
        ORDER BY pokemon_type ASC
        """)
    return cursor.fetchall()

def get_pokemon_type(cursor, type_input):
    cursor.execute(
        """
        SELECT p.name, pt.pokemon_type
        FROM pokemon p
        JOIN pokemon_types pt ON pt.pokemon_id = p.id
        WHERE pt.pokemon_type = :pokemon_type
        ORDER BY p.name ASC
        """, {'pokemon_type': type_input.lower()})
    return cursor.fetchall()