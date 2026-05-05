import logging

logger = logging.getLogger(__name__)

REQUIRED_FIELDS = ["name", "height", "weight", "types"]

def is_valid_pokemon(row):
    for field in REQUIRED_FIELDS:
        if field not in row:
            logger.warning(f"Skipping record: missing required field '{field}'")
            return False
    
    if not row["types"]:
        logger.warning(f"Skipping {row['name']}: no type data found")
        return False
    
    return True

def get_valid_types(row):
    pokemon_types = []

    for typ in row["types"]:
        if "type" not in typ or "name" not in typ["type"]:
            logger.warning(f"Skipping malformed type entry for {row['name']}")
            continue

        pokemon_types.append(typ["type"]["name"])

    return pokemon_types

def transform(raw_data):
    transformed = []

    for row in raw_data:
        if not is_valid_pokemon(row):
            continue

        pokemon_types = get_valid_types(row)
        if not pokemon_types:
            logger.warning(f"Skipping {row['name']}: no valid type names found")
            continue

        transformed.append({
            "name": row["name"],
            "height": row["height"],
            "weight": row["weight"],
            "types": pokemon_types
        })

    return transformed