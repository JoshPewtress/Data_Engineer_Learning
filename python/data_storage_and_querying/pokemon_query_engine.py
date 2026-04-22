import sqlite3

def get_high_experience_pokemon(cursor, min_exp):
    cursor.execute("""
                    SELECT id, name, height, weight, base_experience 
                    FROM pokemon
                    WHERE base_experience > ?
                    ORDER BY base_experience DESC
                    LIMIT 3
                    """, (min_exp,))
    rows = cursor.fetchall()
    return [extract_pokemon_fields(row) for row in rows]

def get_lightweight_pokemon(cursor, max_weight):
    cursor.execute("""
                    SELECT id, name, height, weight, base_experience
                    FROM pokemon 
                    WHERE weight < ? 
                    ORDER BY weight ASC
                    """, (max_weight,))
    rows = cursor.fetchall()
    return [extract_pokemon_fields(row) for row in rows]

def display_pokemon(title, rows, field):
    print(title)
    for row in rows:
        print(f"Name: {row['name'].capitalize()} | {field.capitalize()}: {row[field]}")
    print()

def extract_pokemon_fields(row):
    return {
        "id": row["id"],
        "name": row["name"],
        "height": row["height"],
        "weight": row["weight"],
        "base_experience": row["base_experience"]
    }

def main():
    conn = sqlite3.connect('data/pokemon.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    high_experience_pokemon = get_high_experience_pokemon(cursor, 100)
    lightweight_pokemon = get_lightweight_pokemon(cursor, 100)

    display_pokemon("Top Pokémon by Base Experience:", high_experience_pokemon, "base_experience")
    display_pokemon("Lightest Pokémon by Weight:", lightweight_pokemon, "weight")

    conn.close()

if __name__ == "__main__":
    main()